from __future__ import print_function
import time
import mips_api_client
from mips_api_client.rest import ApiException
from pprint import pprint
import json
import argparse
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
from traitlets import default
import logging
import subprocess
from math import ceil
from glob import glob
import pathlib
from collections import defaultdict
from itertools import chain
import concurrent.futures
from threading import Lock
import os

from functools import partialmethod


bar_format = "{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
data_lock = Lock()
data_cnt = 0
data_completed = 0
data_bar = tqdm(total=0, desc='Data upload', position=1,
                leave=False, bar_format=bar_format)
enrich_lock = Lock()
enrich_cnt = 0
enrich_completed = 0
enrich_bar = tqdm(total=0, desc='Enrichment upload',
                  position=2, leave=False, bar_format=bar_format)
data_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
enrich_executor = concurrent.futures.ThreadPoolExecutor(max_workers=6)
data_futures = []
enrich_futures = []

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s][%(levelname)s] %(message)s')
LOGGER = logging.getLogger('upload_db')

# Configure API key authorization: APIKeyHeader
configuration = mips_api_client.Configuration()
env_var = os.environ
configuration.api_key['X-API-KEY'] = env_var['UIUC_MIPS_API_KEY']
configuration.host = env_var.get('UIUC_MIPS_API_ENDPOINT', 'http://incas.csl.illinois.edu:10003')
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = mips_api_client.AdminApi(
    mips_api_client.ApiClient(configuration))
# body = mips_api_client.RawDataPostRequest() # RawDataPostRequest |

parser = argparse.ArgumentParser()
parser.add_argument("--data_folder", type=str,
                    help="specify path of data folder")
parser.add_argument("--read_batchsize", type=int, default=5000,
                    help="specify batch size when uploading data")
parser.add_argument("--batchsize", type=int, default=5000,
                    help="specify batch size when uploading data")
args = parser.parse_args()

data_folder = args.data_folder
data_folder = pathlib.Path(data_folder).expanduser().resolve()
files = [f for f in glob(str(data_folder.joinpath('*.jsonl')))]


def submit_data_batch(raw_entries):
    global data_lock, data_completed, data_bar
    try:
        body = mips_api_client.RawDataPostRequest(
            override=False,
            data=[mips_api_client.RawDataPostEntry(
                source=mips_api_client.Source(
                    id=source_id, platform='Twitter', type='Twitter'),
                items=item
            ) for source_id, item in raw_entries.items()]
        )
        res = api_instance.admin_data_post(body)
        with data_lock:
            data_completed += 1
            data_bar.update(1)
    except ApiException as e:
        LOGGER.error(
            "Exception when calling AdminApi->admin_data_post: %s\n" % e)
        os._exit(0)
    else:
        return res.source_id_map, res.item_id_map


raw_entries = defaultdict(list)
for filename in files:
    LOGGER.info(f'Reading {filename}')
    # Process messages line by line
    with open(filename, 'r') as json_file:
        for line in tqdm(json_file, desc="File read",
                         total=int(subprocess.check_output(
                             ['wc', '-l', filename]).decode("utf8").split()[0]),
                         leave=False, bar_format=bar_format):
            # Interpret as a dict
            data = json.loads(line)
            m_obj = mips_api_client.Item(
                id=data['id'],
                author=data['author'],
                platform=data['mediaType'],
                time_published=data['timePublished']
            )
            raw_entries[m_obj.author].append(m_obj)

            if len(raw_entries) % args.batchsize == 0:
                with data_lock:
                    data_cnt += 1
                    data_bar.total = data_cnt
                    data_bar.refresh()
                data_futures.append(data_executor.submit(
                    submit_data_batch, raw_entries))
                raw_entries = defaultdict(list)

                flag = False
                with data_lock:
                    if data_cnt - data_completed > 8:
                        flag = True
                while flag:
                    for future in data_futures:
                        if future.running():
                            try:
                                future.result()
                            except Exception as exc:
                                print('%r generated an exception: %s' %
                                      (future, exc))
                            with data_lock:
                                if data_cnt - data_completed <= 4:
                                    flag = False
                                    break

data_futures.append(data_executor.submit(submit_data_batch, raw_entries))
for future in data_futures:
    if future.running():
        try:
            future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (future, exc))

data_executor.shutdown()
enrich_executor.shutdown()

data_bar.close()
enrich_bar.close()

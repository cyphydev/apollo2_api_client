from tqdm import tqdm
from math import ceil
import apollo2_api_client
from itertools import chain
import contextlib
import joblib
from functools import partial
from math import ceil
from threading import Lock

def get_all_actors(
    client, *,
    batch_size,
    limit,
    last,
    end,
    with_enrichment,
    with_cluster,
    enrichment_name,
    enrichment_provider,
    enrichment_tag,
    enrichment_version,
    cluster_name,
    cluster_provider,
    cluster_tag,
    cluster_version,
    platform,
    identifier,
):
    actor_api = apollo2_api_client.SourceApi(client)
    lock = Lock()
    aug_kwargs = {}
    if identifier:
        if 'filtered_actor_' in identifier:
            identifier = identifier.replace('filtered_actor_', 'filtered_')
        aug_kwargs["identifier"] = identifier
    if platform:
        aug_kwargs["platform"] = platform
    max_id = actor_api.source_max_id_get(**aug_kwargs)
    total = actor_api.source_count_get(**aug_kwargs)
    aug_kwargs.update(kwargs)
    prog_bar = tqdm(total=total, desc='Loading actors', position=2, leave=False, bar_format=bar_format)

    def get_batch(last, end):
        # partial_total = actor_api.actor_count_get(last=last, end=end)
        inret = actor_api.source_get(
            limit=bsize,
            last=last,
            end=end,
            **aug_kwargs)
        # assert len(inret) == partial_total
        with lock:
            prog_bar.update(len(inret))
        return inret

    ret = joblib.Parallel(n_jobs=2, prefer="threads")(
        joblib.delayed(get_batch)(i, i + bsize) for i in range(0, max_id + 1, bsize))
    prog_bar.close()
    ret = list(chain(*ret))
    assert len(ret) == total
    return ret

def get_all_message(bsize, identifier, platform, **kwargs):
    msg_api = self.msg_api_instance
    lock = Lock()
    aug_kwargs = {}
    if identifier:
        aug_kwargs["identifier"] = identifier
    if platform:
        aug_kwargs["platform"] = platform
    max_id = msg_api.item_max_id_get(**aug_kwargs)
    total = msg_api.item_count_get(**aug_kwargs)
    aug_kwargs.update(kwargs)
    prog_bar = tqdm(total=total, desc='Loading messages', position=1, leave=False, bar_format=bar_format)

    def get_batch(last, end):
        inret = msg_api.item_get(
            limit=bsize,
            last=last,
            end=end,
            **aug_kwargs)
        with lock:
            prog_bar.update(len(inret))
        return inret

    ret = joblib.Parallel(n_jobs=4, prefer="threads")(
        joblib.delayed(get_batch)(i, i + bsize) for i in range(0, max_id + 1, bsize))
    prog_bar.close()
    ret = list(chain(*ret))
    assert len(ret) == total
    return ret

def get_all_data():
    def wrap_f(f):
        return f()

    actor_func = partial(get_all_actor, bsize=batchsize,
                            identifier=self.data_identifier,
                            platform=self.media_type,
                            with_enrichment=True,
                            enrichment_provider=self.actor_provider_name,
                            enrichment_tag=self.actor_enrichment_tag,
                            enrichment_version=self.actor_enrichment_version
                        )
    msg_func = partial(get_all_message, bsize=batchsize,
                        identifier=self.data_identifier,
                        platform=self.media_type,
                        with_enrichment=True,
                        enrichment_provider=self.message_provider_name,
                        enrichment_tag=self.message_enrichment_tag,
                        enrichment_version=self.message_enrichment_version)
    messages, actors = joblib.Parallel(n_jobs=2, prefer="threads")(
        joblib.delayed(wrap_f)(f) for f in [msg_func, actor_func])
    return messages, actors
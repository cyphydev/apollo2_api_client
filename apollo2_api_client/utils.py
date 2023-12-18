from functools import partial
from itertools import chain
from threading import Lock

import joblib
from tqdm import tqdm

from apollo2_api_client.api.cluster_api import ClusterApi
from apollo2_api_client.api.enrichment_api import EnrichmentApi
from apollo2_api_client.api.identifier_api import IdentifierApi
from apollo2_api_client.api.item_api import ItemApi
from apollo2_api_client.api.source_api import SourceApi


def get_all_sources_multithreaded(
    client, *,
    batch_size=5000,
    n_workers=2,
    with_enrichment=False,
    with_cluster=False,
    enrichment_name=None,
    enrichment_provider=None,
    enrichment_tag=None,
    enrichment_version=None,
    cluster_name=None,
    cluster_provider=None,
    cluster_tag=None,
    cluster_version=None,
    platform=None,
    identifier=None,
    show_tqdm=True,
    tqdm_position=0,
    tqdm_leave=False,
):
    aug_kwargs = {}
    if enrichment_name is not None:
        aug_kwargs["enrichment_name"] = enrichment_name
    if enrichment_provider is not None:
        aug_kwargs["enrichment_provider"] = enrichment_provider
    if enrichment_tag is not None:
        aug_kwargs["enrichment_tag"] = enrichment_tag
    if enrichment_version is not None:
        aug_kwargs["enrichment_version"] = enrichment_version
    if cluster_name is not None:
        aug_kwargs["cluster_name"] = cluster_name
    if cluster_provider is not None:
        aug_kwargs["cluster_provider"] = cluster_provider
    if cluster_tag is not None:
        aug_kwargs["cluster_tag"] = cluster_tag
    if cluster_version is not None:
        aug_kwargs["cluster_version"] = cluster_version
    if platform:
        aug_kwargs["platform"] = platform
    if identifier:
        if 'filtered_actor_' in identifier:
            identifier = identifier.replace('filtered_actor_', 'filtered_')
        aug_kwargs["identifier"] = identifier

    actor_api = SourceApi(client)
    max_id = actor_api.source_max_id_get(**aug_kwargs)
    total = actor_api.source_count_get(**aug_kwargs)

    prog_lock = Lock()
    prog_bar = None
    if show_tqdm:
        prog_bar = tqdm(
            total=total, desc='Loading actors', ncols=100,
            position=tqdm_position, leave=tqdm_leave,
            bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
        )

    def get_batch(last, end):
        _ret = actor_api.source_get(
            limit=batch_size,
            last=last,
            end=end,
            with_enrichment=with_enrichment,
            with_cluster=with_cluster,
            **aug_kwargs
        )
        if prog_bar is not None:
            with prog_lock:
                prog_bar.update(len(_ret))
        return _ret

    ret = joblib.Parallel(n_jobs=n_workers, prefer="threads")(
        joblib.delayed(get_batch)(i, i + batch_size)
        for i in range(0, max_id + 1, batch_size)
    )
    if prog_bar is not None:
        prog_bar.close()
    ret = list(chain(*ret))
    assert len(ret) == total
    return ret

def get_all_items_multithreaded(
    client, *,
    batch_size=5000,
    n_workers=2,
    actor_ids=None,
    with_enrichment=False,
    with_cluster=False,
    enrichment_name=None,
    enrichment_provider=None,
    enrichment_tag=None,
    enrichment_version=None,
    cluster_name=None,
    cluster_provider=None,
    cluster_tag=None,
    cluster_version=None,
    platform=None,
    identifier=None,
    inclusive_begin_datetime=None,
    exclusive_end_datetime=None,
    show_tqdm=True,
    tqdm_position=0,
    tqdm_leave=False,
):
    aug_kwargs = {}
    if actor_ids is not None:
        aug_kwargs["actor_ids"] = actor_ids
    if enrichment_name is not None:
        aug_kwargs["enrichment_name"] = enrichment_name
    if enrichment_provider is not None:
        aug_kwargs["enrichment_provider"] = enrichment_provider
    if enrichment_tag is not None:
        aug_kwargs["enrichment_tag"] = enrichment_tag
    if enrichment_version is not None:
        aug_kwargs["enrichment_version"] = enrichment_version
    if cluster_name is not None:
        aug_kwargs["cluster_name"] = cluster_name
    if cluster_provider is not None:
        aug_kwargs["cluster_provider"] = cluster_provider
    if cluster_tag is not None:
        aug_kwargs["cluster_tag"] = cluster_tag
    if cluster_version is not None:
        aug_kwargs["cluster_version"] = cluster_version
    if inclusive_begin_datetime is not None:
        aug_kwargs["inclusive_begin_datetime"] = inclusive_begin_datetime
    if exclusive_end_datetime is not None:
        aug_kwargs["exclusive_end_datetime"] = exclusive_end_datetime
    if platform:
        aug_kwargs["platform"] = platform
    if identifier:
        if 'filtered_actor_' in identifier:
            identifier = identifier.replace('filtered_actor_', 'filtered_')
        aug_kwargs["identifier"] = identifier

    item_api = ItemApi(client)
    max_id = item_api.item_max_id_get(**aug_kwargs)
    total = item_api.item_count_get(**aug_kwargs)

    prog_lock = Lock()
    prog_bar = None
    if show_tqdm:
        prog_bar = tqdm(
            total=total, desc='Loading items', ncols=100,
            position=tqdm_position, leave=tqdm_leave,
            bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
        )

    def get_batch(last, end):
        _ret = item_api.item_get(
            limit=batch_size,
            last=last,
            end=end,
            with_enrichment=with_enrichment,
            with_cluster=with_cluster,
            **aug_kwargs
        )
        if prog_bar is not None:
            with prog_lock:
                prog_bar.update(len(_ret))
        return _ret

    ret = joblib.Parallel(n_jobs=n_workers, prefer="threads")(
        joblib.delayed(get_batch)(i, i + batch_size)
        for i in range(0, max_id + 1, batch_size)
    )
    if prog_bar is not None:
        prog_bar.close()
    ret = list(chain(*ret))
    assert len(ret) == total
    return ret

def get_all_data_multithreaded(
    client, *,
    batch_size=5000,
    source_n_workers=2,
    source_with_enrichment=False,
    source_with_cluster=False,
    source_enrichment_name=None,
    source_enrichment_provider=None,
    source_enrichment_tag=None,
    source_enrichment_version=None,
    source_cluster_name=None,
    source_cluster_provider=None,
    source_cluster_tag=None,
    source_cluster_version=None,
    source_platform=None,
    source_identifier=None,
    item_n_workers=2,
    item_actor_ids=None,
    item_with_enrichment=False,
    item_with_cluster=False,
    item_enrichment_name=None,
    item_enrichment_provider=None,
    item_enrichment_tag=None,
    item_enrichment_version=None,
    item_cluster_name=None,
    item_cluster_provider=None,
    item_cluster_tag=None,
    item_cluster_version=None,
    item_platform=None,
    item_identifier=None,
    item_inclusive_begin_datetime=None,
    item_exclusive_end_datetime=None,
    show_tqdm=True,
    tqdm_leave=False,
):
    def wrap_f(f):
        return f()
    item_func = partial(
        get_all_items_multithreaded,
        client=client,
        batch_size=batch_size,
        n_workers=item_n_workers,
        actor_ids=item_actor_ids,
        with_enrichment=item_with_enrichment,
        with_cluster=item_with_cluster,
        enrichment_name=item_enrichment_name,
        enrichment_provider=item_enrichment_provider,
        enrichment_tag=item_enrichment_tag,
        enrichment_version=item_enrichment_version,
        cluster_name=item_cluster_name,
        cluster_provider=item_cluster_provider,
        cluster_tag=item_cluster_tag,
        cluster_version=item_cluster_version,
        platform=item_platform,
        identifier=item_identifier,
        inclusive_begin_datetime=item_inclusive_begin_datetime,
        exclusive_end_datetime=item_exclusive_end_datetime,
        show_tqdm=show_tqdm,
        tqdm_position=0,
        tqdm_leave=tqdm_leave,
    )
    source_func = partial(
        get_all_sources_multithreaded,
        client=client,
        batch_size=batch_size,
        n_workers=source_n_workers,
        with_enrichment=source_with_enrichment,
        with_cluster=source_with_cluster,
        enrichment_name=source_enrichment_name,
        enrichment_provider=source_enrichment_provider,
        enrichment_tag=source_enrichment_tag,
        enrichment_version=source_enrichment_version,
        cluster_name=source_cluster_name,
        cluster_provider=source_cluster_provider,
        cluster_tag=source_cluster_tag,
        cluster_version=source_cluster_version,
        platform=source_platform,
        identifier=source_identifier,
        show_tqdm=show_tqdm,
        tqdm_position=1,
        tqdm_leave=tqdm_leave,
    )
    messages, actors = joblib.Parallel(n_jobs=2, prefer="threads")(
        joblib.delayed(wrap_f)(f) for f in [item_func, source_func]
    )
    return messages, actors

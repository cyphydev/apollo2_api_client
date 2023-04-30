from apollo2_api_client.paths.enrichments_meta.get import ApiForget
from apollo2_api_client.paths.enrichments_meta.post import ApiForpost
from apollo2_api_client.paths.enrichments_meta.delete import ApiFordelete


class EnrichmentsMeta(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

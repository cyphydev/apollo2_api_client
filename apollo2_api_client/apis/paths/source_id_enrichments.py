from apollo2_api_client.paths.source_id_enrichments.get import ApiForget
from apollo2_api_client.paths.source_id_enrichments.post import ApiForpost
from apollo2_api_client.paths.source_id_enrichments.delete import ApiFordelete


class SourceIdEnrichments(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

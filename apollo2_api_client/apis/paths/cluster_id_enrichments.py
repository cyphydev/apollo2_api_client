from apollo2_api_client.paths.cluster_id_enrichments.get import ApiForget
from apollo2_api_client.paths.cluster_id_enrichments.post import ApiForpost
from apollo2_api_client.paths.cluster_id_enrichments.delete import ApiFordelete


class ClusterIdEnrichments(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

from apollo2_api_client.paths.cluster.get import ApiForget
from apollo2_api_client.paths.cluster.post import ApiForpost
from apollo2_api_client.paths.cluster.delete import ApiFordelete


class Cluster(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

import typing_extensions

from apollo2_api_client.apis.tags import TagValues
from apollo2_api_client.apis.tags.admin_api import AdminApi
from apollo2_api_client.apis.tags.item_api import ItemApi
from apollo2_api_client.apis.tags.source_api import SourceApi
from apollo2_api_client.apis.tags.enrichment_api import EnrichmentApi
from apollo2_api_client.apis.tags.cluster_api import ClusterApi
from apollo2_api_client.apis.tags.graph_api import GraphApi
from apollo2_api_client.apis.tags.media_item_api import MediaItemApi
from apollo2_api_client.apis.tags.identifier_api import IdentifierApi
from apollo2_api_client.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ADMIN: AdminApi,
        TagValues.ITEM: ItemApi,
        TagValues.SOURCE: SourceApi,
        TagValues.ENRICHMENT: EnrichmentApi,
        TagValues.CLUSTER: ClusterApi,
        TagValues.GRAPH: GraphApi,
        TagValues.MEDIA_ITEM: MediaItemApi,
        TagValues.IDENTIFIER: IdentifierApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ADMIN: AdminApi,
        TagValues.ITEM: ItemApi,
        TagValues.SOURCE: SourceApi,
        TagValues.ENRICHMENT: EnrichmentApi,
        TagValues.CLUSTER: ClusterApi,
        TagValues.GRAPH: GraphApi,
        TagValues.MEDIA_ITEM: MediaItemApi,
        TagValues.IDENTIFIER: IdentifierApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

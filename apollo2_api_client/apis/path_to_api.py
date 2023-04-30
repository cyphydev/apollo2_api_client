import typing_extensions

from apollo2_api_client.paths import PathValues
from apollo2_api_client.apis.paths.ping import Ping
from apollo2_api_client.apis.paths.data import Data
from apollo2_api_client.apis.paths.status import Status
from apollo2_api_client.apis.paths.dbflush import Dbflush
from apollo2_api_client.apis.paths.item_count import ItemCount
from apollo2_api_client.apis.paths.item_max_id import ItemMaxId
from apollo2_api_client.apis.paths.item import Item
from apollo2_api_client.apis.paths.item_get import ItemGet
from apollo2_api_client.apis.paths.item_id_forward import ItemIdForward
from apollo2_api_client.apis.paths.item_id_forward_id import ItemIdForwardId
from apollo2_api_client.apis.paths.item_id_reverse import ItemIdReverse
from apollo2_api_client.apis.paths.item_id_reverse_id import ItemIdReverseId
from apollo2_api_client.apis.paths.item_id import ItemId
from apollo2_api_client.apis.paths.item_id_enrichments import ItemIdEnrichments
from apollo2_api_client.apis.paths.item_enrichments_get import ItemEnrichmentsGet
from apollo2_api_client.apis.paths.item_enrichments_submit import ItemEnrichmentsSubmit
from apollo2_api_client.apis.paths.item_enrichments_delete import ItemEnrichmentsDelete
from apollo2_api_client.apis.paths.item_attach_media import ItemAttachMedia
from apollo2_api_client.apis.paths.item_detach_media import ItemDetachMedia
from apollo2_api_client.apis.paths.item_identifer_post import ItemIdentiferPost
from apollo2_api_client.apis.paths.item_identifer_delete import ItemIdentiferDelete
from apollo2_api_client.apis.paths.item_id_identifer import ItemIdIdentifer
from apollo2_api_client.apis.paths.source_count import SourceCount
from apollo2_api_client.apis.paths.source_max_id import SourceMaxId
from apollo2_api_client.apis.paths.source import Source
from apollo2_api_client.apis.paths.source_get import SourceGet
from apollo2_api_client.apis.paths.source_id_forward import SourceIdForward
from apollo2_api_client.apis.paths.source_id_forward_id import SourceIdForwardId
from apollo2_api_client.apis.paths.source_id_reverse import SourceIdReverse
from apollo2_api_client.apis.paths.source_id_reverse_id import SourceIdReverseId
from apollo2_api_client.apis.paths.source_id import SourceId
from apollo2_api_client.apis.paths.source_id_enrichments import SourceIdEnrichments
from apollo2_api_client.apis.paths.source_enrichments_get import SourceEnrichmentsGet
from apollo2_api_client.apis.paths.source_enrichments_submit import SourceEnrichmentsSubmit
from apollo2_api_client.apis.paths.source_enrichments_delete import SourceEnrichmentsDelete
from apollo2_api_client.apis.paths.source_identifer_post import SourceIdentiferPost
from apollo2_api_client.apis.paths.source_identifer_delete import SourceIdentiferDelete
from apollo2_api_client.apis.paths.source_id_identifer import SourceIdIdentifer
from apollo2_api_client.apis.paths.enrichments_meta import EnrichmentsMeta
from apollo2_api_client.apis.paths.cluster import Cluster
from apollo2_api_client.apis.paths.cluster_id import ClusterId
from apollo2_api_client.apis.paths.cluster_id_members import ClusterIdMembers
from apollo2_api_client.apis.paths.cluster_id_delete_members import ClusterIdDeleteMembers
from apollo2_api_client.apis.paths.cluster_id_enrichments import ClusterIdEnrichments
from apollo2_api_client.apis.paths.cluster_enrichments_get import ClusterEnrichmentsGet
from apollo2_api_client.apis.paths.cluster_enrichments_submit import ClusterEnrichmentsSubmit
from apollo2_api_client.apis.paths.cluster_enrichments_delete import ClusterEnrichmentsDelete
from apollo2_api_client.apis.paths.cluster_identifer_post import ClusterIdentiferPost
from apollo2_api_client.apis.paths.cluster_identifer_delete import ClusterIdentiferDelete
from apollo2_api_client.apis.paths.cluster_id_identifer import ClusterIdIdentifer
from apollo2_api_client.apis.paths.graph import Graph
from apollo2_api_client.apis.paths.graph_id import GraphId
from apollo2_api_client.apis.paths.graph_id_edges import GraphIdEdges
from apollo2_api_client.apis.paths.graph_id_edit_edges import GraphIdEditEdges
from apollo2_api_client.apis.paths.graph_id_delete_edges import GraphIdDeleteEdges
from apollo2_api_client.apis.paths.graph_edge_identifer_post import GraphEdgeIdentiferPost
from apollo2_api_client.apis.paths.graph_edge_identifer_delete import GraphEdgeIdentiferDelete
from apollo2_api_client.apis.paths.graph_id_edge_identifer_all import GraphIdEdgeIdentiferAll
from apollo2_api_client.apis.paths.graph_id_edge_identifer import GraphIdEdgeIdentifer
from apollo2_api_client.apis.paths.media_item_count import MediaItemCount
from apollo2_api_client.apis.paths.media_item_max_id import MediaItemMaxId
from apollo2_api_client.apis.paths.media_item import MediaItem
from apollo2_api_client.apis.paths.media_item_get import MediaItemGet
from apollo2_api_client.apis.paths.media_item_id import MediaItemId
from apollo2_api_client.apis.paths.media_item_identifer_post import MediaItemIdentiferPost
from apollo2_api_client.apis.paths.media_item_identifer_delete import MediaItemIdentiferDelete
from apollo2_api_client.apis.paths.media_item_id_identifer import MediaItemIdIdentifer
from apollo2_api_client.apis.paths.identifier_list import IdentifierList
from apollo2_api_client.apis.paths.identifer_delete import IdentiferDelete

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PING: Ping,
        PathValues.DATA: Data,
        PathValues.STATUS: Status,
        PathValues.DBFLUSH: Dbflush,
        PathValues.ITEM_COUNT: ItemCount,
        PathValues.ITEM_MAX_ID: ItemMaxId,
        PathValues.ITEM: Item,
        PathValues.ITEM_GET: ItemGet,
        PathValues.ITEM_ID_FORWARD: ItemIdForward,
        PathValues.ITEM_ID_FORWARD_ID: ItemIdForwardId,
        PathValues.ITEM_ID_REVERSE: ItemIdReverse,
        PathValues.ITEM_ID_REVERSE_ID: ItemIdReverseId,
        PathValues.ITEM_ID: ItemId,
        PathValues.ITEM_ID_ENRICHMENTS: ItemIdEnrichments,
        PathValues.ITEM_ENRICHMENTS_GET: ItemEnrichmentsGet,
        PathValues.ITEM_ENRICHMENTS_SUBMIT: ItemEnrichmentsSubmit,
        PathValues.ITEM_ENRICHMENTS_DELETE: ItemEnrichmentsDelete,
        PathValues.ITEM_ATTACH_MEDIA: ItemAttachMedia,
        PathValues.ITEM_DETACH_MEDIA: ItemDetachMedia,
        PathValues.ITEM_IDENTIFER_POST: ItemIdentiferPost,
        PathValues.ITEM_IDENTIFER_DELETE: ItemIdentiferDelete,
        PathValues.ITEM_ID_IDENTIFER: ItemIdIdentifer,
        PathValues.SOURCE_COUNT: SourceCount,
        PathValues.SOURCE_MAX_ID: SourceMaxId,
        PathValues.SOURCE: Source,
        PathValues.SOURCE_GET: SourceGet,
        PathValues.SOURCE_ID_FORWARD: SourceIdForward,
        PathValues.SOURCE_ID_FORWARD_ID: SourceIdForwardId,
        PathValues.SOURCE_ID_REVERSE: SourceIdReverse,
        PathValues.SOURCE_ID_REVERSE_ID: SourceIdReverseId,
        PathValues.SOURCE_ID: SourceId,
        PathValues.SOURCE_ID_ENRICHMENTS: SourceIdEnrichments,
        PathValues.SOURCE_ENRICHMENTS_GET: SourceEnrichmentsGet,
        PathValues.SOURCE_ENRICHMENTS_SUBMIT: SourceEnrichmentsSubmit,
        PathValues.SOURCE_ENRICHMENTS_DELETE: SourceEnrichmentsDelete,
        PathValues.SOURCE_IDENTIFER_POST: SourceIdentiferPost,
        PathValues.SOURCE_IDENTIFER_DELETE: SourceIdentiferDelete,
        PathValues.SOURCE_ID_IDENTIFER: SourceIdIdentifer,
        PathValues.ENRICHMENTS_META: EnrichmentsMeta,
        PathValues.CLUSTER: Cluster,
        PathValues.CLUSTER_ID: ClusterId,
        PathValues.CLUSTER_ID_MEMBERS: ClusterIdMembers,
        PathValues.CLUSTER_ID_DELETE_MEMBERS: ClusterIdDeleteMembers,
        PathValues.CLUSTER_ID_ENRICHMENTS: ClusterIdEnrichments,
        PathValues.CLUSTER_ENRICHMENTS_GET: ClusterEnrichmentsGet,
        PathValues.CLUSTER_ENRICHMENTS_SUBMIT: ClusterEnrichmentsSubmit,
        PathValues.CLUSTER_ENRICHMENTS_DELETE: ClusterEnrichmentsDelete,
        PathValues.CLUSTER_IDENTIFER_POST: ClusterIdentiferPost,
        PathValues.CLUSTER_IDENTIFER_DELETE: ClusterIdentiferDelete,
        PathValues.CLUSTER_ID_IDENTIFER: ClusterIdIdentifer,
        PathValues.GRAPH: Graph,
        PathValues.GRAPH_ID: GraphId,
        PathValues.GRAPH_ID_EDGES: GraphIdEdges,
        PathValues.GRAPH_ID_EDIT_EDGES: GraphIdEditEdges,
        PathValues.GRAPH_ID_DELETE_EDGES: GraphIdDeleteEdges,
        PathValues.GRAPH_EDGE_IDENTIFER_POST: GraphEdgeIdentiferPost,
        PathValues.GRAPH_EDGE_IDENTIFER_DELETE: GraphEdgeIdentiferDelete,
        PathValues.GRAPH_ID_EDGE_IDENTIFER_ALL: GraphIdEdgeIdentiferAll,
        PathValues.GRAPH_ID_EDGE_IDENTIFER: GraphIdEdgeIdentifer,
        PathValues.MEDIA_ITEM_COUNT: MediaItemCount,
        PathValues.MEDIA_ITEM_MAX_ID: MediaItemMaxId,
        PathValues.MEDIA_ITEM: MediaItem,
        PathValues.MEDIA_ITEM_GET: MediaItemGet,
        PathValues.MEDIA_ITEM_ID: MediaItemId,
        PathValues.MEDIA_ITEM_IDENTIFER_POST: MediaItemIdentiferPost,
        PathValues.MEDIA_ITEM_IDENTIFER_DELETE: MediaItemIdentiferDelete,
        PathValues.MEDIA_ITEM_ID_IDENTIFER: MediaItemIdIdentifer,
        PathValues.IDENTIFIER_LIST: IdentifierList,
        PathValues.IDENTIFER_DELETE: IdentiferDelete,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PING: Ping,
        PathValues.DATA: Data,
        PathValues.STATUS: Status,
        PathValues.DBFLUSH: Dbflush,
        PathValues.ITEM_COUNT: ItemCount,
        PathValues.ITEM_MAX_ID: ItemMaxId,
        PathValues.ITEM: Item,
        PathValues.ITEM_GET: ItemGet,
        PathValues.ITEM_ID_FORWARD: ItemIdForward,
        PathValues.ITEM_ID_FORWARD_ID: ItemIdForwardId,
        PathValues.ITEM_ID_REVERSE: ItemIdReverse,
        PathValues.ITEM_ID_REVERSE_ID: ItemIdReverseId,
        PathValues.ITEM_ID: ItemId,
        PathValues.ITEM_ID_ENRICHMENTS: ItemIdEnrichments,
        PathValues.ITEM_ENRICHMENTS_GET: ItemEnrichmentsGet,
        PathValues.ITEM_ENRICHMENTS_SUBMIT: ItemEnrichmentsSubmit,
        PathValues.ITEM_ENRICHMENTS_DELETE: ItemEnrichmentsDelete,
        PathValues.ITEM_ATTACH_MEDIA: ItemAttachMedia,
        PathValues.ITEM_DETACH_MEDIA: ItemDetachMedia,
        PathValues.ITEM_IDENTIFER_POST: ItemIdentiferPost,
        PathValues.ITEM_IDENTIFER_DELETE: ItemIdentiferDelete,
        PathValues.ITEM_ID_IDENTIFER: ItemIdIdentifer,
        PathValues.SOURCE_COUNT: SourceCount,
        PathValues.SOURCE_MAX_ID: SourceMaxId,
        PathValues.SOURCE: Source,
        PathValues.SOURCE_GET: SourceGet,
        PathValues.SOURCE_ID_FORWARD: SourceIdForward,
        PathValues.SOURCE_ID_FORWARD_ID: SourceIdForwardId,
        PathValues.SOURCE_ID_REVERSE: SourceIdReverse,
        PathValues.SOURCE_ID_REVERSE_ID: SourceIdReverseId,
        PathValues.SOURCE_ID: SourceId,
        PathValues.SOURCE_ID_ENRICHMENTS: SourceIdEnrichments,
        PathValues.SOURCE_ENRICHMENTS_GET: SourceEnrichmentsGet,
        PathValues.SOURCE_ENRICHMENTS_SUBMIT: SourceEnrichmentsSubmit,
        PathValues.SOURCE_ENRICHMENTS_DELETE: SourceEnrichmentsDelete,
        PathValues.SOURCE_IDENTIFER_POST: SourceIdentiferPost,
        PathValues.SOURCE_IDENTIFER_DELETE: SourceIdentiferDelete,
        PathValues.SOURCE_ID_IDENTIFER: SourceIdIdentifer,
        PathValues.ENRICHMENTS_META: EnrichmentsMeta,
        PathValues.CLUSTER: Cluster,
        PathValues.CLUSTER_ID: ClusterId,
        PathValues.CLUSTER_ID_MEMBERS: ClusterIdMembers,
        PathValues.CLUSTER_ID_DELETE_MEMBERS: ClusterIdDeleteMembers,
        PathValues.CLUSTER_ID_ENRICHMENTS: ClusterIdEnrichments,
        PathValues.CLUSTER_ENRICHMENTS_GET: ClusterEnrichmentsGet,
        PathValues.CLUSTER_ENRICHMENTS_SUBMIT: ClusterEnrichmentsSubmit,
        PathValues.CLUSTER_ENRICHMENTS_DELETE: ClusterEnrichmentsDelete,
        PathValues.CLUSTER_IDENTIFER_POST: ClusterIdentiferPost,
        PathValues.CLUSTER_IDENTIFER_DELETE: ClusterIdentiferDelete,
        PathValues.CLUSTER_ID_IDENTIFER: ClusterIdIdentifer,
        PathValues.GRAPH: Graph,
        PathValues.GRAPH_ID: GraphId,
        PathValues.GRAPH_ID_EDGES: GraphIdEdges,
        PathValues.GRAPH_ID_EDIT_EDGES: GraphIdEditEdges,
        PathValues.GRAPH_ID_DELETE_EDGES: GraphIdDeleteEdges,
        PathValues.GRAPH_EDGE_IDENTIFER_POST: GraphEdgeIdentiferPost,
        PathValues.GRAPH_EDGE_IDENTIFER_DELETE: GraphEdgeIdentiferDelete,
        PathValues.GRAPH_ID_EDGE_IDENTIFER_ALL: GraphIdEdgeIdentiferAll,
        PathValues.GRAPH_ID_EDGE_IDENTIFER: GraphIdEdgeIdentifer,
        PathValues.MEDIA_ITEM_COUNT: MediaItemCount,
        PathValues.MEDIA_ITEM_MAX_ID: MediaItemMaxId,
        PathValues.MEDIA_ITEM: MediaItem,
        PathValues.MEDIA_ITEM_GET: MediaItemGet,
        PathValues.MEDIA_ITEM_ID: MediaItemId,
        PathValues.MEDIA_ITEM_IDENTIFER_POST: MediaItemIdentiferPost,
        PathValues.MEDIA_ITEM_IDENTIFER_DELETE: MediaItemIdentiferDelete,
        PathValues.MEDIA_ITEM_ID_IDENTIFER: MediaItemIdIdentifer,
        PathValues.IDENTIFIER_LIST: IdentifierList,
        PathValues.IDENTIFER_DELETE: IdentiferDelete,
    }
)

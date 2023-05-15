# generated by datamodel-codegen:
#   filename:  openapi_dm.json
#   timestamp: 2023-05-08T20:20:47+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, confloat


class AccountType(Enum):
    MEDIA_UNSPECIFIED = 'MEDIA_UNSPECIFIED'
    News = 'News'
    Reddit = 'Reddit'
    Twitter = 'Twitter'
    Webpage = 'Webpage'
    Blog = 'Blog'
    Comment = 'Comment'
    Facebook = 'Facebook'
    Forum = 'Forum'
    Google_Plus = 'Google Plus'
    LINE = 'LINE'
    Search_Result = 'Search Result'
    VK = 'VK'
    Bing = 'Bing'
    Wikipedia = 'Wikipedia'
    Other = 'Other'


class BatchGetRequest(BaseModel):
    ids: List[int] = Field(..., title='Ids')
    with_enrichment: Optional[bool] = Field([False], title='With Enrichment')
    enrichment_name: Optional[str] = Field(None, title='Enrichment Name')
    enrichment_provider: Optional[str] = Field(None, title='Enrichment Provider')
    enrichment_tag: Optional[str] = Field(None, title='Enrichment Tag')
    enrichment_version: Optional[str] = Field(None, title='Enrichment Version')
    with_cluster: Optional[bool] = Field([False], title='With Cluster')
    cluster_name: Optional[str] = Field(None, title='Cluster Name')
    cluster_provider: Optional[str] = Field(None, title='Cluster Provider')
    cluster_tag: Optional[str] = Field(None, title='Cluster Tag')
    cluster_version: Optional[str] = Field(None, title='Cluster Version')


class BatchMediaGetRequest(BaseModel):
    ids: List[int] = Field(..., title='Ids')


class ClusterMember(BaseModel):
    id: Optional[int] = Field(None, title='Id')
    cluster_id: int = Field(..., title='Cluster Id')
    node_id: int = Field(..., title='Node Id')
    data: Optional[Dict[str, Any]] = Field({}, title='Data')


class ClusterType(Enum):
    Segment = 'Segment'
    Claim = 'Claim'
    VisualTopic = 'VisualTopic'


class Edge(BaseModel):
    id: Optional[int] = Field(None, title='Id')
    graph_id: int = Field(..., title='Graph Id')
    src_id: int = Field(..., title='Src Id')
    dst_id: int = Field(..., title='Dst Id')
    type: str = Field(..., title='Type')
    timestamp: Optional[int] = Field(None, title='Timestamp')
    data: Optional[Dict[str, Any]] = Field({}, title='Data')


class EngagementType(Enum):
    ENGAGEMENT_UNSPECIFIED = 'ENGAGEMENT_UNSPECIFIED'
    mention = 'mention'
    quote = 'quote'
    reply = 'reply'
    retweet = 'retweet'
    tweet = 'tweet'
    page_post = 'page_post'


class EnrichmentType(Enum):
    Category = 'Category'
    Numerical = 'Numerical'
    Array = 'Array'
    Text = 'Text'
    List = 'List'
    Json = 'Json'


class EnrichmentsBatchRequest(BaseModel):
    ids: List[int] = Field(..., title='Ids')
    name: Optional[str] = Field(None, title='Name')
    provider: Optional[str] = Field(None, title='Provider')
    tag: Optional[str] = Field(None, title='Tag')
    version: Optional[str] = Field(None, title='Version')


class EntityType(Enum):
    ENTITY_UNSPECIFIED = 'ENTITY_UNSPECIFIED'
    Person = 'Person'
    Media = 'Media'
    Organization = 'Organization'
    Government = 'Government'


class GeoLocation(BaseModel):
    latitude: Optional[float] = Field(None, title='Latitude')
    longitude: Optional[float] = Field(None, title='Longitude')
    country_code: Optional[str] = Field(None, title='Country Code')


class GraphType(Enum):
    ItemItem = 'ItemItem'
    SourceItem = 'SourceItem'
    SourceSource = 'SourceSource'
    ItemMedia = 'ItemMedia'
    MediaMedia = 'MediaMedia'
    ClusterCluster = 'ClusterCluster'


class IncasExtraAttribute(BaseModel):
    name: Optional[str] = Field(None, title='Name')
    id: Optional[str] = Field(None, title='Id')
    provider_name: Optional[str] = Field(None, title='Provider Name')
    attribute_key: Optional[str] = Field(None, title='Attribute Key')
    attribute_value: Optional[str] = Field(None, title='Attribute Value')


class IncasLinks(BaseModel):
    messages: Optional[str] = Field(None, title='Messages')
    self: Optional[str] = Field(None, title='Self')


class IncasMediaResource(BaseModel):
    account_bio: Optional[str] = Field(None, title='Account Bio')
    account_id: Optional[str] = Field(None, title='Account Id')
    account_status: Optional[str] = Field(None, title='Account Status')
    account_type: Optional[AccountType] = None
    display_names: Optional[List[str]] = Field(None, title='Display Names')
    follower_count: Optional[int] = Field(None, title='Follower Count')
    friends_count: Optional[int] = Field(None, title='Friends Count')
    hashedUser_names: Optional[List[str]] = Field(None, title='Hasheduser Names')
    language: Optional[str] = Field(None, title='Language')
    url: Optional[str] = Field(None, title='Url')
    user_names: Optional[List[str]] = Field(None, title='User Names')
    verified: Optional[bool] = Field(None, title='Verified')


class IncasOffset(BaseModel):
    begin: Optional[int] = Field(None, title='Begin')
    end: Optional[int] = Field(None, title='End')


class IncasRedditData(BaseModel):
    pass


class IncasTwitterData(BaseModel):
    engagement_parent_id: Optional[str] = Field(None, title='Engagement Parent Id')
    engagement_type: Optional[EngagementType] = None
    follower_count: Optional[int] = Field(None, title='Follower Count')
    following_count: Optional[int] = Field(None, title='Following Count')
    like_count: Optional[int] = Field(None, title='Like Count')
    mentioned_users: Optional[List[str]] = Field(None, title='Mentioned Users')
    retweet_count: Optional[int] = Field(None, title='Retweet Count')
    tweet_id: Optional[str] = Field(None, title='Tweet Id')
    twitter_author_screenname: Optional[str] = Field(
        None, title='Twitter Author Screenname'
    )
    twitter_user_id: Optional[str] = Field(None, title='Twitter User Id')


class JsonEnrichment(BaseModel):
    name: str = Field(
        ..., description='The enrichment (e.g., name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    type: EnrichmentType = Field(EnrichmentType.Json, const=True)
    value: Dict[str, Any] = Field(..., title='Value')


class JsonEnrichmentMeta(BaseModel):
    description: str = Field(
        ..., description='Description of the enrichment algorithm.', title='Description'
    )
    name: str = Field(
        ..., description='The enrichment name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: EnrichmentType = Field(EnrichmentType.Json, const=True)


class ListEnrichment(BaseModel):
    name: str = Field(
        ..., description='The enrichment (e.g., name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    type: EnrichmentType = Field(EnrichmentType.List, const=True)
    value: List[Union[str, float]] = Field(..., title='Value')
    confidence: Optional[List[confloat(ge=0.0, le=1.0)]] = Field(
        None,
        description='The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0',
        title='Confidence',
    )


class ListEnrichmentMeta(BaseModel):
    description: str = Field(
        ..., description='Description of the enrichment algorithm.', title='Description'
    )
    name: str = Field(
        ..., description='The enrichment name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: EnrichmentType = Field(EnrichmentType.List, const=True)


class MediaItemType(Enum):
    Link = 'Link'
    Image = 'Image'


class ModifyMediaAttachmentRequest(BaseModel):
    item_ids: List[int] = Field(..., title='Item Ids')
    media_ids: List[int] = Field(..., title='Media Ids')
    data: Optional[List[Dict[str, Any]]] = Field(None, title='Data')
    ignore_missing_when_deleting: Optional[bool] = Field(
        True, title='Ignore Missing When Deleting'
    )


class NumericalEnrichment(BaseModel):
    name: str = Field(
        ..., description='The enrichment (e.g., name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    type: EnrichmentType = Field(EnrichmentType.Numerical, const=True)
    value: float = Field(..., title='Value')
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0',
        title='Confidence',
    )


class NumericalEnrichmentMeta(BaseModel):
    description: str = Field(
        ..., description='Description of the enrichment algorithm.', title='Description'
    )
    name: str = Field(
        ..., description='The enrichment name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: EnrichmentType = Field(EnrichmentType.Numerical, const=True)


class PlatformType(Enum):
    News = 'News'
    Reddit = 'Reddit'
    Twitter = 'Twitter'
    Youtube = 'Youtube'
    MEDIA_UNSPECIFIED = 'MEDIA_UNSPECIFIED'
    Webpage = 'Webpage'
    Blog = 'Blog'
    Comment = 'Comment'
    Facebook = 'Facebook'
    Forum = 'Forum'
    Google_Plus = 'Google Plus'
    LINE = 'LINE'
    Search_Result = 'Search Result'
    VK = 'VK'
    Bing = 'Bing'
    Wikipedia = 'Wikipedia'
    Other = 'Other'


class RawDataPostResponse(BaseModel):
    source_id_map: Dict[str, int] = Field(..., title='Source Id Map')
    item_id_map: Dict[str, int] = Field(..., title='Item Id Map')
    media_item_id_map: Dict[str, int] = Field(..., title='Media Item Id Map')


class RedditData(BaseModel):
    data_type: str = Field('Reddit', const=True, title='Data Type')


class RedditUserData(BaseModel):
    data_type: str = Field('Reddit', const=True, title='Data Type')


class Segment(BaseModel):
    id: Optional[int] = Field(None, title='Id')
    description: Optional[str] = Field(None, title='Description')
    name: str = Field(
        ...,
        description='The enrichment (e.g., Concern-Stance) name for the enrichment.',
        title='Name',
    )
    provider: str = Field(
        ...,
        description='The team (e.g., UIUC-DMG) who provides the enrichment.',
        title='Provider',
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: Optional[ClusterType] = 'Segment'


class TextEnrichment(BaseModel):
    name: str = Field(
        ..., description='The enrichment (e.g., name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    type: EnrichmentType = Field(EnrichmentType.Text, const=True)
    value: str = Field(..., title='Value')
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0',
        title='Confidence',
    )


class TextEnrichmentMeta(BaseModel):
    description: str = Field(
        ..., description='Description of the enrichment algorithm.', title='Description'
    )
    name: str = Field(
        ..., description='The enrichment name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: EnrichmentType = Field(EnrichmentType.Text, const=True)


class TwitterAnnotation(BaseModel):
    end: Optional[int] = Field(None, title='End')
    normalized_text: Optional[str] = Field(None, title='Normalized Text')
    probability: Optional[float] = Field(None, title='Probability')
    start: Optional[int] = Field(None, title='Start')
    type: Optional[str] = Field(None, title='Type')


class TwitterAttachment(BaseModel):
    media_keys: Optional[List[str]] = Field([], title='Media Keys')


class TwitterDomain(BaseModel):
    description: Optional[str] = Field(None, title='Description')
    id: Optional[str] = Field(None, title='Id')
    name: Optional[str] = Field(None, title='Name')


class TwitterEditControls(BaseModel):
    editable_until: Optional[str] = Field(None, title='Editable Until')
    edits_remaining: Optional[int] = Field(None, title='Edits Remaining')
    is_edit_eligible: Optional[bool] = Field(None, title='Is Edit Eligible')


class TwitterEntity(BaseModel):
    description: Optional[str] = Field(None, title='Description')
    id: Optional[str] = Field(None, title='Id')
    name: Optional[str] = Field(None, title='Name')


class TwitterHashtag(BaseModel):
    end: Optional[int] = Field(None, title='End')
    start: Optional[int] = Field(None, title='Start')
    tag: Optional[str] = Field(None, title='Tag')


class TwitterMention(BaseModel):
    end: Optional[int] = Field(None, title='End')
    id: Optional[str] = Field(None, title='Id')
    start: Optional[int] = Field(None, title='Start')
    username: Optional[str] = Field(None, title='Username')


class TwitterPublicMetrics(BaseModel):
    like_count: Optional[int] = Field(None, title='Like Count')
    quote_count: Optional[int] = Field(None, title='Quote Count')
    reply_count: Optional[int] = Field(None, title='Reply Count')
    retweet_count: Optional[int] = Field(None, title='Retweet Count')
    followers_count: Optional[int] = Field(None, title='Followers Count')
    following_count: Optional[int] = Field(None, title='Following Count')
    listed_count: Optional[int] = Field(None, title='Listed Count')
    tweet_count: Optional[int] = Field(None, title='Tweet Count')


class TwitterReferencedTweet(BaseModel):
    id: Optional[str] = Field(None, title='Id')
    type: Optional[str] = Field(None, title='Type')


class TwitterUserData(BaseModel):
    data_type: str = Field('Twitter', const=True, title='Data Type')
    description: Optional[str] = Field(None, title='Description')
    location: Optional[str] = Field(None, title='Location')
    pinned_tweet_id: Optional[str] = Field(None, title='Pinned Tweet Id')
    profile_image_url: Optional[str] = Field(None, title='Profile Image Url')
    protected: Optional[bool] = Field(None, title='Protected')
    public_metrics: Optional[TwitterPublicMetrics] = None
    username: Optional[str] = Field(None, title='Username')
    verified: Optional[bool] = Field(None, title='Verified')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class VisualTopic(BaseModel):
    id: Optional[int] = Field(None, title='Id')
    description: Optional[str] = Field(None, title='Description')
    name: str = Field(
        ...,
        description='The enrichment (e.g., Concern-Stance) name for the enrichment.',
        title='Name',
    )
    provider: str = Field(
        ...,
        description='The team (e.g., UIUC-DMG) who provides the enrichment.',
        title='Provider',
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: Optional[ClusterType] = 'VisualTopic'


class ArrayEnrichment(BaseModel):
    name: str = Field(
        ..., description='The enrichment (e.g., name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    type: EnrichmentType = Field(EnrichmentType.Array, const=True)
    value: List[float] = Field(..., title='Value')
    confidence: Optional[List[confloat(ge=0.0, le=1.0)]] = Field(
        None,
        description='The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0',
        title='Confidence',
    )


class ArrayEnrichmentMeta(BaseModel):
    description: str = Field(
        ..., description='Description of the enrichment algorithm.', title='Description'
    )
    name: str = Field(
        ..., description='The enrichment name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: EnrichmentType = Field(EnrichmentType.Array, const=True)
    label_map: Dict[str, int] = Field(
        ..., description='The mapping from label to index.', title='Label Map'
    )


class CategoryEnrichment(BaseModel):
    name: str = Field(
        ..., description='The enrichment (e.g., name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    type: EnrichmentType = Field(EnrichmentType.Category, const=True)
    value: str = Field(..., title='Value')
    confidence: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The confidence that this enrichment is correct, expressed as a percentage between 0.0 and 1.0',
        title='Confidence',
    )


class CategoryEnrichmentMeta(BaseModel):
    description: str = Field(
        ..., description='Description of the enrichment algorithm.', title='Description'
    )
    name: str = Field(
        ..., description='The enrichment name for the enrichment.', title='Name'
    )
    provider: str = Field(
        ..., description='The team who provides the enrichment.', title='Provider'
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: EnrichmentType = Field(EnrichmentType.Category, const=True)
    categories: List[str] = Field(
        ...,
        description='The list of categories for the enrichment.',
        title='Categories',
    )


class Claim(BaseModel):
    id: Optional[int] = Field(None, title='Id')
    description: Optional[str] = Field(None, title='Description')
    name: str = Field(
        ...,
        description='The enrichment (e.g., Concern-Stance) name for the enrichment.',
        title='Name',
    )
    provider: str = Field(
        ...,
        description='The team (e.g., UIUC-DMG) who provides the enrichment.',
        title='Provider',
    )
    tag: str = Field(
        ..., description='The tag within the same (provider, name).', title='Tag'
    )
    version: str = Field(
        ...,
        description='The version within the same (provider, name).',
        title='Version',
    )
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    type: Optional[ClusterType] = 'Claim'


class Cluster(BaseModel):
    __root__: Union[Segment, Claim, VisualTopic] = Field(
        ...,
        description='This is the unified interface for cluster output.',
        title='Cluster',
    )


class EnrichmentObj(BaseModel):
    __root__: Union[
        CategoryEnrichment,
        NumericalEnrichment,
        ArrayEnrichment,
        TextEnrichment,
        ListEnrichment,
        JsonEnrichment,
    ] = Field(
        ...,
        description='This is the unified interface for message enrichment output.',
        title='Enrichment',
    )


class EnrichmentMetaObj(BaseModel):
    __root__: Union[
        CategoryEnrichmentMeta,
        NumericalEnrichmentMeta,
        ArrayEnrichmentMeta,
        TextEnrichmentMeta,
        ListEnrichmentMeta,
        JsonEnrichmentMeta,
    ] = Field(
        ...,
        description='This is the unified interface for message enrichment algorithm meta information.',
        title='EnrichmentMeta',
    )

EnrichmentMeta = Union[
    CategoryEnrichmentMeta,
    NumericalEnrichmentMeta,
    ArrayEnrichmentMeta,
    TextEnrichmentMeta,
    ListEnrichmentMeta,
    JsonEnrichmentMeta,
]

Enrichment = Union[
    CategoryEnrichment,
    NumericalEnrichment,
    ArrayEnrichment,
    TextEnrichment,
    ListEnrichment,
    JsonEnrichment,
]

class Graph(BaseModel):
    id: Optional[int] = Field(None, title='Id')
    name: str = Field(..., title='Name')
    provider: str = Field(..., title='Provider')
    tag: str = Field(..., title='Tag')
    version: str = Field(..., title='Version')
    type: GraphType
    edges: Optional[List[Edge]] = Field([], title='Edges')
    data: Optional[Dict[str, Any]] = Field({}, title='Data')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class IncasAnnotation(BaseModel):
    attribute: Optional[str] = Field(None, title='Attribute')
    confidence: Optional[float] = Field(None, title='Confidence')
    id: Optional[str] = Field(None, title='Id')
    name: Optional[str] = Field(None, title='Name')
    offsets: Optional[List[IncasOffset]] = Field(None, title='Offsets')
    provider_name: Optional[str] = Field(None, title='Provider Name')
    text: Optional[str] = Field(None, title='Text')
    type: Optional[str] = Field(None, title='Type')


class IncasOneOfMediaTypeAttributes(BaseModel):
    reddit_data: Optional[IncasRedditData] = None
    twitter_data: Optional[IncasTwitterData] = None


class IncasSegment(BaseModel):
    annotations: Optional[List[IncasAnnotation]] = Field(None, title='Annotations')
    description: Optional[str] = Field(None, title='Description')
    extra_attributes: Optional[List[IncasExtraAttribute]] = Field(
        None, title='Extra Attributes'
    )
    id: Optional[str] = Field(None, title='Id')
    name: Optional[str] = Field(None, title='Name')
    provider_name: Optional[str] = Field(None, title='Provider Name')


class MediaItem(BaseModel):
    id: Optional[int] = Field(None, title='Id')
    type: MediaItemType
    content: str = Field(..., title='Content')


class TwitterContextAnnotation(BaseModel):
    domain: Optional[TwitterDomain] = None
    entity: Optional[TwitterEntity] = None


class TwitterEntities(BaseModel):
    annotations: Optional[List[TwitterAnnotation]] = Field([], title='Annotations')
    hashtags: Optional[List[TwitterHashtag]] = Field([], title='Hashtags')
    mentions: Optional[List[TwitterMention]] = Field([], title='Mentions')


class IncasActor(BaseModel):
    data_type: str = Field('Incas', const=True, title='Data Type')
    annotations: Optional[List[IncasAnnotation]] = Field([], title='Annotations')
    extra_attributes: Optional[List[IncasExtraAttribute]] = Field(
        [], title='Extra Attributes'
    )
    media_resources: Optional[List[IncasMediaResource]] = Field(
        [], title='Media Resources'
    )
    segments: Optional[List[IncasSegment]] = Field([], title='Segments')
    actor_name: Optional[str] = Field(None, title='Actor Name')
    description: Optional[str] = Field(None, title='Description')
    entity_type: Optional[EntityType] = None
    expose_actor_info: Optional[bool] = Field(None, title='Expose Actor Info')
    id: Optional[str] = Field(None, title='Id')
    knowledge_base_url: Optional[str] = Field(None, title='Knowledge Base Url')
    links: Optional[IncasLinks] = None
    name: Optional[str] = Field(None, title='Name')


class IncasMessage(BaseModel):
    data_type: str = Field('Incas', const=True, title='Data Type')
    annotations: Optional[List[IncasAnnotation]] = Field([], title='Annotations')
    data_tags: Optional[List[str]] = Field([], title='Data Tags')
    embedded_urls: Optional[List[str]] = Field([], title='Embedded Urls')
    extra_attributes: Optional[List[IncasExtraAttribute]] = Field(
        [], title='Extra Attributes'
    )
    image_urls: Optional[List[str]] = Field([], title='Image Urls')
    segments: Optional[List[IncasSegment]] = Field([], title='Segments')
    author: Optional[str] = Field(None, title='Author')
    content_text: Optional[str] = Field(None, title='Content Text')
    geolocation: Optional[GeoLocation] = None
    id: Optional[str] = Field(None, title='Id')
    language: Optional[str] = Field(None, title='Language')
    media_type: Optional[PlatformType] = None
    media_type_attributes: Optional[IncasOneOfMediaTypeAttributes] = None
    mentioned_users: Optional[List] = Field(None, title='Mentioned Users')
    name: Optional[str] = Field(None, title='Name')
    time_published: Optional[int] = Field(None, title='Time Published')
    title: Optional[str] = Field(None, title='Title')
    url: Optional[str] = Field(None, title='Url')
    translated_content_text: Optional[str] = Field(
        None, title='Translated Content Text'
    )
    translated_title: Optional[str] = Field(None, title='Translated Title')


# class SourceData(BaseModel):
#     __root__: Union[TwitterUserData, RedditUserData, IncasActor] = Field(
#         ..., title='SourceData'
#     )

SourceData = Union[TwitterUserData, RedditUserData, IncasActor]


class TwitterData(BaseModel):
    data_type: str = Field('Twitter', const=True, title='Data Type')
    attachments: Optional[TwitterAttachment] = None
    context_annotations: Optional[List[TwitterContextAnnotation]] = Field(
        [], title='Context Annotations'
    )
    author_id: Optional[str] = Field(None, title='Author Id')
    conversation_id: Optional[str] = Field(None, title='Conversation Id')
    created_at: Optional[str] = Field(None, title='Created At')
    edit_controls: Optional[TwitterEditControls] = None
    edit_history_tweet_ids: Optional[List[str]] = Field(
        [], title='Edit History Tweet Ids'
    )
    entities: Optional[TwitterEntities] = None
    id: Optional[str] = Field(None, title='Id')
    lang: Optional[str] = Field(None, title='Lang')
    possibly_sensitive: Optional[bool] = Field(None, title='Possibly Sensitive')
    public_metrics: Optional[TwitterPublicMetrics] = None
    reference_tweets: Optional[List[TwitterReferencedTweet]] = Field(
        [], title='Reference Tweets'
    )
    reply_settings: Optional[str] = Field(None, title='Reply Settings')
    tweet_id: Optional[str] = Field(None, title='Tweet Id')
    twitter_author_screenname: Optional[str] = Field(
        None, title='Twitter Author Screenname'
    )
    twitter_user_id: Optional[str] = Field(None, title='Twitter User Id')


# class ItemData(BaseModel):
#     __root__: Union[TwitterData, RedditData, IncasMessage] = Field(
#         ..., title='ItemData'
#     )

ItemData = Union[TwitterData, RedditData, IncasMessage]


class Source(BaseModel):
    id: str = Field(..., title='Id')
    type: str = Field(..., title='Type')
    platform: PlatformType
    sid: Optional[int] = Field(None, title='Sid')
    enrichments: Optional[List[Enrichment]] = Field([], title='Enrichments')
    clusters: Optional[List[ClusterMember]] = Field([], title='Clusters')
    name: Optional[str] = Field(None, title='Name')
    data: SourceData


class Item(BaseModel):
    id: str = Field(..., title='Id')
    author: str = Field(..., title='Author')
    platform: PlatformType
    time_published: int = Field(..., title='Time Published')
    sid: Optional[int] = Field(None, title='Sid')
    source_id: Optional[int] = Field(None, title='Source Id')
    enrichments: Optional[List[Enrichment]] = Field([], title='Enrichments')
    clusters: Optional[List[ClusterMember]] = Field([], title='Clusters')
    media_items: Optional[List[MediaItem]] = Field([], title='Media Items')
    text: Optional[str] = Field(None, title='Text')
    data: ItemData


class RawDataPostEntry(BaseModel):
    source: Source
    items: List[Item] = Field(..., title='Items')


class RawDataPostRequest(BaseModel):
    override: Optional[bool] = Field(False, title='Override')
    data: List[RawDataPostEntry] = Field(..., title='Data')

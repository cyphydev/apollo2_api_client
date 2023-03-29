# mips-api-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import mips_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mips_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mips_api_client
from mips_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = mips_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = mips_api_client.AdminApi(mips_api_client.ApiClient(configuration))
body = mips_api_client.RawDataPostRequest() # RawDataPostRequest | 

try:
    # Admin Data Post
    api_response = api_instance.admin_data_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_data_post: %s\n" % e)

# Configure API key authorization: APIKeyHeader
configuration = mips_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = mips_api_client.AdminApi(mips_api_client.ApiClient(configuration))

try:
    # Admin Flush
    api_response = api_instance.admin_flush()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_flush: %s\n" % e)

# Configure API key authorization: APIKeyHeader
configuration = mips_api_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = mips_api_client.AdminApi(mips_api_client.ApiClient(configuration))

try:
    # Status Get
    api_response = api_instance.status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->status_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**admin_data_post**](docs/AdminApi.md#admin_data_post) | **POST** /data | Admin Data Post
*AdminApi* | [**admin_flush**](docs/AdminApi.md#admin_flush) | **DELETE** /dbflush | Admin Flush
*AdminApi* | [**status_get**](docs/AdminApi.md#status_get) | **GET** /status | Status Get
*ClusterApi* | [**cluster_delete**](docs/ClusterApi.md#cluster_delete) | **DELETE** /cluster | Cluster Delete
*ClusterApi* | [**cluster_get**](docs/ClusterApi.md#cluster_get) | **GET** /cluster | Cluster Get
*ClusterApi* | [**cluster_id_delete**](docs/ClusterApi.md#cluster_id_delete) | **DELETE** /cluster/{id} | Cluster Id Delete
*ClusterApi* | [**cluster_id_delete_members_post**](docs/ClusterApi.md#cluster_id_delete_members_post) | **POST** /cluster/{id}/delete_members | Cluster Id Delete Members Post
*ClusterApi* | [**cluster_id_edit_members_post**](docs/ClusterApi.md#cluster_id_edit_members_post) | **POST** /cluster/{id}/edit_members | Cluster Id Edit Members Post
*ClusterApi* | [**cluster_id_get**](docs/ClusterApi.md#cluster_id_get) | **GET** /cluster/{id} | Cluster Id Get
*ClusterApi* | [**cluster_id_members_get**](docs/ClusterApi.md#cluster_id_members_get) | **GET** /cluster/{id}/members | Cluster Id Members Get
*ClusterApi* | [**cluster_post**](docs/ClusterApi.md#cluster_post) | **POST** /cluster | Cluster Post
*DefaultApi* | [**ping_get**](docs/DefaultApi.md#ping_get) | **GET** /ping | Ping Get
*EnrichmentApi* | [**enrichments_meta_delete**](docs/EnrichmentApi.md#enrichments_meta_delete) | **DELETE** /enrichments/meta | Enrichments Meta Delete
*EnrichmentApi* | [**enrichments_meta_get**](docs/EnrichmentApi.md#enrichments_meta_get) | **GET** /enrichments/meta | Enrichments Meta Get
*EnrichmentApi* | [**enrichments_meta_post**](docs/EnrichmentApi.md#enrichments_meta_post) | **POST** /enrichments/meta | Enrichments Meta Post
*GraphApi* | [**graph_get**](docs/GraphApi.md#graph_get) | **GET** /graph | Graph Get
*GraphApi* | [**graph_id_delete**](docs/GraphApi.md#graph_id_delete) | **DELETE** /graph/{id} | Graph Id Delete
*GraphApi* | [**graph_id_delete_edges_post**](docs/GraphApi.md#graph_id_delete_edges_post) | **POST** /graph/{id}/delete_edges | Graph Id Delete Edges Post
*GraphApi* | [**graph_id_edges_get**](docs/GraphApi.md#graph_id_edges_get) | **GET** /graph/{id}/edges | Graph Id Edges Get
*GraphApi* | [**graph_id_edit_edges_post**](docs/GraphApi.md#graph_id_edit_edges_post) | **POST** /graph/{id}/edit_edges | Graph Id Edit Edges Post
*GraphApi* | [**graph_id_get**](docs/GraphApi.md#graph_id_get) | **GET** /graph/{id} | Graph Id Get
*GraphApi* | [**graph_post**](docs/GraphApi.md#graph_post) | **POST** /graph | Graph Post
*ItemApi* | [**item_attach_media_post**](docs/ItemApi.md#item_attach_media_post) | **POST** /item/attach_media | Item Attach Media Post
*ItemApi* | [**item_batch_get**](docs/ItemApi.md#item_batch_get) | **POST** /item/get | Item Batch Get
*ItemApi* | [**item_count_get**](docs/ItemApi.md#item_count_get) | **GET** /item/count | Item Count Get
*ItemApi* | [**item_detach_media_post**](docs/ItemApi.md#item_detach_media_post) | **POST** /item/detach_media | Item Detach Media Post
*ItemApi* | [**item_enrichments_batch_delete**](docs/ItemApi.md#item_enrichments_batch_delete) | **POST** /item/enrichments/delete | Item Enrichments Batch Delete
*ItemApi* | [**item_enrichments_batch_get**](docs/ItemApi.md#item_enrichments_batch_get) | **POST** /item/enrichments/get | Item Enrichments Batch Get
*ItemApi* | [**item_enrichments_batch_post**](docs/ItemApi.md#item_enrichments_batch_post) | **POST** /item/enrichments/submit | Item Enrichments Batch Post
*ItemApi* | [**item_get**](docs/ItemApi.md#item_get) | **GET** /item | Item Get
*ItemApi* | [**item_id_delete**](docs/ItemApi.md#item_id_delete) | **DELETE** /item/{id} | Item Id Delete
*ItemApi* | [**item_id_enrichments_delete**](docs/ItemApi.md#item_id_enrichments_delete) | **DELETE** /item/{id}/enrichments | Item Id Enrichments Delete
*ItemApi* | [**item_id_enrichments_get**](docs/ItemApi.md#item_id_enrichments_get) | **GET** /item/{id}/enrichments | Item Id Enrichments Get
*ItemApi* | [**item_id_enrichments_post**](docs/ItemApi.md#item_id_enrichments_post) | **POST** /item/{id}/enrichments | Item Id Enrichments Post
*ItemApi* | [**item_id_forward_batch_translate**](docs/ItemApi.md#item_id_forward_batch_translate) | **POST** /item/id/forward | Item Id Forward Batch Translate
*ItemApi* | [**item_id_forward_translate**](docs/ItemApi.md#item_id_forward_translate) | **GET** /item/id/forward/{id} | Item Id Forward Translate
*ItemApi* | [**item_id_get**](docs/ItemApi.md#item_id_get) | **GET** /item/{id} | Item Id Get
*ItemApi* | [**item_id_reverse_batch_translate**](docs/ItemApi.md#item_id_reverse_batch_translate) | **POST** /item/id/reverse | Item Id Reverse Batch Translate
*ItemApi* | [**item_id_reverse_translate**](docs/ItemApi.md#item_id_reverse_translate) | **GET** /item/id/reverse/{id} | Item Id Reverse Translate
*ItemApi* | [**item_max_id_get**](docs/ItemApi.md#item_max_id_get) | **GET** /item/max_id | Item Max Id Get
*MediaItemApi* | [**media_item_batch_get**](docs/MediaItemApi.md#media_item_batch_get) | **POST** /media_item/get | Media Item Batch Get
*MediaItemApi* | [**media_item_count_get**](docs/MediaItemApi.md#media_item_count_get) | **GET** /media_item/count | Media Item Count Get
*MediaItemApi* | [**media_item_get**](docs/MediaItemApi.md#media_item_get) | **GET** /media_item | Media Item Get
*MediaItemApi* | [**media_item_id_delete**](docs/MediaItemApi.md#media_item_id_delete) | **DELETE** /media_item/{id} | Media Item Id Delete
*MediaItemApi* | [**media_item_id_get**](docs/MediaItemApi.md#media_item_id_get) | **GET** /media_item/{id} | Media Item Id Get
*MediaItemApi* | [**media_item_max_id_get**](docs/MediaItemApi.md#media_item_max_id_get) | **GET** /media_item/max_id | Media Item Max Id Get
*SourceApi* | [**source_batch_get**](docs/SourceApi.md#source_batch_get) | **POST** /source/get | Source Batch Get
*SourceApi* | [**source_count_get**](docs/SourceApi.md#source_count_get) | **GET** /source/count | Source Count Get
*SourceApi* | [**source_enrichments_batch_delete**](docs/SourceApi.md#source_enrichments_batch_delete) | **POST** /source/enrichments/delete | Source Enrichments Batch Delete
*SourceApi* | [**source_enrichments_batch_get**](docs/SourceApi.md#source_enrichments_batch_get) | **POST** /source/enrichments/get | Source Enrichments Batch Get
*SourceApi* | [**source_enrichments_batch_post**](docs/SourceApi.md#source_enrichments_batch_post) | **POST** /source/enrichments/submit | Source Enrichments Batch Post
*SourceApi* | [**source_get**](docs/SourceApi.md#source_get) | **GET** /source | Source Get
*SourceApi* | [**source_id_delete**](docs/SourceApi.md#source_id_delete) | **DELETE** /source/{id} | Source Id Delete
*SourceApi* | [**source_id_enrichments_delete**](docs/SourceApi.md#source_id_enrichments_delete) | **DELETE** /source/{id}/enrichments | Source Id Enrichments Delete
*SourceApi* | [**source_id_enrichments_get**](docs/SourceApi.md#source_id_enrichments_get) | **GET** /source/{id}/enrichments | Source Id Enrichments Get
*SourceApi* | [**source_id_enrichments_post**](docs/SourceApi.md#source_id_enrichments_post) | **POST** /source/{id}/enrichments | Source Id Enrichments Post
*SourceApi* | [**source_id_forward_batch_translate**](docs/SourceApi.md#source_id_forward_batch_translate) | **POST** /source/id/forward | Source Id Forward Batch Translate
*SourceApi* | [**source_id_forward_translate**](docs/SourceApi.md#source_id_forward_translate) | **GET** /source/id/forward/{id} | Source Id Forward Translate
*SourceApi* | [**source_id_get**](docs/SourceApi.md#source_id_get) | **GET** /source/{id} | Source Id Get
*SourceApi* | [**source_id_reverse_batch_translate**](docs/SourceApi.md#source_id_reverse_batch_translate) | **POST** /source/id/reverse | Source Id Reverse Batch Translate
*SourceApi* | [**source_id_reverse_translate**](docs/SourceApi.md#source_id_reverse_translate) | **GET** /source/id/reverse/{id} | Source Id Reverse Translate
*SourceApi* | [**source_max_id_get**](docs/SourceApi.md#source_max_id_get) | **GET** /source/max_id | Source Max Id Get

## Documentation For Models

 - [Annotation](docs/Annotation.md)
 - [AnyOfCluster](docs/AnyOfCluster.md)
 - [AnyOfEnrichment](docs/AnyOfEnrichment.md)
 - [AnyOfEnrichmentMeta](docs/AnyOfEnrichmentMeta.md)
 - [AnyOfItemData](docs/AnyOfItemData.md)
 - [AnyOfListEnrichmentValueItems](docs/AnyOfListEnrichmentValueItems.md)
 - [AnyOfSourceData](docs/AnyOfSourceData.md)
 - [AnyOfValidationErrorLocItems](docs/AnyOfValidationErrorLocItems.md)
 - [ArrayEnrichment](docs/ArrayEnrichment.md)
 - [ArrayEnrichmentMeta](docs/ArrayEnrichmentMeta.md)
 - [Attachment](docs/Attachment.md)
 - [BatchGetRequest](docs/BatchGetRequest.md)
 - [BatchMediaGetRequest](docs/BatchMediaGetRequest.md)
 - [CategoryEnrichment](docs/CategoryEnrichment.md)
 - [CategoryEnrichmentMeta](docs/CategoryEnrichmentMeta.md)
 - [Claim](docs/Claim.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterMember](docs/ClusterMember.md)
 - [ClusterType](docs/ClusterType.md)
 - [ContextAnnotation](docs/ContextAnnotation.md)
 - [Domain](docs/Domain.md)
 - [Edge](docs/Edge.md)
 - [EditControls](docs/EditControls.md)
 - [Enrichment](docs/Enrichment.md)
 - [EnrichmentMeta](docs/EnrichmentMeta.md)
 - [EnrichmentType](docs/EnrichmentType.md)
 - [EnrichmentsBatchRequest](docs/EnrichmentsBatchRequest.md)
 - [Entities](docs/Entities.md)
 - [Entity](docs/Entity.md)
 - [Graph](docs/Graph.md)
 - [GraphType](docs/GraphType.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Hashtag](docs/Hashtag.md)
 - [Item](docs/Item.md)
 - [ListEnrichment](docs/ListEnrichment.md)
 - [ListEnrichmentMeta](docs/ListEnrichmentMeta.md)
 - [MediaItem](docs/MediaItem.md)
 - [MediaItemType](docs/MediaItemType.md)
 - [MediaType](docs/MediaType.md)
 - [Mention](docs/Mention.md)
 - [ModifyMediaAttachmentRequest](docs/ModifyMediaAttachmentRequest.md)
 - [NumericalEnrichment](docs/NumericalEnrichment.md)
 - [NumericalEnrichmentMeta](docs/NumericalEnrichmentMeta.md)
 - [PublicMetrics](docs/PublicMetrics.md)
 - [RawDataPostEntry](docs/RawDataPostEntry.md)
 - [RawDataPostRequest](docs/RawDataPostRequest.md)
 - [RawDataPostResponse](docs/RawDataPostResponse.md)
 - [RedditData](docs/RedditData.md)
 - [RedditUserData](docs/RedditUserData.md)
 - [ReferencedTweet](docs/ReferencedTweet.md)
 - [Segment](docs/Segment.md)
 - [Source](docs/Source.md)
 - [TextEnrichment](docs/TextEnrichment.md)
 - [TextEnrichmentMeta](docs/TextEnrichmentMeta.md)
 - [TwitterData](docs/TwitterData.md)
 - [TwitterUserData](docs/TwitterUserData.md)
 - [ValidationError](docs/ValidationError.md)
 - [VisualTopic](docs/VisualTopic.md)

## Documentation For Authorization


## APIKeyHeader

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author



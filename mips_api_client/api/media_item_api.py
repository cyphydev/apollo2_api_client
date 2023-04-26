# coding: utf-8

"""
    Mips UIUC Datatypes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mips_api_client.api_client import ApiClient


class MediaItemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def media_item_batch_get(self, body, **kwargs):  # noqa: E501
        """Media Item Batch Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_batch_get(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchMediaGetRequest body: (required)
        :param str identifier:
        :return: list[MediaItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_batch_get_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.media_item_batch_get_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def media_item_batch_get_with_http_info(self, body, **kwargs):  # noqa: E501
        """Media Item Batch Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_batch_get_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchMediaGetRequest body: (required)
        :param str identifier:
        :return: list[MediaItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_batch_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `media_item_batch_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MediaItem]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_count_get(self, **kwargs):  # noqa: E501
        """Media Item Count Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_count_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int last:
        :param int end:
        :param str identifier:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_count_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.media_item_count_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def media_item_count_get_with_http_info(self, **kwargs):  # noqa: E501
        """Media Item Count Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_count_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int last:
        :param int end:
        :param str identifier:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['last', 'end', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_count_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'last' in params:
            query_params.append(('last', params['last']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_get(self, limit, **kwargs):  # noqa: E501
        """Media Item Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_get(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: (required)
        :param int last:
        :param int end:
        :param str identifier:
        :return: list[MediaItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_get_with_http_info(limit, **kwargs)  # noqa: E501
        else:
            (data) = self.media_item_get_with_http_info(limit, **kwargs)  # noqa: E501
            return data

    def media_item_get_with_http_info(self, limit, **kwargs):  # noqa: E501
        """Media Item Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_get_with_http_info(limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: (required)
        :param int last:
        :param int end:
        :param str identifier:
        :return: list[MediaItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'last', 'end', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `media_item_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'last' in params:
            query_params.append(('last', params['last']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MediaItem]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_id_delete(self, id, **kwargs):  # noqa: E501
        """Media Item Id Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.media_item_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def media_item_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Media Item Id Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `media_item_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_id_get(self, id, **kwargs):  # noqa: E501
        """Media Item Id Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: MediaItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.media_item_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def media_item_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Media Item Id Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: MediaItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `media_item_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MediaItem',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_id_identifer_get(self, id, **kwargs):  # noqa: E501
        """Media Item Id Identifer Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_id_identifer_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_id_identifer_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.media_item_id_identifer_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def media_item_id_identifer_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Media Item Id Identifer Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_id_identifer_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_id_identifer_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `media_item_id_identifer_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/{id}/identifer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_identifer_delete(self, body, identifier, **kwargs):  # noqa: E501
        """Media Item Identifer Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_identifer_delete(body, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body: (required)
        :param str identifier: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_identifer_delete_with_http_info(body, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.media_item_identifer_delete_with_http_info(body, identifier, **kwargs)  # noqa: E501
            return data

    def media_item_identifer_delete_with_http_info(self, body, identifier, **kwargs):  # noqa: E501
        """Media Item Identifer Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_identifer_delete_with_http_info(body, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body: (required)
        :param str identifier: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_identifer_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `media_item_identifer_delete`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `media_item_identifer_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/identifer/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_identifer_post(self, body, identifier, **kwargs):  # noqa: E501
        """Media Item Identifer Post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_identifer_post(body, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body: (required)
        :param str identifier: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_identifer_post_with_http_info(body, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.media_item_identifer_post_with_http_info(body, identifier, **kwargs)  # noqa: E501
            return data

    def media_item_identifer_post_with_http_info(self, body, identifier, **kwargs):  # noqa: E501
        """Media Item Identifer Post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_identifer_post_with_http_info(body, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body: (required)
        :param str identifier: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_identifer_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `media_item_identifer_post`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `media_item_identifer_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/identifer/post', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def media_item_max_id_get(self, **kwargs):  # noqa: E501
        """Media Item Max Id Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_max_id_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.media_item_max_id_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.media_item_max_id_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def media_item_max_id_get_with_http_info(self, **kwargs):  # noqa: E501
        """Media Item Max Id Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.media_item_max_id_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method media_item_max_id_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/media_item/max_id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

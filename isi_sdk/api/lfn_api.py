# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 22
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk.api_client import ApiClient


class LfnApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_lfn_item(self, lfn_item, **kwargs):  # noqa: E501
        """create_lfn_item  # noqa: E501

        Create a new file name length configuration domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_lfn_item(lfn_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LfnItem lfn_item: (required)
        :return: LfnDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_lfn_item_with_http_info(lfn_item, **kwargs)  # noqa: E501
        else:
            (data) = self.create_lfn_item_with_http_info(lfn_item, **kwargs)  # noqa: E501
            return data

    def create_lfn_item_with_http_info(self, lfn_item, **kwargs):  # noqa: E501
        """create_lfn_item  # noqa: E501

        Create a new file name length configuration domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_lfn_item_with_http_info(lfn_item, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LfnItem lfn_item: (required)
        :return: LfnDomain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lfn_item']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_lfn_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lfn_item' is set
        if ('lfn_item' not in params or
                params['lfn_item'] is None):
            raise ValueError("Missing the required parameter `lfn_item` when calling `create_lfn_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lfn_item' in params:
            body_params = params['lfn_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/12/lfn', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LfnDomain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_lfn(self, **kwargs):  # noqa: E501
        """delete_lfn  # noqa: E501

        Delete all file name length configuration domains, returning to legacy limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_lfn(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_lfn_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_lfn_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_lfn_with_http_info(self, **kwargs):  # noqa: E501
        """delete_lfn  # noqa: E501

        Delete all file name length configuration domains, returning to legacy limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_lfn_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_lfn" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/12/lfn', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_lfn_path(self, lfn_path, **kwargs):  # noqa: E501
        """delete_lfn_path  # noqa: E501

        Delete the file name length configuration domain that originates at the specified path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_lfn_path(lfn_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lfn_path: Delete the file name length configuration domain that originates at the specified path. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_lfn_path_with_http_info(lfn_path, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_lfn_path_with_http_info(lfn_path, **kwargs)  # noqa: E501
            return data

    def delete_lfn_path_with_http_info(self, lfn_path, **kwargs):  # noqa: E501
        """delete_lfn_path  # noqa: E501

        Delete the file name length configuration domain that originates at the specified path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_lfn_path_with_http_info(lfn_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lfn_path: Delete the file name length configuration domain that originates at the specified path. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lfn_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_lfn_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lfn_path' is set
        if ('lfn_path' not in params or
                params['lfn_path'] is None):
            raise ValueError("Missing the required parameter `lfn_path` when calling `delete_lfn_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lfn_path' in params:
            path_params['LfnPath'] = params['lfn_path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/12/lfn/{LfnPath}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_lfn_path(self, lfn_path, **kwargs):  # noqa: E501
        """get_lfn_path  # noqa: E501

        Retrieve file name length configuration information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lfn_path(lfn_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lfn_path: Retrieve file name length configuration information. (required)
        :return: Lfn
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_lfn_path_with_http_info(lfn_path, **kwargs)  # noqa: E501
        else:
            (data) = self.get_lfn_path_with_http_info(lfn_path, **kwargs)  # noqa: E501
            return data

    def get_lfn_path_with_http_info(self, lfn_path, **kwargs):  # noqa: E501
        """get_lfn_path  # noqa: E501

        Retrieve file name length configuration information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lfn_path_with_http_info(lfn_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lfn_path: Retrieve file name length configuration information. (required)
        :return: Lfn
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lfn_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lfn_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lfn_path' is set
        if ('lfn_path' not in params or
                params['lfn_path'] is None):
            raise ValueError("Missing the required parameter `lfn_path` when calling `get_lfn_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lfn_path' in params:
            path_params['LfnPath'] = params['lfn_path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/12/lfn/{LfnPath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Lfn',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_lfn(self, **kwargs):  # noqa: E501
        """list_lfn  # noqa: E501

        List all file name length configuration domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_lfn(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: LfnExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_lfn_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_lfn_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_lfn_with_http_info(self, **kwargs):  # noqa: E501
        """list_lfn  # noqa: E501

        List all file name length configuration domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_lfn_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dir: The direction of the sort.
        :param int limit: Return no more than this many results at once (see resume).
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :param str sort: The field that will be used for sorting.
        :return: LfnExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dir', 'limit', 'resume', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_lfn" % key
                )
            params[key] = val
        del params['kwargs']

        if ('dir' in params and
                len(params['dir']) < 0):
            raise ValueError("Invalid value for parameter `dir` when calling `list_lfn`, length must be greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_lfn`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_lfn`, must be a value greater than or equal to `1`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) > 8192):
            raise ValueError("Invalid value for parameter `resume` when calling `list_lfn`, length must be less than or equal to `8192`")  # noqa: E501
        if ('resume' in params and
                len(params['resume']) < 0):
            raise ValueError("Invalid value for parameter `resume` when calling `list_lfn`, length must be greater than or equal to `0`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) > 255):
            raise ValueError("Invalid value for parameter `sort` when calling `list_lfn`, length must be less than or equal to `255`")  # noqa: E501
        if ('sort' in params and
                len(params['sort']) < 0):
            raise ValueError("Invalid value for parameter `sort` when calling `list_lfn`, length must be greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dir' in params:
            query_params.append(('dir', params['dir']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/12/lfn', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LfnExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_lfn_path(self, lfn_path_params, lfn_path, **kwargs):  # noqa: E501
        """update_lfn_path  # noqa: E501

        Modify file name length settings if specified path is the root of the configuration. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_lfn_path(lfn_path_params, lfn_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LfnPathParams lfn_path_params: (required)
        :param str lfn_path: Modify file name length settings if specified path is the root of the configuration. All input fields are optional, but one or more must be supplied. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_lfn_path_with_http_info(lfn_path_params, lfn_path, **kwargs)  # noqa: E501
        else:
            (data) = self.update_lfn_path_with_http_info(lfn_path_params, lfn_path, **kwargs)  # noqa: E501
            return data

    def update_lfn_path_with_http_info(self, lfn_path_params, lfn_path, **kwargs):  # noqa: E501
        """update_lfn_path  # noqa: E501

        Modify file name length settings if specified path is the root of the configuration. All input fields are optional, but one or more must be supplied.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_lfn_path_with_http_info(lfn_path_params, lfn_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LfnPathParams lfn_path_params: (required)
        :param str lfn_path: Modify file name length settings if specified path is the root of the configuration. All input fields are optional, but one or more must be supplied. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lfn_path_params', 'lfn_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_lfn_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lfn_path_params' is set
        if ('lfn_path_params' not in params or
                params['lfn_path_params'] is None):
            raise ValueError("Missing the required parameter `lfn_path_params` when calling `update_lfn_path`")  # noqa: E501
        # verify the required parameter 'lfn_path' is set
        if ('lfn_path' not in params or
                params['lfn_path'] is None):
            raise ValueError("Missing the required parameter `lfn_path` when calling `update_lfn_path`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lfn_path' in params:
            path_params['LfnPath'] = params['lfn_path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'lfn_path_params' in params:
            body_params = params['lfn_path_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/12/lfn/{LfnPath}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

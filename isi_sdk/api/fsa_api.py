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


class FsaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_fsa_result(self, fsa_result_id, **kwargs):  # noqa: E501
        """delete_fsa_result  # noqa: E501

        Delete the result set.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fsa_result(fsa_result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fsa_result_id: Delete the result set. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_fsa_result_with_http_info(fsa_result_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_fsa_result_with_http_info(fsa_result_id, **kwargs)  # noqa: E501
            return data

    def delete_fsa_result_with_http_info(self, fsa_result_id, **kwargs):  # noqa: E501
        """delete_fsa_result  # noqa: E501

        Delete the result set.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fsa_result_with_http_info(fsa_result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fsa_result_id: Delete the result set. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fsa_result_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fsa_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fsa_result_id' is set
        if ('fsa_result_id' not in params or
                params['fsa_result_id'] is None):
            raise ValueError("Missing the required parameter `fsa_result_id` when calling `delete_fsa_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fsa_result_id' in params:
            path_params['FsaResultId'] = params['fsa_result_id']  # noqa: E501

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
            '/platform/3/fsa/results/{FsaResultId}', 'DELETE',
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

    def delete_fsa_settings(self, **kwargs):  # noqa: E501
        """delete_fsa_settings  # noqa: E501

        Revert all settings to their defaults.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fsa_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_fsa_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_fsa_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_fsa_settings_with_http_info(self, **kwargs):  # noqa: E501
        """delete_fsa_settings  # noqa: E501

        Revert all settings to their defaults.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fsa_settings_with_http_info(async_req=True)
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
                    " to method delete_fsa_settings" % key
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
            '/platform/1/fsa/settings', 'DELETE',
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

    def get_fsa_index(self, **kwargs):  # noqa: E501
        """get_fsa_index  # noqa: E501

        Retrieve all the FSA index table names available on an PowerScale cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_index(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FsaIndex
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fsa_index_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fsa_index_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fsa_index_with_http_info(self, **kwargs):  # noqa: E501
        """get_fsa_index  # noqa: E501

        Retrieve all the FSA index table names available on an PowerScale cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_index_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FsaIndex
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
                    " to method get_fsa_index" % key
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
            '/platform/8/fsa/index', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FsaIndex',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fsa_result(self, fsa_result_id, **kwargs):  # noqa: E501
        """get_fsa_result  # noqa: E501

        Retrieve result set information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_result(fsa_result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fsa_result_id: Retrieve result set information. (required)
        :return: FsaResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fsa_result_with_http_info(fsa_result_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fsa_result_with_http_info(fsa_result_id, **kwargs)  # noqa: E501
            return data

    def get_fsa_result_with_http_info(self, fsa_result_id, **kwargs):  # noqa: E501
        """get_fsa_result  # noqa: E501

        Retrieve result set information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_result_with_http_info(fsa_result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fsa_result_id: Retrieve result set information. (required)
        :return: FsaResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fsa_result_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fsa_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fsa_result_id' is set
        if ('fsa_result_id' not in params or
                params['fsa_result_id'] is None):
            raise ValueError("Missing the required parameter `fsa_result_id` when calling `get_fsa_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fsa_result_id' in params:
            path_params['FsaResultId'] = params['fsa_result_id']  # noqa: E501

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
            '/platform/3/fsa/results/{FsaResultId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FsaResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fsa_results(self, **kwargs):  # noqa: E501
        """get_fsa_results  # noqa: E501

        List all results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_results(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FsaResultsExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fsa_results_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fsa_results_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fsa_results_with_http_info(self, **kwargs):  # noqa: E501
        """get_fsa_results  # noqa: E501

        List all results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_results_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FsaResultsExtended
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
                    " to method get_fsa_results" % key
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
            '/platform/3/fsa/results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FsaResultsExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fsa_settings(self, **kwargs):  # noqa: E501
        """get_fsa_settings  # noqa: E501

        List all settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: If specified as effective or not specified, all fields are returned.  If specified as user, only fields with non-default values are shown.  If specified as default, the original values are returned.
        :return: FsaSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fsa_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fsa_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fsa_settings_with_http_info(self, **kwargs):  # noqa: E501
        """get_fsa_settings  # noqa: E501

        List all settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fsa_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scope: If specified as effective or not specified, all fields are returned.  If specified as user, only fields with non-default values are shown.  If specified as default, the original values are returned.
        :return: FsaSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fsa_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501

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
            '/platform/1/fsa/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FsaSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_fsa_result(self, fsa_result, fsa_result_id, **kwargs):  # noqa: E501
        """update_fsa_result  # noqa: E501

        Modify result set. Only the pinned property can be changed at this time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fsa_result(fsa_result, fsa_result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FsaResult fsa_result: (required)
        :param str fsa_result_id: Modify result set. Only the pinned property can be changed at this time. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_fsa_result_with_http_info(fsa_result, fsa_result_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_fsa_result_with_http_info(fsa_result, fsa_result_id, **kwargs)  # noqa: E501
            return data

    def update_fsa_result_with_http_info(self, fsa_result, fsa_result_id, **kwargs):  # noqa: E501
        """update_fsa_result  # noqa: E501

        Modify result set. Only the pinned property can be changed at this time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fsa_result_with_http_info(fsa_result, fsa_result_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FsaResult fsa_result: (required)
        :param str fsa_result_id: Modify result set. Only the pinned property can be changed at this time. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fsa_result', 'fsa_result_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_fsa_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fsa_result' is set
        if ('fsa_result' not in params or
                params['fsa_result'] is None):
            raise ValueError("Missing the required parameter `fsa_result` when calling `update_fsa_result`")  # noqa: E501
        # verify the required parameter 'fsa_result_id' is set
        if ('fsa_result_id' not in params or
                params['fsa_result_id'] is None):
            raise ValueError("Missing the required parameter `fsa_result_id` when calling `update_fsa_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fsa_result_id' in params:
            path_params['FsaResultId'] = params['fsa_result_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'fsa_result' in params:
            body_params = params['fsa_result']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/fsa/results/{FsaResultId}', 'PUT',
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

    def update_fsa_settings(self, fsa_settings, **kwargs):  # noqa: E501
        """update_fsa_settings  # noqa: E501

        Modify one or more settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fsa_settings(fsa_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FsaSettingsSettings fsa_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_fsa_settings_with_http_info(fsa_settings, **kwargs)  # noqa: E501
        else:
            (data) = self.update_fsa_settings_with_http_info(fsa_settings, **kwargs)  # noqa: E501
            return data

    def update_fsa_settings_with_http_info(self, fsa_settings, **kwargs):  # noqa: E501
        """update_fsa_settings  # noqa: E501

        Modify one or more settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fsa_settings_with_http_info(fsa_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FsaSettingsSettings fsa_settings: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fsa_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_fsa_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fsa_settings' is set
        if ('fsa_settings' not in params or
                params['fsa_settings'] is None):
            raise ValueError("Missing the required parameter `fsa_settings` when calling `update_fsa_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'fsa_settings' in params:
            body_params = params['fsa_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/fsa/settings', 'PUT',
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

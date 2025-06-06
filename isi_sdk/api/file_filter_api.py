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


class FileFilterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_file_filter_settings(self, **kwargs):  # noqa: E501
        """get_file_filter_settings  # noqa: E501

        View File Filtering settings of an access zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_filter_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone: Specifies the access zones in which these settings apply.
        :return: FileFilterSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_filter_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_file_filter_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_file_filter_settings_with_http_info(self, **kwargs):  # noqa: E501
        """get_file_filter_settings  # noqa: E501

        View File Filtering settings of an access zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_filter_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone: Specifies the access zones in which these settings apply.
        :return: FileFilterSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_filter_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

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
            '/platform/3/file-filter/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileFilterSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_file_filter_settings(self, file_filter_settings, **kwargs):  # noqa: E501
        """update_file_filter_settings  # noqa: E501

        Modify one or more File Filtering settings for an access zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_file_filter_settings(file_filter_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FileFilterSettingsExtended file_filter_settings: (required)
        :param str zone: Specifies the access zones in which these settings apply.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_file_filter_settings_with_http_info(file_filter_settings, **kwargs)  # noqa: E501
        else:
            (data) = self.update_file_filter_settings_with_http_info(file_filter_settings, **kwargs)  # noqa: E501
            return data

    def update_file_filter_settings_with_http_info(self, file_filter_settings, **kwargs):  # noqa: E501
        """update_file_filter_settings  # noqa: E501

        Modify one or more File Filtering settings for an access zone  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_file_filter_settings_with_http_info(file_filter_settings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FileFilterSettingsExtended file_filter_settings: (required)
        :param str zone: Specifies the access zones in which these settings apply.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_filter_settings', 'zone']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_file_filter_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_filter_settings' is set
        if ('file_filter_settings' not in params or
                params['file_filter_settings'] is None):
            raise ValueError("Missing the required parameter `file_filter_settings` when calling `update_file_filter_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'file_filter_settings' in params:
            body_params = params['file_filter_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/file-filter/settings', 'PUT',
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

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


class SyncPoliciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_policy_reset_item(self, policy_reset_item, policy, **kwargs):  # noqa: E501
        """create_policy_reset_item  # noqa: E501

        Reset a SyncIQ policy incremental state and force a full sync/copy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy_reset_item(policy_reset_item, policy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty policy_reset_item: (required)
        :param str policy: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_policy_reset_item_with_http_info(policy_reset_item, policy, **kwargs)  # noqa: E501
        else:
            (data) = self.create_policy_reset_item_with_http_info(policy_reset_item, policy, **kwargs)  # noqa: E501
            return data

    def create_policy_reset_item_with_http_info(self, policy_reset_item, policy, **kwargs):  # noqa: E501
        """create_policy_reset_item  # noqa: E501

        Reset a SyncIQ policy incremental state and force a full sync/copy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_policy_reset_item_with_http_info(policy_reset_item, policy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty policy_reset_item: (required)
        :param str policy: (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_reset_item', 'policy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy_reset_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_reset_item' is set
        if ('policy_reset_item' not in params or
                params['policy_reset_item'] is None):
            raise ValueError("Missing the required parameter `policy_reset_item` when calling `create_policy_reset_item`")  # noqa: E501
        # verify the required parameter 'policy' is set
        if ('policy' not in params or
                params['policy'] is None):
            raise ValueError("Missing the required parameter `policy` when calling `create_policy_reset_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy' in params:
            path_params['Policy'] = params['policy']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'policy_reset_item' in params:
            body_params = params['policy_reset_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/sync/policies/{Policy}/reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

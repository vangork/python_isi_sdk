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


class CatalogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_catalog_list(self, **kwargs):  # noqa: E501
        """get_catalog_list  # noqa: E501

        List metadata for artifacts in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: the type of upgrade
        :param int onefs_version: onefs version
        :param str reference: onefs component that references this entry.
        :return: CatalogList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_catalog_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_catalog_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_catalog_list_with_http_info(self, **kwargs):  # noqa: E501
        """get_catalog_list  # noqa: E501

        List metadata for artifacts in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: the type of upgrade
        :param int onefs_version: onefs version
        :param str reference: onefs component that references this entry.
        :return: CatalogList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'onefs_version', 'reference']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_list" % key
                )
            params[key] = val
        del params['kwargs']

        if ('content_type' in params and
                len(params['content_type']) > 128):
            raise ValueError("Invalid value for parameter `content_type` when calling `get_catalog_list`, length must be less than or equal to `128`")  # noqa: E501
        if ('content_type' in params and
                len(params['content_type']) < 3):
            raise ValueError("Invalid value for parameter `content_type` when calling `get_catalog_list`, length must be greater than or equal to `3`")  # noqa: E501
        if 'onefs_version' in params and params['onefs_version'] > -1:  # noqa: E501
            raise ValueError("Invalid value for parameter `onefs_version` when calling `get_catalog_list`, must be a value less than or equal to `-1`")  # noqa: E501
        if 'onefs_version' in params and params['onefs_version'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `onefs_version` when calling `get_catalog_list`, must be a value greater than or equal to `0`")  # noqa: E501
        if ('reference' in params and
                len(params['reference']) > 128):
            raise ValueError("Invalid value for parameter `reference` when calling `get_catalog_list`, length must be less than or equal to `128`")  # noqa: E501
        if ('reference' in params and
                len(params['reference']) < 1):
            raise ValueError("Invalid value for parameter `reference` when calling `get_catalog_list`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'content_type' in params:
            query_params.append(('content_type', params['content_type']))  # noqa: E501
        if 'onefs_version' in params:
            query_params.append(('onefs_version', params['onefs_version']))  # noqa: E501
        if 'reference' in params:
            query_params.append(('reference', params['reference']))  # noqa: E501

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
            '/platform/14/catalog/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_catalog_readme(self, **kwargs):  # noqa: E501
        """get_catalog_readme  # noqa: E501

        README file content for artifact in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_readme(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: Path of the signed file to import in the catalog
        :param str hash: The sha256 hash of the file stored in catalog
        :return: CatalogReadme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_catalog_readme_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_catalog_readme_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_catalog_readme_with_http_info(self, **kwargs):  # noqa: E501
        """get_catalog_readme  # noqa: E501

        README file content for artifact in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_readme_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: Path of the signed file to import in the catalog
        :param str hash: The sha256 hash of the file stored in catalog
        :return: CatalogReadme
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_readme" % key
                )
            params[key] = val
        del params['kwargs']

        if ('file' in params and
                len(params['file']) > 4096):
            raise ValueError("Invalid value for parameter `file` when calling `get_catalog_readme`, length must be less than or equal to `4096`")  # noqa: E501
        if ('file' in params and
                len(params['file']) < 3):
            raise ValueError("Invalid value for parameter `file` when calling `get_catalog_readme`, length must be greater than or equal to `3`")  # noqa: E501
        if ('hash' in params and
                len(params['hash']) > 128):
            raise ValueError("Invalid value for parameter `hash` when calling `get_catalog_readme`, length must be less than or equal to `128`")  # noqa: E501
        if ('hash' in params and
                len(params['hash']) < 3):
            raise ValueError("Invalid value for parameter `hash` when calling `get_catalog_readme`, length must be greater than or equal to `3`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file' in params:
            query_params.append(('file', params['file']))  # noqa: E501
        if 'hash' in params:
            query_params.append(('hash', params['hash']))  # noqa: E501

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
            '/platform/14/catalog/readme', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogReadme',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_catalog_verify(self, **kwargs):  # noqa: E501
        """get_catalog_verify  # noqa: E501

        Verification of the signatures of any specified file, a specific artifact in the catalog, or all artifacts in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_verify(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: Path to unsigned file to verify
        :param str hash: The sha256 hash of the file stored in catalog
        :return: CatalogVerify
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_catalog_verify_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_catalog_verify_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_catalog_verify_with_http_info(self, **kwargs):  # noqa: E501
        """get_catalog_verify  # noqa: E501

        Verification of the signatures of any specified file, a specific artifact in the catalog, or all artifacts in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_catalog_verify_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file: Path to unsigned file to verify
        :param str hash: The sha256 hash of the file stored in catalog
        :return: CatalogVerify
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_verify" % key
                )
            params[key] = val
        del params['kwargs']

        if ('file' in params and
                len(params['file']) > 4096):
            raise ValueError("Invalid value for parameter `file` when calling `get_catalog_verify`, length must be less than or equal to `4096`")  # noqa: E501
        if ('file' in params and
                len(params['file']) < 3):
            raise ValueError("Invalid value for parameter `file` when calling `get_catalog_verify`, length must be greater than or equal to `3`")  # noqa: E501
        if ('hash' in params and
                len(params['hash']) > 128):
            raise ValueError("Invalid value for parameter `hash` when calling `get_catalog_verify`, length must be less than or equal to `128`")  # noqa: E501
        if ('hash' in params and
                len(params['hash']) < 3):
            raise ValueError("Invalid value for parameter `hash` when calling `get_catalog_verify`, length must be greater than or equal to `3`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file' in params:
            query_params.append(('file', params['file']))  # noqa: E501
        if 'hash' in params:
            query_params.append(('hash', params['hash']))  # noqa: E501

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
            '/platform/14/catalog/verify', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogVerify',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_catalog_clean(self, catalog_clean, **kwargs):  # noqa: E501
        """update_catalog_clean  # noqa: E501

        Removes any unreferenced artifacts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_clean(catalog_clean, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty catalog_clean: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_catalog_clean_with_http_info(catalog_clean, **kwargs)  # noqa: E501
        else:
            (data) = self.update_catalog_clean_with_http_info(catalog_clean, **kwargs)  # noqa: E501
            return data

    def update_catalog_clean_with_http_info(self, catalog_clean, **kwargs):  # noqa: E501
        """update_catalog_clean  # noqa: E501

        Removes any unreferenced artifacts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_clean_with_http_info(catalog_clean, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty catalog_clean: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_clean']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_catalog_clean" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_clean' is set
        if ('catalog_clean' not in params or
                params['catalog_clean'] is None):
            raise ValueError("Missing the required parameter `catalog_clean` when calling `update_catalog_clean`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'catalog_clean' in params:
            body_params = params['catalog_clean']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/catalog/clean', 'PUT',
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

    def update_catalog_export(self, catalog_export, **kwargs):  # noqa: E501
        """update_catalog_export  # noqa: E501

        Allows a catalog artifact to be exported out of the catalog to a file that the user can access. A typical use case would be if a user needs to export artifacts prior to a full catalog wipe or if a specific package is needed so that it can be applied on another cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_export(catalog_export, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogExport catalog_export: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_catalog_export_with_http_info(catalog_export, **kwargs)  # noqa: E501
        else:
            (data) = self.update_catalog_export_with_http_info(catalog_export, **kwargs)  # noqa: E501
            return data

    def update_catalog_export_with_http_info(self, catalog_export, **kwargs):  # noqa: E501
        """update_catalog_export  # noqa: E501

        Allows a catalog artifact to be exported out of the catalog to a file that the user can access. A typical use case would be if a user needs to export artifacts prior to a full catalog wipe or if a specific package is needed so that it can be applied on another cluster.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_export_with_http_info(catalog_export, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogExport catalog_export: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_export']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_catalog_export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_export' is set
        if ('catalog_export' not in params or
                params['catalog_export'] is None):
            raise ValueError("Missing the required parameter `catalog_export` when calling `update_catalog_export`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'catalog_export' in params:
            body_params = params['catalog_export']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/catalog/export', 'PUT',
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

    def update_catalog_import(self, catalog_import, **kwargs):  # noqa: E501
        """update_catalog_import  # noqa: E501

        Allow a signed package to be re-imported into the catalog. A typical use case would be if a required package is missing or damaged.  All user imported files will be subjected to a full signature verification including verifying the sha256 hashes for all data regions. Files that are not correctly signed will not be allowed in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_import(catalog_import, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogImport catalog_import: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_catalog_import_with_http_info(catalog_import, **kwargs)  # noqa: E501
        else:
            (data) = self.update_catalog_import_with_http_info(catalog_import, **kwargs)  # noqa: E501
            return data

    def update_catalog_import_with_http_info(self, catalog_import, **kwargs):  # noqa: E501
        """update_catalog_import  # noqa: E501

        Allow a signed package to be re-imported into the catalog. A typical use case would be if a required package is missing or damaged.  All user imported files will be subjected to a full signature verification including verifying the sha256 hashes for all data regions. Files that are not correctly signed will not be allowed in the catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_import_with_http_info(catalog_import, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogImport catalog_import: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_import']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_catalog_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_import' is set
        if ('catalog_import' not in params or
                params['catalog_import'] is None):
            raise ValueError("Missing the required parameter `catalog_import` when calling `update_catalog_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'catalog_import' in params:
            body_params = params['catalog_import']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/catalog/import', 'PUT',
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

    def update_catalog_remove(self, catalog_remove, **kwargs):  # noqa: E501
        """update_catalog_remove  # noqa: E501

        Allows a user to remove a specific sha256 artifact and  all related metadata. If the file is needed again in the future it will  need to be re-imported.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_remove(catalog_remove, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogRemove catalog_remove: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_catalog_remove_with_http_info(catalog_remove, **kwargs)  # noqa: E501
        else:
            (data) = self.update_catalog_remove_with_http_info(catalog_remove, **kwargs)  # noqa: E501
            return data

    def update_catalog_remove_with_http_info(self, catalog_remove, **kwargs):  # noqa: E501
        """update_catalog_remove  # noqa: E501

        Allows a user to remove a specific sha256 artifact and  all related metadata. If the file is needed again in the future it will  need to be re-imported.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_remove_with_http_info(catalog_remove, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogRemove catalog_remove: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_remove']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_catalog_remove" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_remove' is set
        if ('catalog_remove' not in params or
                params['catalog_remove'] is None):
            raise ValueError("Missing the required parameter `catalog_remove` when calling `update_catalog_remove`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'catalog_remove' in params:
            body_params = params['catalog_remove']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/catalog/remove', 'PUT',
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

    def update_catalog_repair(self, catalog_repair, **kwargs):  # noqa: E501
        """update_catalog_repair  # noqa: E501

        Repairs a damaged catalog. Erases catalog database, creates a new catalog database, and automatically reverifies and reimports all the artifacts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_repair(catalog_repair, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty catalog_repair: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_catalog_repair_with_http_info(catalog_repair, **kwargs)  # noqa: E501
        else:
            (data) = self.update_catalog_repair_with_http_info(catalog_repair, **kwargs)  # noqa: E501
            return data

    def update_catalog_repair_with_http_info(self, catalog_repair, **kwargs):  # noqa: E501
        """update_catalog_repair  # noqa: E501

        Repairs a damaged catalog. Erases catalog database, creates a new catalog database, and automatically reverifies and reimports all the artifacts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_catalog_repair_with_http_info(catalog_repair, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Empty catalog_repair: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_repair']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_catalog_repair" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_repair' is set
        if ('catalog_repair' not in params or
                params['catalog_repair'] is None):
            raise ValueError("Missing the required parameter `catalog_repair` when calling `update_catalog_repair`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'catalog_repair' in params:
            body_params = params['catalog_repair']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/14/catalog/repair', 'PUT',
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

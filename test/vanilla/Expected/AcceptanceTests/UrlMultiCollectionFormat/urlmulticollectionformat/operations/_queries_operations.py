# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class QueriesOperations(object):
    """QueriesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def array_string_multi_null(
            self, array_query=None, raw=False, **kwargs):
        """Get a null array of string using the multi-array format.

        :param array_query: a null array of string using the multi-array
         format
        :type array_query: list[str]
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<urlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = self.array_string_multi_null.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    array_string_multi_null.metadata = {'url': '/queries/array/multi/string/null'}

    def array_string_multi_empty(
            self, array_query=None, raw=False, **kwargs):
        """Get an empty array [] of string using the multi-array format.

        :param array_query: an empty array [] of string using the multi-array
         format
        :type array_query: list[str]
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<urlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = self.array_string_multi_empty.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    array_string_multi_empty.metadata = {'url': '/queries/array/multi/string/empty'}

    def array_string_multi_valid(
            self, array_query=None, raw=False, **kwargs):
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' ,
        null, ''] using the mult-array format.

        :param array_query: an array of string ['ArrayQuery1', 'begin!*'();:@
         &=+$,/?#[]end' , null, ''] using the mult-array format
        :type array_query: list[str]
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<urlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = self.array_string_multi_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    array_string_multi_valid.metadata = {'url': '/queries/array/multi/string/valid'}

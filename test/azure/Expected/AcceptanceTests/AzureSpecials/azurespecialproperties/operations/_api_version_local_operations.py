# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import uuid
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator import distributed_trace

from .. import models


class ApiVersionLocalOperations(object):
    """ApiVersionLocalOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
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
        self._config = config
    @distributed_trace
    def get_method_local_valid(self, cls=None, **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_method_local_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_method_local_valid.metadata = {'url': '/azurespecials/apiVersion/method/string/none/query/local/2.0'}

    @distributed_trace
    def get_method_local_null(self, cls=None, **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version = null to succeed.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_method_local_null.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_method_local_null.metadata = {'url': '/azurespecials/apiVersion/method/string/none/query/local/null'}

    @distributed_trace
    def get_path_local_valid(self, cls=None, **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_path_local_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_path_local_valid.metadata = {'url': '/azurespecials/apiVersion/path/string/none/query/local/2.0'}

    @distributed_trace
    def get_swagger_local_valid(self, cls=None, **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_swagger_local_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get_swagger_local_valid.metadata = {'url': '/azurespecials/apiVersion/swagger/string/none/query/local/2.0'}


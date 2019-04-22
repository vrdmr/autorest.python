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

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling.async_poller import async_poller, AsyncNoPolling
from msrestazure.polling.async_arm_polling import AsyncARMPolling

from ... import models


class LROsCustomHeaderOperations:
    """LROsCustomHeaderOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config


    async def _put_async_retry_succeeded_initial(
            self, product=None, *, raw=False, **kwargs):
        # Construct URL
        url = self.put_async_retry_succeeded.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.CloudErrorException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)
            header_dict = {
                'Azure-AsyncOperation': 'str',
                'Location': 'str',
                'Retry-After': 'int',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized

    async def put_async_retry_succeeded(
            self, product=None, *, raw=False, polling=True, **kwargs):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running put request,
        service returns a 200 to the initial request, with an entity that
        contains ProvisioningState=’Creating’. Poll the endpoint indicated in
        the Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of Product or ClientRawResponse<Product> if
         raw==True
        :rtype: ~~lro.models.Product or
         ~msrest.pipeline.ClientRawResponse[~lro.models.Product]
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._put_async_retry_succeeded_initial(
            product=product,
            raw=True,
            **kwargs
        )

        def get_long_running_output(response):
            header_dict = {
                'Azure-AsyncOperation': 'str',
                'Location': 'str',
                'Retry-After': 'int',
            }
            deserialized = self._deserialize('Product', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                client_raw_response.add_headers(header_dict)
                return client_raw_response

            return deserialized

        lro_delay = kwargs.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self, raw_result, get_long_running_output, polling_method)
    put_async_retry_succeeded.metadata = {'url': '/lro/customheader/putasync/retry/succeeded'}


    async def _put201_creating_succeeded200_initial(
            self, product=None, *, raw=False, **kwargs):
        # Construct URL
        url = self.put201_creating_succeeded200.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 201]:
            raise models.CloudErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)
        if response.status_code == 201:
            deserialized = self._deserialize('Product', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def put201_creating_succeeded200(
            self, product=None, *, raw=False, polling=True, **kwargs):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running put request,
        service returns a 201 to the initial request, with an entity that
        contains ProvisioningState=’Creating’.  Polls return this value until
        the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of Product or ClientRawResponse<Product> if
         raw==True
        :rtype: ~~lro.models.Product or
         ~msrest.pipeline.ClientRawResponse[~lro.models.Product]
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._put201_creating_succeeded200_initial(
            product=product,
            raw=True,
            **kwargs
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Product', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = kwargs.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self, raw_result, get_long_running_output, polling_method)
    put201_creating_succeeded200.metadata = {'url': '/lro/customheader/put/201/creating/succeeded/200'}


    async def _post202_retry200_initial(
            self, product=None, *, raw=False, **kwargs):
        # Construct URL
        url = self.post202_retry200.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [202]:
            raise models.CloudErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            header_dict = {
                'Location': 'str',
                'Retry-After': 'int',
            }
            client_raw_response.add_headers(header_dict)
            return client_raw_response

    async def post202_retry200(
            self, product=None, *, raw=False, polling=True, **kwargs):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running post request,
        service returns a 202 to the initial request, with 'Location' and
        'Retry-After' headers, Polls return a 200 with a response body after
        success.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None or ClientRawResponse<None> if raw==True
        :rtype: ~None or ~msrest.pipeline.ClientRawResponse[None]
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._post202_retry200_initial(
            product=product,
            raw=True,
            **kwargs
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                client_raw_response.add_headers({
                    'Location': 'str',
                    'Retry-After': 'int',
                })
                return client_raw_response

        lro_delay = kwargs.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self, raw_result, get_long_running_output, polling_method)
    post202_retry200.metadata = {'url': '/lro/customheader/post/202/retry/200'}


    async def _post_async_retry_succeeded_initial(
            self, product=None, *, raw=False, **kwargs):
        # Construct URL
        url = self.post_async_retry_succeeded.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct body
        if product is not None:
            body_content = self._serialize.body(product, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [202]:
            raise models.CloudErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            header_dict = {
                'Azure-AsyncOperation': 'str',
                'Location': 'str',
                'Retry-After': 'int',
            }
            client_raw_response.add_headers(header_dict)
            return client_raw_response

    async def post_async_retry_succeeded(
            self, product=None, *, raw=False, polling=True, **kwargs):
        """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is
        required message header for all requests. Long running post request,
        service returns a 202 to the initial request, with an entity that
        contains ProvisioningState=’Creating’. Poll the endpoint indicated in
        the Azure-AsyncOperation header for operation status.

        :param product: Product to put
        :type product: ~lro.models.Product
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None or ClientRawResponse<None> if raw==True
        :rtype: ~None or ~msrest.pipeline.ClientRawResponse[None]
        :raises: :class:`CloudErrorException<lro.models.CloudErrorException>`
        """
        raw_result = await self._post_async_retry_succeeded_initial(
            product=product,
            raw=True,
            **kwargs
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                client_raw_response.add_headers({
                    'Azure-AsyncOperation': 'str',
                    'Location': 'str',
                    'Retry-After': 'int',
                })
                return client_raw_response

        lro_delay = kwargs.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self, raw_result, get_long_running_output, polling_method)
    post_async_retry_succeeded.metadata = {'url': '/lro/customheader/postasync/retry/succeeded'}

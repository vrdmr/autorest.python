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

from ... import models


class DateModelOperations:
    """DateModelOperations async operations.

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

    async def get_null(
            self, *, raw=False, **kwargs):
        """Get null date value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_null.metadata = {'url': '/date/null'}

    async def get_invalid_date(
            self, *, raw=False, **kwargs):
        """Get invalid date value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_invalid_date.metadata = {'url': '/date/invaliddate'}

    async def get_overflow_date(
            self, *, raw=False, **kwargs):
        """Get overflow date value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_overflow_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_overflow_date.metadata = {'url': '/date/overflowdate'}

    async def get_underflow_date(
            self, *, raw=False, **kwargs):
        """Get underflow date value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_underflow_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_underflow_date.metadata = {'url': '/date/underflowdate'}

    async def put_max_date(
            self, date_body, *, raw=False, **kwargs):
        """Put max date value 9999-12-31.

        :param date_body:
        :type date_body: date
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.put_max_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_max_date.metadata = {'url': '/date/max'}

    async def get_max_date(
            self, *, raw=False, **kwargs):
        """Get max date value 9999-12-31.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_max_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_max_date.metadata = {'url': '/date/max'}

    async def put_min_date(
            self, date_body, *, raw=False, **kwargs):
        """Put min date value 0000-01-01.

        :param date_body:
        :type date_body: date
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.put_min_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_min_date.metadata = {'url': '/date/min'}

    async def get_min_date(
            self, *, raw=False, **kwargs):
        """Get min date value 0000-01-01.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: date or ClientRawResponse if raw=true
        :rtype: date or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_min_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_min_date.metadata = {'url': '/date/min'}

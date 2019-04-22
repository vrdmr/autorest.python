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


class PolymorphismOperations:
    """PolymorphismOperations async operations.

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

    async def get_valid(
            self, *, raw=False, **kwargs):
        """Get complex types that are polymorphic.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: Fish or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.Fish or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_valid.metadata['url']

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
            deserialized = self._deserialize('Fish', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_valid.metadata = {'url': '/complex/polymorphism/valid'}

    async def put_valid(
            self, complex_body, *, raw=False, **kwargs):
        """Put complex types that are polymorphic.

        :param complex_body: Please put a salmon that looks like this:
         {
         'fishtype':'Salmon',
         'location':'alaska',
         'iswild':true,
         'species':'king',
         'length':1.0,
         'siblings':[
         {
         'fishtype':'Shark',
         'age':6,
         'birthday': '2012-01-05T01:00:00Z',
         'length':20.0,
         'species':'predator',
         },
         {
         'fishtype':'Sawshark',
         'age':105,
         'birthday': '1900-01-05T01:00:00Z',
         'length':10.0,
         'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
         'species':'dangerous',
         },
         {
         'fishtype': 'goblin',
         'age': 1,
         'birthday': '2015-08-08T00:00:00Z',
         'length': 30.0,
         'species': 'scary',
         'jawsize': 5
         }
         ]
         };
        :type complex_body: ~bodycomplex.models.Fish
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_valid.metadata = {'url': '/complex/polymorphism/valid'}

    async def get_complicated(
            self, *, raw=False, **kwargs):
        """Get complex types that are polymorphic, but not at the root of the
        hierarchy; also have additional properties.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: Salmon or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.Salmon or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_complicated.metadata['url']

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
            deserialized = self._deserialize('Salmon', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_complicated.metadata = {'url': '/complex/polymorphism/complicated'}

    async def put_complicated(
            self, complex_body, *, raw=False, **kwargs):
        """Put complex types that are polymorphic, but not at the root of the
        hierarchy; also have additional properties.

        :param complex_body:
        :type complex_body: ~bodycomplex.models.Salmon
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_complicated.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Salmon')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_complicated.metadata = {'url': '/complex/polymorphism/complicated'}

    async def put_missing_discriminator(
            self, complex_body, *, raw=False, **kwargs):
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body:
        :type complex_body: ~bodycomplex.models.Salmon
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: Salmon or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.Salmon or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_missing_discriminator.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Salmon')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Salmon', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    put_missing_discriminator.metadata = {'url': '/complex/polymorphism/missingdiscriminator'}

    async def put_valid_missing_required(
            self, complex_body, *, raw=False, **kwargs):
        """Put complex types that are polymorphic, attempting to omit required
        'birthday' field - the request should not be allowed from the client.

        :param complex_body: Please attempt put a sawshark that looks like
         this, the client should not allow this data to be sent:
         {
         "fishtype": "sawshark",
         "species": "snaggle toothed",
         "length": 18.5,
         "age": 2,
         "birthday": "2013-06-01T01:00:00Z",
         "location": "alaska",
         "picture": base64(FF FF FF FF FE),
         "siblings": [
         {
         "fishtype": "shark",
         "species": "predator",
         "birthday": "2012-01-05T01:00:00Z",
         "length": 20,
         "age": 6
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "picture": base64(FF FF FF FF FE),
         "length": 10,
         "age": 105
         }
         ]
         }
        :type complex_body: ~bodycomplex.models.Fish
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_valid_missing_required.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_valid_missing_required.metadata = {'url': '/complex/polymorphism/missingrequired/invalid'}

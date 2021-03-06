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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AdditionalPropertiesClientConfiguration
from .operations import PetsOperations
from . import models


class AdditionalPropertiesClient(SDKClient):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AdditionalPropertiesClientConfiguration

    :ivar pets: Pets operations
    :vartype pets: additionalproperties.operations.PetsOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AdditionalPropertiesClientConfiguration(base_url)
        super(AdditionalPropertiesClient, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.pets = PetsOperations(
            self._client, self.config, self._serialize, self._deserialize)

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

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration import AutoRestAzureSpecialParametersTestClientConfiguration
from .operations import XMsClientRequestIdOperations
from .operations import SubscriptionInCredentialsOperations
from .operations import SubscriptionInMethodOperations
from .operations import ApiVersionDefaultOperations
from .operations import ApiVersionLocalOperations
from .operations import SkipUrlEncodingOperations
from .operations import OdataOperations
from .operations import HeaderOperations
from . import models


class AutoRestAzureSpecialParametersTestClient(PipelineClient):
    """Test Infrastructure for AutoRest


    :ivar xms_client_request_id: XMsClientRequestId operations
    :vartype xms_client_request_id: azurespecialproperties.operations.XMsClientRequestIdOperations
    :ivar subscription_in_credentials: SubscriptionInCredentials operations
    :vartype subscription_in_credentials: azurespecialproperties.operations.SubscriptionInCredentialsOperations
    :ivar subscription_in_method: SubscriptionInMethod operations
    :vartype subscription_in_method: azurespecialproperties.operations.SubscriptionInMethodOperations
    :ivar api_version_default: ApiVersionDefault operations
    :vartype api_version_default: azurespecialproperties.operations.ApiVersionDefaultOperations
    :ivar api_version_local: ApiVersionLocal operations
    :vartype api_version_local: azurespecialproperties.operations.ApiVersionLocalOperations
    :ivar skip_url_encoding: SkipUrlEncoding operations
    :vartype skip_url_encoding: azurespecialproperties.operations.SkipUrlEncodingOperations
    :ivar odata: Odata operations
    :vartype odata: azurespecialproperties.operations.OdataOperations
    :ivar header: Header operations
    :vartype header: azurespecialproperties.operations.HeaderOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription id, which appears in the path,
     always modeled in credentials. The value is always '1234-5678-9012-3456'
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None, config=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = config or AutoRestAzureSpecialParametersTestClientConfiguration(credentials, subscription_id, **kwargs)
        super(AutoRestAzureSpecialParametersTestClient, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-07-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.xms_client_request_id = XMsClientRequestIdOperations(
            self, self._config, self._serialize, self._deserialize)
        self.subscription_in_credentials = SubscriptionInCredentialsOperations(
            self, self._config, self._serialize, self._deserialize)
        self.subscription_in_method = SubscriptionInMethodOperations(
            self, self._config, self._serialize, self._deserialize)
        self.api_version_default = ApiVersionDefaultOperations(
            self, self._config, self._serialize, self._deserialize)
        self.api_version_local = ApiVersionLocalOperations(
            self, self._config, self._serialize, self._deserialize)
        self.skip_url_encoding = SkipUrlEncodingOperations(
            self, self._config, self._serialize, self._deserialize)
        self.odata = OdataOperations(
            self, self._config, self._serialize, self._deserialize)
        self.header = HeaderOperations(
            self, self._config, self._serialize, self._deserialize)

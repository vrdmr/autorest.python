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

from msrest.serialization import Model


class Bar(Model):
    """The URIs that are used to perform a retrieval of a public blob, queue or
    table object.

    :param recursive_point: Recursive Endpoints
    :type recursive_point: ~storage.models.Endpoints
    """

    _attribute_map = {
        'recursive_point': {'key': 'RecursivePoint', 'type': 'Endpoints'},
    }

    def __init__(self, *, recursive_point=None, **kwargs) -> None:
        super(Bar, self).__init__(**kwargs)
        self.recursive_point = recursive_point
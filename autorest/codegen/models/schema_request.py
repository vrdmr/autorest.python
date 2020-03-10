# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, List, Any

from .base_model import BaseModel
from .parameter import Parameter
from .parameter_list import ParameterList

class SchemaRequest(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        media_types: List[str],
        parameters: List[Parameter]
    ) -> None:
        super().__init__(yaml_data)
        self.media_types = media_types
        self.parameters = ParameterList(parameters)

    @property
    def body_parameter_has_schema(self) -> bool:
        """Tell if that request has a parameter that defines a body.
        """
        return any([p for p in self.parameters if hasattr(p, 'schema') and p.schema])

    @property
    def is_stream_request(self) -> bool:
        """Is the request expected to be streamable, like a download."""
        if self.yaml_data['protocol']['http'].get('knownMediaType'):
            return self.yaml_data['protocol']['http']['knownMediaType'] == 'binary' # FIXME: this might be an m4 issue
        return self.yaml_data["protocol"]["http"].get("binary", False)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "SchemaRequest":
        parameters = [
            Parameter.from_yaml(yaml)
            for yaml in yaml_data.get("parameters", [])
        ]

        return cls(
            yaml_data=yaml_data,
            media_types=yaml_data["protocol"]["http"].get("mediaTypes", []),
            parameters=parameters
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.media_types}>"

from __future__ import annotations

from typing import List, Union

from pydantic import BaseModel


class AttributeModel(BaseModel):
    trait_type: str
    value: Union[int, str]


class MetadataModel(BaseModel):
    image: str
    name: str
    description: str
    edition: int
    date: int
    attributes: List[AttributeModel]

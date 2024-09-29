from typing import List
from pydantic import BaseModel, root_validator


class ClassPage(BaseModel):
    link: str
    text: str


class ClassQueryError(BaseModel):
    detail: str


class Class(BaseModel):
    id: str
    name: str
    description: str
    credits: str
    prerequisites: str
    offered: List[str]
    cross_listed: List[str]
    distribution: List[str]
    link: str

    @root_validator(pre=True)
    def strip_all_fields(cls, values):
        def recursive_strip(value):
            if isinstance(value, str):
                return value.strip()
            elif isinstance(value, list):
                return [recursive_strip(item) for item in value]
            else:
                return value

        return {key: recursive_strip(value) for key, value in values.items()}

from typing import List
from pydantic import BaseModel


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

from pydantic import BaseModel
from typing import List

class Version(BaseModel):
    version: str
    description: str

    class ConfigDict:
        from_attributes = True

class TechStackItem(BaseModel):
    name: str
    description: str
    versions: List[Version] = []

    class ConfigDict:
        from_attributes = True

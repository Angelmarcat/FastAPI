from typing import Optional
from pydantic import BaseModel

class People(BaseModel):
    id: Optional[str]
    name: str
    age: int
    orderBy: int
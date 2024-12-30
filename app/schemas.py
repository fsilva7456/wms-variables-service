from pydantic import BaseModel
from typing import Optional

class VariableBase(BaseModel):
    name: str
    value: Optional[str] = None

class VariableCreate(VariableBase):
    pass

class Variable(VariableBase):
    id: int

    class Config:
        orm_mode = True
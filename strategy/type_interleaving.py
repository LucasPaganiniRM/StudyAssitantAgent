from pydantic import BaseModel
from typing import Literal

class TypeInterleaving(BaseModel):
  type: Literal["Procedural", "Declarative"]
from pydantic import BaseModel
from typing import Optional, List, Dict, Literal
from pydantic import AnyUrl, EmailStr

class Pet(BaseModel):
    pet_age: Optional[int]
    breed: Optional[str]
    pet_gender: Optional[bool]
    pet_name: Optional[str]
    owner_id: Optional[str] 


class Owner(BaseModel):
    address: Optional[str]
    owner_age: Optional[int]
    contact: Optional[str]
    email: Optional[EmailStr]
    owner_name: Optional[str]
    pets: Optional[List[str]] = []
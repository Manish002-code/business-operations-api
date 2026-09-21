from pydantic import BaseModel, EmailStr, ConfigDict


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    company: str


class CustomerUpdate(BaseModel):
    name: str
    email: EmailStr
    company: str


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    company: str

    model_config = ConfigDict(from_attributes=True)
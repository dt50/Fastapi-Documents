from pydantic import BaseModel, Field


class UserReg(BaseModel):
    user_name: str = Field(..., min_length=0, max_length=20)
    full_name: str = Field(..., min_length=0, max_length=50)
    email: str = Field(..., min_length=0, max_length=50)
    password: str = Field(..., min_length=0, max_length=20)


class UserIn(BaseModel):
    username: str = Field(..., min_length=0, max_length=20)
    password: str = Field(..., min_length=0, max_length=20)


class UserOut(BaseModel):
    id: int = None
    username: str = None
    fullname: str = None

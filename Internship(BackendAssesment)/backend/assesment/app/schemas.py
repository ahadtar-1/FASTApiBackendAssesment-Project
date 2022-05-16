from typing import List, Optional, Dict

from pydantic import BaseModel

class TenantBase(BaseModel):
    tenantid: int
    tenantname: str
    tenantaddress: str
    tenantcity: str
    tenantstate: str
    tenantcountry: str
    zipcode: str
    phonenumber: str
    url: str

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    pass

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    userid: int
    firstname: str
    lastname: str
    userdept: str
    userdesignation: str
    tenantid: int
    city: str
    country: str
    bio: str
    sociallinks: str
    employeeId: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    pass

    class Config:
        orm_mode = True
from sqlalchemy import Integer
from sqlalchemy.orm import Session

from app import models, schemas

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_tenant_by_id(db: Session, tenant_id: int):
    return db.query(models.Tenant).filter(models.Tenant.tenant_id == tenant_id).first()

def get_tenants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tenant).offset(skip).limit(limit).all()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_tenant(db: Session, tenant: schemas.TenantCreate):
    db_tenant = models.Tenant(tenantid=tenant.tenant_id, tenantname=tenant.tenant_name, tenantaddress=tenant.address, tenantcity=tenant.city, tenantstate=tenant.state, tenantcountry=tenant.country, zipcode=tenant.zip_code, phonenumber=tenant.phone, url=tenant.web_url)
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(userid=user.user_id, firstname=user.first_name, lastname=user.last_name, userdept=user.department, userdesignation=user.designation, tenantid=user.tenant_id, city=user.city, country=user.country, bio=user.bio, sociallinks=user.social_links, employeeId=user.employee_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_tenant(db: Session, tenant_id: int):
    record = db.query(models.Tenant).filter_by(tenant_id=tenant_id).first()
    db.delete(record)
    db.commit()

def delete_user(db: Session, user_id: int):
    record = db.query(models.User).filter_by(user_id=user_id).first()
    db.delete(record)
    db.commit()

##def update_tenant(db: Session,store_data):
    ##db.merge(store_data)
    ##db.commit()
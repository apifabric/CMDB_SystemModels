# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Device(Base):
    """description: Represents devices in the CMDB."""
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    model_id = Column(Integer, ForeignKey('model.id'))
    purchase_date = Column(DateTime)
    warranty_expiry = Column(DateTime)

class Model(Base):
    """description: Represents device models."""
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))

class Manufacturer(Base):
    """description: Represents manufacturers of devices and parts."""
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Location(Base):
    """description: Represents locations where devices are situated."""
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))

class Supplier(Base):
    """description: Represents suppliers providing devices and parts."""
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    contact_email = Column(String(100))
    contact_phone = Column(String(20))

class User(Base):
    """description: Represents system users interacting with the CMDB."""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'))

class Role(Base):
    """description: Represents roles assigned to system users."""
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Department(Base):
    """description: Represents departments within the organization."""
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

class Status(Base):
    """description: Represents device status."""
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class DeviceLog(Base):
    """description: Records historical statuses and operations of devices."""
    __tablename__ = 'device_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('device.id'))
    date = Column(DateTime)
    status_id = Column(Integer, ForeignKey('status.id'))

class Software(Base):
    """description: Represents software that can be installed on devices."""
    __tablename__ = 'software'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    version = Column(String(20))

class Incident(Base):
    """description: Represents incidents related to devices."""
    __tablename__ = 'incident'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey('device.id'))
    description = Column(String(200))
    date_reported = Column(DateTime)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    manufacturer1 = Manufacturer(id=1, name="TechCorp")
    manufacturer2 = Manufacturer(id=2, name="GadgetWorks")
    manufacturer3 = Manufacturer(id=3, name="DeviceMakers")
    manufacturer4 = Manufacturer(id=4, name="Innovatech")
    device1 = Device(id=1, name="Printer Model X", model_id=1, purchase_date=date(2021, 6, 1), warranty_expiry=date(2023, 6, 1))
    device2 = Device(id=2, name="Laptop Pro", model_id=2, purchase_date=date(2020, 9, 15), warranty_expiry=date(2022, 9, 15))
    device3 = Device(id=3, name="Server Prime", model_id=3, purchase_date=date(2019, 11, 18), warranty_expiry=date(2021, 11, 18))
    device4 = Device(id=4, name="Router Spec", model_id=4, purchase_date=date(2022, 7, 10), warranty_expiry=date(2024, 7, 10))
    incident1 = Incident(id=1, device_id=1, description="Printer not responding", date_reported=date(2023, 3, 10))
    incident2 = Incident(id=2, device_id=2, description="Laptop overheating", date_reported=date(2023, 5, 12))
    incident3 = Incident(id=3, device_id=3, description="Server downtime", date_reported=date(2023, 1, 22))
    incident4 = Incident(id=4, device_id=4, description="Router latency", date_reported=date(2023, 4, 5))
    
    
    
    session.add_all([manufacturer1, manufacturer2, manufacturer3, manufacturer4, device1, device2, device3, device4, incident1, incident2, incident3, incident4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')

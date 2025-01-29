# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 29, 2025 07:30:21
# Database: sqlite:////tmp/tmp.FkOUimFYnI-01JJRFENR7ZPV656232F64GS38/CMDB_SystemModels/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Department(Base):  # type: ignore
    """
    description: Represents departments within the organization.
    """
    __tablename__ = 'department'
    _s_collection_name = 'Department'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Location(Base):  # type: ignore
    """
    description: Represents locations where devices are situated.
    """
    __tablename__ = 'location'
    _s_collection_name = 'Location'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))

    # parent relationships (access parent)

    # child relationships (access children)



class Manufacturer(Base):  # type: ignore
    """
    description: Represents manufacturers of devices and parts.
    """
    __tablename__ = 'manufacturer'
    _s_collection_name = 'Manufacturer'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ModelList : Mapped[List["Model"]] = relationship(back_populates="manufacturer")



class Role(Base):  # type: ignore
    """
    description: Represents roles assigned to system users.
    """
    __tablename__ = 'role'
    _s_collection_name = 'Role'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    UserList : Mapped[List["User"]] = relationship(back_populates="role")



class Software(Base):  # type: ignore
    """
    description: Represents software that can be installed on devices.
    """
    __tablename__ = 'software'
    _s_collection_name = 'Software'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    version = Column(String(20))

    # parent relationships (access parent)

    # child relationships (access children)



class Status(Base):  # type: ignore
    """
    description: Represents device status.
    """
    __tablename__ = 'status'
    _s_collection_name = 'Status'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    DeviceLogList : Mapped[List["DeviceLog"]] = relationship(back_populates="status")



class Supplier(Base):  # type: ignore
    """
    description: Represents suppliers providing devices and parts.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_email = Column(String(100))
    contact_phone = Column(String(20))

    # parent relationships (access parent)

    # child relationships (access children)



class Model(Base):  # type: ignore
    """
    description: Represents device models.
    """
    __tablename__ = 'model'
    _s_collection_name = 'Model'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    manufacturer_id = Column(ForeignKey('manufacturer.id'))

    # parent relationships (access parent)
    manufacturer : Mapped["Manufacturer"] = relationship(back_populates=("ModelList"))

    # child relationships (access children)
    DeviceList : Mapped[List["Device"]] = relationship(back_populates="model")



class User(Base):  # type: ignore
    """
    description: Represents system users interacting with the CMDB.
    """
    __tablename__ = 'user'
    _s_collection_name = 'User'  # type: ignore

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    role_id = Column(ForeignKey('role.id'))

    # parent relationships (access parent)
    role : Mapped["Role"] = relationship(back_populates=("UserList"))

    # child relationships (access children)



class Device(Base):  # type: ignore
    """
    description: Represents devices in the CMDB.
    """
    __tablename__ = 'device'
    _s_collection_name = 'Device'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model_id = Column(ForeignKey('model.id'))
    purchase_date = Column(DateTime)
    warranty_expiry = Column(DateTime)

    # parent relationships (access parent)
    model : Mapped["Model"] = relationship(back_populates=("DeviceList"))

    # child relationships (access children)
    DeviceLogList : Mapped[List["DeviceLog"]] = relationship(back_populates="device")
    IncidentList : Mapped[List["Incident"]] = relationship(back_populates="device")



class DeviceLog(Base):  # type: ignore
    """
    description: Records historical statuses and operations of devices.
    """
    __tablename__ = 'device_log'
    _s_collection_name = 'DeviceLog'  # type: ignore

    id = Column(Integer, primary_key=True)
    device_id = Column(ForeignKey('device.id'))
    date = Column(DateTime)
    status_id = Column(ForeignKey('status.id'))

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("DeviceLogList"))
    status : Mapped["Status"] = relationship(back_populates=("DeviceLogList"))

    # child relationships (access children)



class Incident(Base):  # type: ignore
    """
    description: Represents incidents related to devices.
    """
    __tablename__ = 'incident'
    _s_collection_name = 'Incident'  # type: ignore

    id = Column(Integer, primary_key=True)
    device_id = Column(ForeignKey('device.id'))
    description = Column(String(200))
    date_reported = Column(DateTime)

    # parent relationships (access parent)
    device : Mapped["Device"] = relationship(back_populates=("IncidentList"))

    # child relationships (access children)

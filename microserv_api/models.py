from microserv_api import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Region(Base):
    __tablename__ = "region"
    region_id = Column(Integer, primary_key=True)
    region_ref = Column(String, nullable=False)
    region_name = Column(String, nullable=False)
    depts = relationship("Department", back_populates="region")

class Department(Base):
    __tablename__ = "department"
    dept_id = Column(String, primary_key=True)
    region_id = Column(Integer, ForeignKey("region.region_id"), nullable=False)
    dept_ref = Column(String, nullable=False)
    dept_name = Column(String, nullable=False)
    region = relationship("Region", back_populates="depts", lazy="selectin")
    municipalities = relationship("Municipality", back_populates="dept")

class Municipality(Base):
    __tablename__ = "municipality"
    mun_id = Column(Integer, primary_key=True)
    dept_id = Column(String, ForeignKey("department.dept_id"), nullable=False)
    mun_name = Column(String, nullable=False)
    mun_code = Column(String, nullable=False)
    insee_code = Column(String, nullable=True)
    gps_lat = Column(Float, nullable=True)
    gps_lng = Column(Float, nullable=True)
    dept = relationship("Department", back_populates="municipalities", lazy="selectin")

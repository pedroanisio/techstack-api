from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class TechStackDB(Base):
    __tablename__ = "tech_stacks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    versions = relationship("VersionDB", back_populates="tech_stack", cascade="all, delete")

class VersionDB(Base):
    __tablename__ = "versions"
    id = Column(Integer, primary_key=True, index=True)
    version = Column(String, index=True)
    description = Column(Text)
    tech_stack_id = Column(Integer, ForeignKey("tech_stacks.id"))
    tech_stack = relationship("TechStackDB", back_populates="versions")

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel):
    """ """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity')

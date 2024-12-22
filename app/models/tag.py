# app/models/tag.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name =  Column(String(50), unique=True, nullable=False)

    posts = relationship(
        "Post", secondary="post_tags", back_populates="tags"
    )
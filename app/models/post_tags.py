# app/models/post_tags.py

from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class PostTags(Base):
    __tablename__ = "post_tags"

    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
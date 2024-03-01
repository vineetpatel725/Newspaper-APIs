from sqlalchemy import Column
from sqlalchemy.types import VARCHAR, BIGINT, TIMESTAMP, TEXT

from app.db import Base


class Headlines(Base):
    __tablename__ = "headlines"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    source_id = Column(VARCHAR(255))
    author = Column(VARCHAR(255))
    title = Column(VARCHAR(255))
    description = Column(TEXT)
    url = Column(VARCHAR(512))
    image_url = Column(VARCHAR(512))
    published_at = Column(VARCHAR(50))
    content = Column(TEXT)

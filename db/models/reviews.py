from sqlalchemy import UUID, ForeignKey, String, Column, TIMESTAMP
from .base import Base

import uuid
import datetime


class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("Users.id"), nullable=False)
    org_id = Column(UUID, ForeignKey("Organizations.id"), nullable=False)
    body = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

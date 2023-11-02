from sqlalchemy import UUID, ForeignKey, String, Column, TIMESTAMP
from db.models.base_model import Base

from sqlalchemy.ext.declarative import as_declarative

import uuid
from datetime import datetime


@as_declarative()
class Complaints(Base):
    __tablename__ = "complaints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    org_id = Column(UUID, ForeignKey("organizations.id"), nullable=False)
    body = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)


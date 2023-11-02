from sqlalchemy import UUID, ForeignKey, String, Column, TIMESTAMP, Boolean, Integer
from db.models.base_model import Base
from sqlalchemy.ext.declarative import as_declarative
import uuid
from datetime import datetime


@as_declarative()
class In_block_codes(Base):
    __tablename__ = "in_block_codes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(UUID, ForeignKey("otp_codes.id"), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

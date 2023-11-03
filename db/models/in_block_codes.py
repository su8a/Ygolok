import uuid

from datetime import datetime
from sqlalchemy import UUID, ForeignKey, Column, TIMESTAMP
from db.models.base_model import Base


class InBlockCodes(Base):
    __tablename__ = "in_block_codes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(UUID, ForeignKey("otp_codes.id"), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

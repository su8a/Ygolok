from sqlalchemy import UUID, ForeignKey, String,  Column, TIMESTAMP, Boolean, Integer
from database import Base
from models.otp_codes import Otp_codes
import uuid
import datetime


class In_block_codes(Base):
    __tablename__ = "in_block_codes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_id = Column(UUID,ForeignKey("Otp_codes.id"),nullable=False)
    created_at = Column(TIMESTAMP,default=datetime.utcnow)

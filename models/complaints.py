from sqlalchemy import UUID, ForeignKey, String, Column, TIMESTAMP
from database import Base
from models.Organizations import Organizations
from models.users import Users

import uuid
import datetime


class Complaints(Base):
    __tablename__ = "complaints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID,ForeignKey("Users.id"),nullable=False)
    org_id = Column(UUID,ForeignKey("Organizations.id"),nullable=False)
    body = Column(String,nullable=False)
    created_at = Column(TIMESTAMP,default=datetime.utcnow)
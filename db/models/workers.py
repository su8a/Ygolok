import uuid

from sqlalchemy import UUID, ForeignKey, String, Column
from db.models.base_model import Base


class Workers(Base):
    __tablename__ = "workers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(UUID, ForeignKey("organizations.id"), nullable=False)
    full_name = Column(String, nullable=False)
    post = Column(String, nullable=False)
    avatar = Column(String, nullable=False)

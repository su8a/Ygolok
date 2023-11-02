from sqlalchemy import UUID, ForeignKey, String, Column
from .base import Base

import uuid


class OrganizationDocument(Base):
    __tablename__ = "organizationdocument"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(UUID, ForeignKey("Organizations.id"), nullable=False)
    doc_title = Column(String, nullable=False)
    address = Column(String, nullable=False)
    document = Column(String, nullable=False)

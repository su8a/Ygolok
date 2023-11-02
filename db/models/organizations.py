from sqlalchemy import UUID, ForeignKey, String, Column
from db.models.base_model import Base
from sqlalchemy.ext.declarative import as_declarative
import uuid


@as_declarative()
class Organizations(Base):
    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID, ForeignKey("owners.id"), nullable=False)
    title = Column(String, nullable=False)
    address = Column(String, nullable=False)
    logo = Column(String, nullable=False)
    inn = Column(String, nullable=False)
    ogrn = Column(String, nullable=False)
 
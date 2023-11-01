from sqlalchemy import UUID, ForeignKey, String, Boolean, Column
from database import Base
from models.organizations import Organizations

class Workers(Base):
    __tablename__ = "workers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id = Column(UUID,ForeignKey("Organizations.id"),nullable=False)
    full_name = Column(String,nullable=False)
    post = Column(String,nullable=False)
    avatar = Column(String,nullable=False)

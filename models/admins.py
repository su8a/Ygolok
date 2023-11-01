from sqlalchemy import UUID, ForeignKey, String, Boolean, Column
from database import Base
from models.organizations import Organizations
from models.users import Users
import uuid

class Workers(Base):
    __tablename__ = "workers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID,ForeignKey("Users.id"),nullable=False)
    org_id = Column(UUID,ForeignKey("Organizations.id"),nullable=False)
    email = Column(String,nullable=False)
    social_networks = Column(String,nullable=False)
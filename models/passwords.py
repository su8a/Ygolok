from sqlalchemy import UUID, ForeignKey, Integer, String, Boolean, Column
from database import Base
from models.users import Users
import uuid

class Passwords(Base):
    __tablename__ = "passwords"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey("Users.id"))
    password = Column(String,nullable=False)
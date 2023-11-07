from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from db.models.users import Users
from db.models.passwords import Passwords


class UserDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
        self,
        name: str,
        phone: str,
        hashed_password: str,
    ) -> Users:
        new_password = Passwords(
            password=hashed_password
        )
        print(new_password.id)
        self.db_session.add(new_password)
        await self.db_session.flush()
        new_user = Users(
            name=name,
            phone=phone,
            is_verified=False,
            password_id=new_password.id,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def get_user_by_phone(self, phone: str) -> Optional[Users]:
        query = select(Users).where(Users.phone == phone)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        print(user_row)
        if user_row:
            return user_row[0]

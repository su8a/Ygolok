from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from db.models.users import Users


class UserDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
        self,
        name: str,
        phone: str,
        hashed_password: str,
    ) -> Users:
        new_user = Users(
            name=name,
            phone=phone,
            hashed_password=hashed_password,
            is_verified=False,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def get_user_by_name(self, name: str) -> Optional[Users]:
        query = select(Users).where(Users.name == name)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        print(user_row)
        if user_row:
            return user_row[0]

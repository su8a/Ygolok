from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from db.models.passwords import Passwords


class PasswordDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_password(self, hashed_password: str) -> Passwords:
        new_password = Passwords(
            password=hashed_password
        )

        self.db_session.add(new_password)
        await self.db_session.flush()
        return new_password

    async def get_password(self, password_id: str) -> Optional[Passwords]:
        query = select(Passwords).where(Passwords.id == password_id)
        res = await self.db_session.execute(query)
        password_row = res.fetchone()
        print(password_row)
        if password_row:
            return password_row[0]

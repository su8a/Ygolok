from fastapi import APIRouter
from views.auth.schemas import UserCreate, ShowUser
from db.base import async_session
from db.dals.userdal import UserDAL
from db.dals.passworddal import PasswordDAL
from views.auth.hashing import Hasher

register_router = APIRouter()


async def _create_new_user(body: UserCreate) -> ShowUser:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            password_dal = PasswordDAL(session)
            password = await password_dal.create_password(hashed_password=Hasher.get_password_hash(body.password))
            user = await user_dal.create_user(
                name=body.name, phone=body.phone,
                password_id=password.id
            )
            return ShowUser(
                id=user.id, name=user.name, phone=user.phone, is_verified=user.is_verified
            )


@register_router.post('/', response_model=ShowUser)
async def register(body: UserCreate) -> ShowUser:
    return await _create_new_user(body)

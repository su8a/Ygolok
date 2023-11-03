from fastapi import APIRouter
from views.auth.schemas import UserCreate, ShowUser
from db.base import async_session
from db.dals.userdal import UserDAL
from views.auth.hashing import Hasher


register_router = APIRouter()


async def _create_new_user(body: UserCreate) -> ShowUser:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name, email=body.email,
                hashed_password=Hasher.get_password_hash(body.password)
            )
            return ShowUser(
                id=user.id, name=user.name, email=user.email, is_active=user.is_active
            )


@register_router.post('/', response_model=ShowUser)
async def register(body: UserCreate) -> ShowUser:
    return await _create_new_user(body)

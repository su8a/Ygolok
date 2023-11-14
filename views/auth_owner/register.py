from fastapi import APIRouter
from views.auth_owner.schemas import CreateOwner, ShowOwner
from db.base import async_session
from db.dals.ownerdal import OwnerDAL
from db.dals.passworddal import PasswordDAL
from views.secur.hashing import Hasher

owner_register_router = APIRouter()


async def _create_new_owner(body: CreateOwner) -> ShowOwner:
    async with async_session() as session:
        async with session.begin():
            owner_dal = OwnerDAL(session)
            password_dal = PasswordDAL(session)
            password = await password_dal.create_password(hashed_password=Hasher.get_password_hash(body.password))
            owner = await owner_dal.create_owner(
                name=body.name, phone=body.phone,
                last_name=body.last_name, patronymic=body.patronymic,
                inn=body.inn, ogrn=body.ogrn,
                password_id=password.id
            )
            return ShowOwner(
                id=owner.id, name=owner.name, phone=owner.phone, is_verified=owner.is_verified,
                inn=owner.inn, ogrn=owner.ogrn, last_name=owner.last_name, patronymic=owner.patronymic,

            )


@owner_register_router.post('/', response_model=ShowOwner, tags=['owner'])
async def register(body: CreateOwner) -> ShowOwner:
    return await _create_new_owner(body)

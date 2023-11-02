from datetime import timedelta
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from db.dals.userdal import UserDAL
from db.models.users import Users
from db.session import get_db
from views.auth.hashing import Hasher
from views.auth.security import create_access_token
from views.auth.schemas import Token
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

login_router = APIRouter()


async def _get_user_by_name_for_auth(name: str, db: AsyncSession):
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            return await user_dal.get_user_by_name(name)


async def authenticate_user(name: str, password: str, db: AsyncSession) -> Optional[Users]:
    user = await _get_user_by_name_for_auth(name=name, db=db)
    if not user or not Hasher.verify_password(password, user.hashed_password):
        return
    return user


@login_router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.name, 'other_custom_data': [1, 2, 3, 4]},
        live_time=access_token_expires,
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login/token')


async def get_current_user_from_token(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
    )
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        name: str = payload.get('sub')
        print('username extracted is ', name)
        if not name:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await _get_user_by_name_for_auth(name=name, db=db)
    if not user:
        raise credentials_exception
    return user


@login_router.get("/test_about_me")
async def sample_endpoint_under_jwt(
    current_user: Users = Depends(get_current_user_from_token),
):
    return {"Success": True, "current_user":
            {
                current_user.name, current_user.email,
                current_user.id, current_user.is_active
                }
            }

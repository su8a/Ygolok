from datetime import datetime
from datetime import timedelta
from typing import Optional, Dict

from jose import jwt

from config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


def create_access_token(data: Dict, live_time: Optional[timedelta] = None):
    to_encode = data.copy()
    if live_time:
        death_time = datetime.utcnow() + live_time
    else:
        death_time = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({'exp': death_time})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM
    )

    return encoded_jwt

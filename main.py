from fastapi import FastAPI, APIRouter

from views.auth.register import register_router
from views.auth.login import login_router
import uvicorn


app = FastAPI(
    title="Ygolok"
)

main_api_router = APIRouter()

main_api_router.include_router(register_router, prefix='/register')
main_api_router.include_router(login_router, prefix='/login')

app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

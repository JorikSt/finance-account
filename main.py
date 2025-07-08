from fastapi import FastAPI
from api.v1.routes.user import router as user_router



app = FastAPI()


# @app.post('/auth/register')
# async def registration():
#     pass

app.include_router(user_router)

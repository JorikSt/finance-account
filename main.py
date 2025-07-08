from fastapi import FastAPI
from api.endpoints.user import router as user_router



app = FastAPI()


# @app.post('/auth/register')
# async def registration():
#     pass

app.include_router(user_router)

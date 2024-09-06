from fastapi import FastAPI

from apps.views import router


app = FastAPI()
app.include_router(router)
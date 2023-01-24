import uvicorn
from fastapi import FastAPI

from src import views


app = FastAPI()
app.include_router(views.router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000, reload=True
    )



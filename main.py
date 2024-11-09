from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

from courses import courses_router


app = FastAPI()


"""
Set up for logger
"""
logging.basicConfig(
    level=logging.ERROR,
)


"""
All routes
"""
app.include_router(courses_router)


"""
CORS setup to allow requests from everywhere
"""
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

app = app

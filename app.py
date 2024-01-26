from fastapi import FastAPI
from routes.people import people
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(people)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST","DELETE"],
    allow_headers=["*"],
)

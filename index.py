from fastapi import FastAPI
from routes.note import Note

app = FastAPI()
app.include_router(Note)
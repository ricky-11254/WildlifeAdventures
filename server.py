from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()
app.mount("/", StaticFiles(directory=os.getcwd(), html=True), name="static")

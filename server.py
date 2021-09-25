from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()


@app.get("/")
def inex_page():
    return Response("Привееет!!!!", media_type="text/html")

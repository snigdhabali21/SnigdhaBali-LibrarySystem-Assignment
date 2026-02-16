 
import os
import base64
from fastapi import Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()  # loads .env file

USERNAME = os.getenv("AUTH_USERNAME")
PASSWORD = os.getenv("AUTH_PASSWORD")

async def middleware(request: Request, call_next):
    auth = request.headers.get("Authorization")

    if not auth or not auth.startswith("Basic "):
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"}
        )

    try:
        encoded = auth.split(" ")[1]
        decoded = base64.b64decode(encoded).decode("utf-8")
        username, password = decoded.split(":")
    except Exception:
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid Authorization header"}
        )

    if username != USERNAME or password != PASSWORD:
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"}
        )

    request.state.user = username  # attach authenticated user
    return await call_next(request)



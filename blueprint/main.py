from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, status

from blueprint import heartbeat
from blueprint.auth import routes as user_routes
from blueprint.common.exceptions import CustomException

load_dotenv()
app = FastAPI(
    title="Blueprint FastAPI Application",
    description="Blueprint fastapi application with postgres",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)
app.include_router(heartbeat.router)
app.include_router(user_routes.public_routes)
app.include_router(user_routes.authenticated_routes)


@app.exception_handler(CustomException)
def global_exception_handler(request: Request, exc: CustomException):
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=str(exc),
    )

from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.exceptions import RequestValidationError, ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers import pet, owner
from firebase_admin import auth

app = FastAPI(
    title="Pet API",
    description="Backend for the PetAPI",
    version="1.0",
    openapi_tags=tags_metadata
)


tags_metadata = [
    {
        "name": "Pet",
        "description": "Endpoints related to operations on the **Pets**\
            collection."
    },
    {
        "name": "Owner",
        "description": "Endpoints related to operations on the **Owner**\
            collection."
    }
]




@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(exc)
    return Response(status_code=422, content=str(exc))


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(exc)
    return Response(status_code=exc.status_code, content=exc.detail)

app.include_router(
    pet.router,
    prefix="/pet",
    tags=["Pet"]
)

app.include_router(
    owner.router,
    prefix="/owner",
    tags=["Owner"]
)


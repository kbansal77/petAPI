from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.exceptions import RequestValidationError, ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers import pet, owner
from firebase_admin import auth

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

app = FastAPI(
    title="Pet API",
    description="Backend for the Pet API",
    version="1.0",
    openapi_tags=tags_metadata
)


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

# app.include_router(
#     post.router,
#     prefix="/post",
#     tags=["Post"]
# )

# app.include_router(
#     course.router,
#     prefix="/course",
#     tags=["Course"]
# )

# app.include_router(
#     chapter.router,
#     prefix="/chapter",
#     tags=["Chapter"]
# )

# app.include_router(
#     user.router,
#     prefix="/user",
#     tags=["User"]
# )

# app.include_router(
#     badge.router,
#     prefix="/badge",
#     tags=["Badge"]
# )

# app.include_router(
#     bookmark.router,
#     prefix="/bookmark",
#     tags=["Bookmark"]
# )

# app.include_router(
#     notification.router,
#     prefix="/notification",
#     tags=["Notification"]
# )

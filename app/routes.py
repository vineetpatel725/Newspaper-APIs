from typing import Optional

from fastapi import APIRouter, status, Header, Request
from fastapi.responses import JSONResponse

from logs import logger
from app.services import store_top_headlines

newspaper_router = APIRouter(prefix="/api/v1/newspaper", tags=["Newspaper"])


@newspaper_router.post("/top_headlines", status_code=status.HTTP_201_CREATED)
def save_top_headlines(request: Request) -> JSONResponse:
    logger.info(f"API Request URL:: {request.url} || API Path Params :: {request.path_params} || API Query Params :: {request.query_params}")
    response: Optional[JSONResponse] = None
    try:
        headlines_response: dict = store_top_headlines()
        response: JSONResponse = JSONResponse(status_code=headlines_response['code'], content=headlines_response)
    except Exception as e:
        logger.error(f"Error :: {e}", exc_info=True)
        response: JSONResponse = JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "failure",
                "messages": "Internal Server Error",
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
        )
    finally:
        logger.info(f"API Response :: {response}")
        return response

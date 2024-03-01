import requests
from fastapi import status
from requests import Response

from config import global_config
from app.models import Headlines
from app.db import Session
from logs import logger
from celery_app import app


@app.task
def retrieve_newspaper_details(headlines_or_everything: str) -> dict:
    response: dict = dict(
        status="success",
        code=status.HTTP_201_CREATED,
        message=None,
        data=None
    )
    data: list[dict] = list()
    try:
        url: str = f"{global_config.get('NEWSPAPER_URL', 'URL')}/{headlines_or_everything}"
        parameters: dict = dict(country="in")
        headers: dict = {"X-Api-Key": global_config.get("NEWSPAPER_URL", "API_KEY")}
        logger.info(f"Newspaper API URL :: {url} || Parameters :: {parameters}")
        api_response: Response = requests.get(url=url, headers=headers, params=parameters)
        if api_response.status_code == status.HTTP_200_OK:
            data: list[dict] = api_response.json()['articles']
            if data:
                headlines_objs: list = [
                    Headlines(
                        source_id=headline['source']['id'],
                        author=headline['author'],
                        title=headline['title'],
                        description=headline['description'],
                        url=headline['url'],
                        image_url=headline['urlToImage'],
                        published_at=headline['publishedAt'],
                        content=headline['content']
                    ) for headline in data
                ]
                with Session() as session:
                    session.add_all(headlines_objs)
                    session.commit()
                response.update(message="Headlines retrieved and saved successfully!")
            else:
                response.update(
                    status="success",
                    code=status.HTTP_404_NOT_FOUND,
                    message="No Headlines found!"
                )
        else:
            logger.info(f"Newspaper error :: {api_response.content}")
            response.update(
                status="success",
                code=status.HTTP_404_NOT_FOUND,
                message="No Headlines found!"
            )
    except Exception as e:
        logger.error(f"Error :: {e}", exc_info=True)
        response.update(
            status="failure",
            code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="Internal Server Error!"
        )
    finally:
        return response


def store_top_headlines() -> dict:
    response = retrieve_newspaper_details("top-headlines")
    return response

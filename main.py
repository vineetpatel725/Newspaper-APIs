import uvicorn

from logs import logger


def run():
    logger.info("Starting uvicorn Server...")
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)
    logger.info("Stopping uvicorn Server...")


if __name__ == "__main__":
    run()

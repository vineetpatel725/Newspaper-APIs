from sqlalchemy import create_engine, Engine, engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import global_config

url: engine.URL = engine.URL.create(
    drivername="mysql+pymysql",
    username=global_config.get('MYSQL', 'USERNAME'),
    password=global_config.get('MYSQL', 'PASSWORD'),
    host=global_config.get('MYSQL', 'HOST'),
    database=global_config.get('MYSQL', 'DATABASE')
)
engine: Engine = create_engine(url, echo=True)
Session = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()

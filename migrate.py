from app.db import Base, engine
from app.models import Headlines

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

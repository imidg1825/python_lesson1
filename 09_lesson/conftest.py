import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.models import Base


def _get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError(
            "Не задана переменная окружения DATABASE_URL. "
            "Пример: postgresql+psycopg2://user:pass@localhost:5432/dbname"
        )
    return url


@pytest.fixture(scope="session")
def engine():
    engine_ = create_engine(_get_database_url(), future=True)
    Base.metadata.create_all(engine_)
    yield engine_
    Base.metadata.drop_all(engine_)


@pytest.fixture()
def db_session(engine):
    with Session(engine) as session:
        yield session
        session.rollback()

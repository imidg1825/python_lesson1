import uuid

import pytest

from client.yougile_api import YougileAPI


@pytest.fixture()
def api() -> YougileAPI:
    return YougileAPI()


@pytest.fixture()
def created_project(api: YougileAPI) -> str:
    title = f"test_project_{uuid.uuid4()}"
    r = api.create_project(title)

    assert r.status_code == 201, r.text

    project_id = r.json().get("id")
    assert project_id

    return project_id

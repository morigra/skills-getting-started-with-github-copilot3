from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_data

ORIGINAL_ACTIVITIES = deepcopy(activities_data)

@pytest.fixture(autouse=True)
def reset_activities():
    activities_data.clear()
    activities_data.update(deepcopy(ORIGINAL_ACTIVITIES))
    yield

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

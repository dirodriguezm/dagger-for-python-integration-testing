import pytest
from test_utils.services import create_postgres_container
import dagger
import sys
import os


@pytest.fixture
def check_ok():
    return "ok"


@pytest.fixture(scope="session")
async def postgres_service():
    running_ci = os.getenv("CI", False)
    if not running_ci:
        async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
            endpoint, psql_container = await create_postgres_container(client)
            yield endpoint
    else:
        yield "postgres:5432"

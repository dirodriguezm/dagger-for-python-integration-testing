import pytest
from test_utils.services import create_postgres_container
import dagger
import sys


@pytest.fixture
def check_ok():
    return "ok"


@pytest.fixture(scope="session")
async def postgres_service():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        endpoint = await create_postgres_container(client)
        yield endpoint

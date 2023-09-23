import pytest
import dagger
import sys


@pytest.fixture
def check_ok():
    return "ok"


@pytest.fixture(scope="session")
async def postgres_service():
    # create Dagger client
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        python = (
            client.container().from_("python:3.11-slim").with_exec(["python", "-V"])
        )

        # execute
        version = await python.stdout()
        return version

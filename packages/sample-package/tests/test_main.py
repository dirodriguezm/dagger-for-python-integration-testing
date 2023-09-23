import pytest
from sample_package.main import query_hello_world


def test_check_test_utils(check_ok):
    assert check_ok == "ok"


@pytest.mark.asyncio
async def test_query(postgres_service):
    ver = await postgres_service
    assert ver == "Python 3.11.5\n"
    assert query_hello_world() == [("Hello, World!",)]

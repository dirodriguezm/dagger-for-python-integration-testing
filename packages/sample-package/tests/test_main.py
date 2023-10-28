from sample_package.main import query_hello_world
from test_utils.fixtures import check_ok, postgres_service
import pytest


@pytest.mark.asyncio
async def test_check_test_utils(check_ok):
    assert check_ok == "ok"


@pytest.mark.asyncio
async def test_query(postgres_service):
    endpoint = await anext(postgres_service)
    host = endpoint.split(":")[0]
    port = endpoint.split(":")[1]
    db_url = f"dbname=postgres user=postgres password=postgres host={host} port={port}"
    assert query_hello_world(db_url) == [("Hello, World!",)]

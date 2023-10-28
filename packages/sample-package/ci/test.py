import sys
import dagger
import anyio
from test_utils.services import create_postgres_container
import pathlib


async def test_pipeline():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        _, postgres = await create_postgres_container(client)
        packages_dir = str(pathlib.Path(__file__).parent.parent.parent.absolute())
        source = (
            client.container()
            .from_("python:3.11-slim")
            .with_exec(["pip", "install", "poetry"])
            .with_env_variable("CI", "true")
            .with_directory(
                "/src",
                client.host().directory(packages_dir),
                exclude=[".venv"],
            )
            .with_service_binding("postgres", postgres)
        )
        runner = source.with_workdir("/src/sample-package").with_exec(
            ["poetry", "install"]
        )
        out = await runner.with_exec(["poetry", "run", "pytest"]).stderr()
        print(out)


anyio.run(test_pipeline)

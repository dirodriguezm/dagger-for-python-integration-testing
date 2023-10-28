import dagger


async def create_postgres_container(dagger_client: dagger.Client) -> str:
    postgres = (
        dagger_client.container()
        .from_("postgres")
        .with_env_variable("POSTGRES_USER", "postgres")
        .with_env_variable("POSTGRES_PASSWORD", "postgres")
        .with_env_variable("POSTGRES_DB", "postgres")
        .with_exposed_port(5432)
        .as_service()
    )
    tunnel = await dagger_client.host().tunnel(postgres).start()
    endpoint = await tunnel.endpoint()
    return endpoint

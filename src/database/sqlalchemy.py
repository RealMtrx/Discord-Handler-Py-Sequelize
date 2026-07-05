from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncEngine,
)
from sqlalchemy.orm import DeclarativeBase

from src.config import config


class Base(DeclarativeBase):
    pass


engine: AsyncEngine | None = None
async_session_maker: async_sessionmaker[AsyncSession] | None = None


def get_database_url() -> str:
    dialect = config.db_dialect.lower()
    if dialect == "sqlite":
        return f"sqlite+aiosqlite:///{config.db_storage}"
    elif dialect == "mysql":
        return (
            f"mysql+asyncmy://{config.db_username}:{config.db_password}"
            f"@{config.db_host}:{config.db_port}/{config.db_database}"
        )
    elif dialect == "postgresql":
        return (
            f"postgresql+asyncpg://{config.db_username}:{config.db_password}"
            f"@{config.db_host}:{config.db_port}/{config.db_database}"
        )
    return f"sqlite+aiosqlite:///{config.db_storage}"


async def setup_database():
    global engine, async_session_maker
    url = get_database_url()
    engine = create_async_engine(url, echo=False)
    async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("  ✅ Database connected successfully")
    return engine, async_session_maker


async def get_session() -> AsyncSession:
    if async_session_maker is None:
        raise RuntimeError("Database not initialized")
    return async_session_maker()


async def close_database():
    global engine
    if engine:
        await engine.dispose()
        print("  ✅ Database connection closed")

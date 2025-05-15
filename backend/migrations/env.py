"""Configuration script for Alembic migrations"""

from alembic import context
from sqlalchemy import engine_from_config, pool

from core.config import settings
from db.database import Base
from models.user import User
from models.photo import Photo

# this is the Alembic Config object
config = context.config

# Set the database URL in the Alembic config
section = config.config_ini_section
config.set_section_option(section, "sqlalchemy.url", 
                          f"mysql+pymysql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}"
                          f"@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}")

# Import all models for Alembic to detect
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
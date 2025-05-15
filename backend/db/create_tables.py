from db.database import Base, engine
from models.user import User
from models.photo import Photo

# Import all models here so they can be discovered by SQLAlchemy


def create_tables():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """Drop all tables in the database."""
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    print("Creating database tables...")
    create_tables()
    print("Database tables created successfully!")
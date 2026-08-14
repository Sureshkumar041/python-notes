from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# you cannot put it directly into the URL. Encode @ as %40:
DATABASE_URL = "postgresql://postgres:Welcome%40123@localhost:5432/python_db"

engine = create_engine(DATABASE_URL)

# Now that the connection was already verified, you don't need this test code permanently:
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT 1"))
#     print(result.scalar())

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    # creates a database session.
    db = SessionLocal()

    try:
        yield db
    finally:
        # makes sure the session is closed after the request.
        db.close()

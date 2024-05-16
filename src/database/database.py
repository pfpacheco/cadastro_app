# Importing necessary modules
from decouple import config  # For managing environment variables
from sqlalchemy import create_engine  # For creating a database engine
from sqlalchemy.orm import sessionmaker  # For creating a session factory


# Database class to handle database operations
class Database:

    # Constructor method to initialize the class
    def __init__(self):
        # Fetching the database URL from environment variables using Decouple
        self.database_url = config("POSTGRES_URL")
        # Creating a SQLAlchemy engine for connecting to the database
        # Note: connect_args={"check_same_thread": False} is for SQLite, can be omitted for other databases
        self.engine = create_engine(self.database_url, connect_args={"check_same_thread": False})
        # Creating a session maker bound to the engine for generating sessions
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    # Method to get a database session
    def get_db(self):
        # Creating a new database session
        db = self.session_local()
        try:
            # Yielding the database session to the caller
            yield db
        finally:
            # Ensuring the session is properly closed when done to release resources
            db.close()

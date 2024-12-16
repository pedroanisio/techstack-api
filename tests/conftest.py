import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.dependencies import get_db
from app.main import app

# Test database setup
TEST_DATABASE_URL = "sqlite:///./test_techstack.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the dependency for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply overrides to the app
app.dependency_overrides[get_db] = override_get_db

# Fixture to create tables and return a test client
@pytest.fixture(scope="module")
def test_client():
    # Create tables
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)

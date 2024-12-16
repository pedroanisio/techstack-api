import pytest

# Test for creating a tech stack
def test_create_tech_stack(test_client):
    tech_stack_data = {
        "name": "FastAPI",
        "description": "A modern web framework for Python",
        "versions": [
            {"version": "0.1.0", "description": "Initial version"},
            {"version": "0.2.0", "description": "Bug fixes"}
        ]
    }
    response = test_client.post("/techstack", json=tech_stack_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == tech_stack_data["name"]
    assert len(data["versions"]) == 2

# Fixture to ensure the tech stack exists
@pytest.fixture(scope="module")
def ensure_tech_stack_exists(test_client):
    try:
        tech_stack_data = {
            "name": "FastAPI",
            "description": "A modern web framework for Python",
            "versions": [
                {"version": "0.1.0", "description": "Initial version"},
                {"version": "0.2.0", "description": "Bug fixes"}
            ]
        }
        response = test_client.post("/techstack", json=tech_stack_data)
        assert response.status_code in [200, 400]  # 400 indicates it already exists
    except Exception as e:
        pytest.fail(f"Setup failed: {e}")

# Test for fetching all tech stacks
def test_get_all_tech_stacks(test_client, ensure_tech_stack_exists):
    response = test_client.get("/techstack")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

# Test for fetching a tech stack by name
def test_get_tech_stack_by_name(test_client, ensure_tech_stack_exists):
    response = test_client.get("/techstack/FastAPI")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "FastAPI"

# Test for adding a new version to an existing tech stack
def test_add_version_to_tech_stack(test_client, ensure_tech_stack_exists):
    version_data = {"version": "0.3.0", "description": "Added new features"}
    response = test_client.post("/techstack/FastAPI/versions", json=version_data)
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == version_data["version"]

# Test for fetching all versions of a tech stack
def test_get_versions_of_tech_stack(test_client, ensure_tech_stack_exists):
    response = test_client.get("/techstack/FastAPI/versions")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

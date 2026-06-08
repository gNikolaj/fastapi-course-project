import pytest


@pytest.mark.asyncio
async def test_create_user(client):
    response = await client.post("/users/", json={
        "email": "test@gmail.com",
        "password": "123456"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@gmail.com"
    assert data["is_active"] is True


@pytest.mark.asyncio
async def test_get_users(client):
    await client.post("/users/", json={
        "email": "test@gmail.com",
        "password": "123456"
    })

    response = await client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1
    assert len(data["users"]) == 1


@pytest.mark.asyncio
async def test_get_user_by_id(client):
    create = await client.post("/users/", json={
        "email": "test@gmail.com",
        "password": "123456"
    })
    user_id = create.json()["id"]

    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.asyncio
async def test_get_user_not_found(client):
    response = await client.get("/users/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_user(client):
    create = await client.post("/users/", json={
        "email": "test@gmail.com",
        "password": "123456"
    })
    user_id = create.json()["id"]

    response = await client.put(f"/users/{user_id}", json={
        "email": "updated@gmail.com"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "updated@gmail.com"


@pytest.mark.asyncio
async def test_delete_user(client):
    create = await client.post("/users/", json={
        "email": "test@gmail.com",
        "password": "123456"
    })
    user_id = create.json()["id"]

    response = await client.delete(f"/users/{user_id}")
    assert response.status_code == 204

    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 404

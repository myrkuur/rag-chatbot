import pytest
from httpx import AsyncClient
from fastapi import status
from app import app

@pytest.mark.asyncio
async def test_ingest_success():
    session_id = "test_session_1"
    test_url = "https://example.com"  # should have <p> for BS4 to work

    async with AsyncClient(app=app, base_url="http://test") as client:
        res = await client.post("/ingest", params={"url": test_url, "session_id": session_id})
        assert res.status_code == status.HTTP_200_OK
        assert res.json()["result"] == "SUCCESS"

@pytest.mark.asyncio
async def test_ask_response():
    session_id = "test_session_2"
    query = "What is this page about?"

    async with AsyncClient(app=app, base_url="http://test") as client:
        res = await client.post("/ask", params={"query": query, "session_id": session_id})
        assert res.status_code == status.HTTP_200_OK
        assert "response" in res.json()
        assert res.json()["session_id"] == session_id

@pytest.mark.asyncio
async def test_delete_user_data():
    session_id = "test_session_3"

    async with AsyncClient(app=app, base_url="http://test") as client:
        res = await client.get("/delete-user-data", params={"session_id": session_id})
        assert res.status_code == status.HTTP_200_OK
        assert res.json()["result"] == "SUCCESS"

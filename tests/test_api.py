import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_ask_response():
    session_id = "test_session_2"
    query = "What is this page about?"

    async with AsyncClient(base_url="http://localhost:8000") as client:
        res = await client.post("/ask", params={"query": query, "session_id": session_id})
        assert res.status_code == status.HTTP_200_OK
        assert "response" in res.json()
        assert res.json()["session_id"] == session_id


@pytest.mark.asyncio
async def test_delete_user_data():
    session_id = "test_session_3"

    async with AsyncClient(base_url="http://localhost:8000") as client:
        res = await client.get("/delete-user-data", params={"session_id": session_id})
        assert res.status_code == status.HTTP_200_OK
        assert res.json()["result"] == "SUCCESS"
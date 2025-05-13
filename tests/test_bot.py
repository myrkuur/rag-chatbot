import pytest
from unittest.mock import AsyncMock, patch
from telegram import Update
from bot import delete_all, ingest_url, handle_question

class FakeMessage:
    def __init__(self, text):
        self.text = text
        self.replies = []
    async def reply_text(self, msg):
        self.replies.append(msg)

@pytest.mark.asyncio
@patch("requests.get")
async def test_delete_all(mock_get):
    mock_get.return_value.json = lambda: {"result": "SUCCESS"}
    update = Update(update_id=123, message=FakeMessage("/delete"))
    context = AsyncMock()
    update.effective_chat = type("obj", (), {"id": 999})

    await delete_all(update, context)
    assert "SUCCESS" in update.message.replies[0]

@pytest.mark.asyncio
@patch("requests.post")
async def test_ingest_url(mock_post):
    mock_post.return_value.json = lambda: {"result": "SUCCESS"}
    update = Update(update_id=123, message=FakeMessage("/ingest http://test.com"))
    context = AsyncMock()
    context.args = ["http://test.com"]
    update.effective_chat = type("obj", (), {"id": 999})

    await ingest_url(update, context)
    assert "SUCCESS" in update.message.replies[0]

@pytest.mark.asyncio
@patch("requests.post")
async def test_handle_question(mock_post):
    mock_post.return_value.json = lambda: {
        "response": "Here's your answer.",
        "session_id": "999"
    }
    update = Update(update_id=123, message=FakeMessage("What is AI?"))
    context = AsyncMock()
    update.effective_chat = type("obj", (), {"id": 999})

    await handle_question(update, context)
    assert "Here's your answer." in update.message.replies[0]

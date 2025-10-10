from typing import Literal

from pydantic import BaseModel


class ConversationRound(BaseModel):
    content: str
    role: Literal["user", "assistant"]

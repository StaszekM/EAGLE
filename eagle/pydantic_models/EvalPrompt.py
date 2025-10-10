from typing import List

from pydantic import BaseModel

from .ConversationRound import ConversationRound


class EvalPrompt(BaseModel):
    question_id: int
    turns: List[ConversationRound]

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description="the text of the option shown to the user")
    next_node: Dict[str, Any] = Field(description="the next node content and its options")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="the main content of the story node")
    is_ending: bool = Field(description="whether this node is ending node")
    is_winning_ending: bool = Field(description="whether this node is winning ending node")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="the options for this node")


class StoryLLMResponse(BaseModel):
    title: str = Field(description="the title of the story")
    root_node: StoryNodeLLM = Field(description="the root node of the story")
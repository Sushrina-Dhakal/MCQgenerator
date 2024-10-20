from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatPerplexity

from enum import Enum

from dotenv import load_dotenv
load_dotenv()

import os
openai_key=os.getenv("OPENAI_API_KEY")
anthropic_key=os.getenv("ANTHROPIC_API_KEY")
perplexity_key=os.getenv("PERPLEXITY_API_KEY")

openai_model=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=openai_key
)

anthropic_model=ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0,
    api_key=anthropic_key
)

perplexity_model=ChatPerplexity(
    temperature=0,
    model="llama-3.1-sonar-small-128k-online",
    api_key=perplexity_key
)

class Models(Enum):
    Openai="openai"
    Anthropic="anthropic"
    Perplexity="perplexity"

def fetchllm(modelname: Models):
    if modelname==Models.Openai:
        return openai_model
    elif modelname==Models.Anthropic:
        return anthropic_model
    else:
        return perplexity_model
    

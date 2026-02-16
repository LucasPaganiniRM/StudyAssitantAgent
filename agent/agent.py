from langchain.tools import tool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END
from langgraph.graph import State


class ChooseInterleaving(BaseModel):
    
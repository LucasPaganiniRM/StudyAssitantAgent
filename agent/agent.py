from langchain.tools import tool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END as END_STATE
from langgraph.graph import State
from typing import List
from datetime import datetime
from langchain.schema import AIMessage, HumanMessage, SystemMessage

def identify_type_interleaving(state: State) -> str:
    content = state['messages'][-1].content
    messages = [
        SystemMessage(content=ANALYSIS_SYSTEM_PROMPT),
        HumanMessage(content=f"Content: {content}")
    ]
    response = llm.invoke(messages, response_format=TypeInterleaving)
    state['study_recuperation'].interleaving.method = response.content
    return response.content

def identify_interleaving_method_with_rag(state: State) -> str:
    content = state['messages'][-1].content
    messages = [
        SystemMessage(content=ANALYSIS_SYSTEM_PROMPT),
        HumanMessage(content=f"Content: {content}")
    ]
    response = llm.invoke(messages, response_format=InterleavingMethod)
    return response.content

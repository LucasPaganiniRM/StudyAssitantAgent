from langchain.tools import tool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END as END_STATE
from langgraph.graph import State
from typing import List
from datetime import datetime
from langchain.schema import AIMessage

class Interleaving(BaseModel):
    method: str = Field(description="Método de Interleaving")
    messages: List[AIMessage] = Field(description="Mensagens para enviar ao usuário")
    days_after: int = Field(description="Dias após o envio da mensagem")
    type_interleaving: str = Field(description="Tipo de Interleaving: Procedural ou ")

class StudyRecuperation(BaseModel):
    interleavings: List[Interleaving] = Field(description="Lista de Interleavings")
    date_spacings: List[datetime] = Field(description="Datas de espaçamento")

class State(StateGraph):
    study_recuperation: StudyRecuperation = Field(description="Recuperação de estudo")
    messages: List[Message] = Field(description="Mensagens para enviar ao usuário")



builder = StateGraph(State)
builder.add_node(START, State())

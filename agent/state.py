from pydantic import BaseModel, Field
from langgraph.graph import StateGraph
from langgraph.graph import State
from typing import List
from datetime import datetime
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from strategy.interleaving_method import InterleavingMethod
from strategy.type_interleaving import TypeInterleaving

class Interleaving(BaseModel):
    method: InterleavingMethod = Field(description="Método de Interleaving")
    messages: List[SystemMessage] = Field(description="Mensagens para enviar ao usuário")
    type_interleaving: TypeInterleaving = Field(description="Tipo de Interleaving: Procedural ou Declarativo")

class StudyRecuperation(BaseModel):
    interleavings: List[Interleaving] = Field(description="Lista de Interleavings")
    date_spacings: List[datetime] = Field(description="Datas de espaçamento")

class State(StateGraph):
    study_recuperation: StudyRecuperation = Field(description="Recuperação de estudo")
    messages: List[AIMessage | HumanMessage | SystemMessage] = Field(description="Mensagens para enviar ao usuário")

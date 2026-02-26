from abc import ABC, abstractmethod
from enum import Enum

class InterleavingMethod(ABC):
    """Classe base para os métodos de intercalação."""
    
    @abstractmethod
    def apply(self, *args, **kwargs):
        """Aplica a estratégia de intercalação."""
        pass

class Declarativo(InterleavingMethod):
    """Implementação do método de intercalação para conteúdo Declarativo."""
    
    FLASHCARDS = "Flashcards (Relacionais Simples)"
    BRAIN_DUMP = "Brain Dump (Mapa Mental)"
    TEACHING = "Ensino (Relacional Simples)"
    CHUNKMAPS = "Chunkmaps (GRINDEmaps)"
    GENERATED_QUESTIONS = "Perguntas Geradas (Avaliativas)"
    PRACTICE_QUESTIONS = "Perguntas de Prática (Método Estendido)"
 
    def apply(self, *args, **kwargs):
        # TODO: Implementar lógica de intercalação declarativa
        pass

class Procedural(InterleavingMethod):
    """Implementação do método de intercalação para conteúdo Procedural."""
    
    RETRIEVAL_EXECUTION_INTEGRATIVE = "Execução Recuperada (Integrativa)"
    CHALLENGES_INTEGRATIVE = "Desafios (Integrativos)"
    VARIABLE_MODIFICATION = "Modificação de Variáveis"
    RETRIEVAL_EXECUTION_APPLIED = "Execução Recuperada (Aplicada)"
    CHALLENGES_EDGE_CASES = "Desafios (Edge-Cases)"
    VARIABLE_ADDITION = "Adição de Variáveis"

    def apply(self, *args, **kwargs):
        # TODO: Implementar lógica de intercalação procedural
        pass

# StudyAgentMD â€“ InstruÃ§Ãµes para Agentes de IA

> Este arquivo Ã© reconhecido automaticamente por: **Claude** (CLAUDE.md), **Gemini** (GEMINI.md), **Cursor** (.cursorrules), **Windsurf**, **Copilot** e qualquer agente compatÃ­vel com o padrÃ£o `AGENTS.md`.

---

## ðŸŽ¯ PropÃ³sito deste Workspace

Este Ã© o workspace **StudyAgentMD** â€” um hub centralizado para gerenciar, automatizar e documentar tarefas de estudo usando o **TickTick** como sistema de produtividade pessoal do usuÃ¡rio (Lucas Emanuel).

O foco principal Ã© criar e gerenciar **tarefas de revisÃ£o espaÃ§ada** (*spaced repetition*) com tÃ©cnicas de *interleaving* no TickTick, diretamente via API REST ou MCP.

---

## ðŸ”Œ IntegraÃ§Ã£o com TickTick

### MÃ©todo de AutenticaÃ§Ã£o

O TickTick usa **OAuth2 Bearer Token** (token pessoal prÃ©-autorizado):

```
Authorization: Bearer tp_7972769ad0ca4d9c944f11d3170fb707
Content-Type: application/json
Base URL: https://api.ticktick.com/open/v1
```

> âš ï¸ Este token Ã© pessoal e jÃ¡ estÃ¡ autenticado. NÃ£o Ã© necessÃ¡rio nenhum fluxo OAuth adicional.

### ConfiguraÃ§Ã£o MCP (Antigravity)

O servidor MCP do TickTick estÃ¡ configurado em:
```
C:\Users\Lucas Emanuel\.gemini\antigravity\mcp_config.json
```

Com transporte **SSE**:
```json
{
  "mcpServers": {
    "ticktick": {
      "type": "sse",
      "url": "https://mcp.ticktick.com",
      "headers": {
        "Authorization": "Bearer tp_7972769ad0ca4d9c944f11d3170fb707"
      }
    }
  }
}
```

> â„¹ï¸ Se o MCP nÃ£o estiver disponÃ­vel na sessÃ£o atual, use a **API REST diretamente via PowerShell** (veja seÃ§Ã£o abaixo).

---

## ðŸ“ Projetos do TickTick (Mapeamento Completo)

| ID | Nome | Tipo | VisualizaÃ§Ã£o |
|----|------|------|-------------|
| `67f4f4115250f258ba2c5c07` | ðŸ’¼ Trabalho | TASK | list |
| `67f4f4c65250f258ba2c5c39` | ðŸ  Vida pessoal | TASK | list |
| `67f4f5015250f258ba2c5cbe` | ðŸ“š Estudos | TASK | kanban |
| `683330eb8f08e3d3eeca31f0` | ðŸ¤– Machine Learning | TASK | kanban |
| `68334f8cebcdf700000001fd` | ðŸ“ MatemÃ¡tica | TASK | kanban |
| `6859ebbeebcdf700000005a2` | ðŸŽ“ Curso Justin | TASK | kanban |
| `687ce2dfebcdf700000003f3` | ðŸ“ AnotaÃ§Ãµes - Curso Justin | NOTE | list |
| `68ab1930ebcdf7000000045f` | ðŸ§  Agentes de AI | TASK | kanban |
| `695be02febce9c00000000a0` | ðŸƒ Esportes | TASK | list |
| `695d1b59ebce9c0000000137` | ðŸ“‹ Vagas referÃªncia | NOTE | list |
| `69791c43ebce9c0000000359` | ðŸ”¨ Projetos | TASK | kanban |
| `69ce4ecd8f088767a27244a8` | ðŸŒ¿ Nelium | TASK | list |

### Colunas Kanban do Projeto MatemÃ¡tica

| ID | Nome |
|----|------|
| `68334fa9ebcdf70000000250` | Encoding |
| `68334fb0ebcdf70000000259` | Spacing |

---

## ðŸ› ï¸ Como Criar Tarefas via API REST (PowerShell)

### Estrutura Completa de uma Task

```powershell
$token = "tp_7972769ad0ca4d9c944f11d3170fb707"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

$task = @{
    title     = "TÃ­tulo da Tarefa"
    projectId = "68334f8cebcdf700000001fd"    # ID do projeto
    dueDate   = "2026-04-13T06:00:00.000+0000" # UTC (BRT = UTC-3, entÃ£o 06:00 UTC = 03:00 BRT = dia inteiro)
    startDate = "2026-04-13T06:00:00.000+0000" # Opcional
    priority  = 3                              # 0=None, 1=Low, 3=Medium, 5=High
    isAllDay  = $true                          # Tarefa de dia inteiro
    timeZone  = "America/Sao_Paulo"
    content   = "DescriÃ§Ã£o detalhada da tarefa"
    tags      = @("ia-gerado")                 # Array de strings
    columnId  = "68334fa9ebcdf70000000250"     # Opcional: coluna kanban
    kind      = "TEXT"                         # TEXT ou NOTE
} | ConvertTo-Json -Depth 3

$result = Invoke-RestMethod -Uri "https://api.ticktick.com/open/v1/task" -Headers $headers -Method POST -Body $task
Write-Host "Criada: $($result.id)"
```

### Endpoints DisponÃ­veis

| MÃ©todo | Endpoint | DescriÃ§Ã£o |
|--------|----------|-----------|
| `GET` | `/project` | Lista todos os projetos |
| `GET` | `/project/{projectId}/data` | Dados do projeto (tasks + colunas) |
| `GET` | `/project/{projectId}/task/{taskId}` | Busca task especÃ­fica |
| `POST` | `/task` | Cria nova task |
| `POST` | `/task/{taskId}` | Atualiza task existente |
| `DELETE` | `/project/{projectId}/task/{taskId}` | Deleta task |
| `POST` | `/project/{projectId}/task/{taskId}/complete` | Completa task |

### Campos da Task (Schema Completo)

```json
{
    "id":         "string (gerado automaticamente)",
    "projectId":  "string (obrigatÃ³rio)",
    "title":      "string (obrigatÃ³rio)",
    "content":    "string (descriÃ§Ã£o / corpo da tarefa)",
    "startDate":  "string ISO-8601 UTC",
    "dueDate":    "string ISO-8601 UTC",
    "timeZone":   "string (ex: America/Sao_Paulo)",
    "isAllDay":   "boolean",
    "priority":   "0 | 1 | 3 | 5",
    "status":     "0=ativo | 2=completo",
    "tags":       ["array", "de", "strings"],
    "columnId":   "string (kanban column ID)",
    "sortOrder":  "number",
    "kind":       "TEXT | NOTE",
    "items":      [{ "title": "...", "status": 0 }]
}
```

---

## ðŸ·ï¸ Tags PadrÃ£o

| Tag | Uso |
|-----|-----|
| `ia-gerado` | Qualquer tarefa criada por agente de IA |
| `revisao` | Tarefas de revisÃ£o/spaced repetition |
| `urgente` | Alta prioridade imediata |
| `gcal` | Sincronizado com Google Calendar |

> Ao criar qualquer tarefa via IA, **sempre inclua a tag `ia-gerado`**.

---

## ðŸ“… Metodologia de RevisÃ£o EspaÃ§ada (Spaced Repetition)

Quando o usuÃ¡rio pedir para criar tasks de revisÃ£o baseadas em um conteÃºdo estudado, seguir este padrÃ£o:

### Intervalos PadrÃ£o

| RevisÃ£o | Intervalo apÃ³s estudo | NÃ­vel | TÃ©cnicas |
|---------|----------------------|-------|----------|
| R1 | 2â€“3 dias | MÃ©dio | Brain Dump + QuestÃµes Misturadas |
| R2 | 5â€“10 dias apÃ³s R1 | MÃ©dioâ†’Alto | Ensinar + Comparar/Contrastar |
| R3 | 10â€“20 dias apÃ³s R2 | Alto | Modificar VariÃ¡veis + Criar QuestÃµes |
| R4 | 1â€“2 meses apÃ³s R3 | Alto | Estudo de Caso Multi-Conceito |

### Grupos de ConteÃºdo (Interleaving)

Organizar conteÃºdos em grupos para forÃ§ar conexÃµes:
- **Grupo A (Fundamentos)**: Conceitos base, definiÃ§Ãµes, fÃ³rmulas
- **Grupo B (Discreto/AplicaÃ§Ã£o A)**: Primeiro grupo de aplicaÃ§Ãµes
- **Grupo C (ContÃ­nuo/AplicaÃ§Ã£o B)**: Segundo grupo de aplicaÃ§Ãµes  
- **Grupo D (IntegraÃ§Ã£o)**: Conceitos de ordem superior / inferÃªncia

---

## ðŸ”„ Fluxo de Trabalho para Criar Tasks de RevisÃ£o

Quando receber um prompt pedindo tasks de revisÃ£o:

1. **Identificar os grupos de conteÃºdo** no material fornecido
2. **Calcular as datas** a partir da data atual:
   - R1: hoje + 2 ou 3 dias
   - R2: R1 + 7 dias (ponto mÃ©dio de 5â€“10)
   - R3: R2 + 15 dias (ponto mÃ©dio de 10â€“20)
   - R4: R3 + 45 dias (ponto mÃ©dio de 1â€“2 meses)
3. **Criar as tasks via API REST** com o template abaixo
4. **Confirmar** os IDs e datas criados

### Template de Task de RevisÃ£o

```
TÃ­tulo: "ðŸ“Š RevisÃ£o N â€“ [Assunto]: [TÃ©cnica Principal]"

ConteÃºdo:
ðŸŽ¯ NÃVEL [MÃ‰DIO|ALTO] â€“ Foco em [relaÃ§Ãµes|integraÃ§Ã£o|modificaÃ§Ã£o]

ðŸ“Œ TÃ‰CNICAS:
â€¢ [TÃ©cnica 1]
â€¢ [TÃ©cnica 2]

ðŸ“‹ AÃ‡Ã•ES:
1. [AÃ§Ã£o especÃ­fica com detalhes]
2. [AÃ§Ã£o especÃ­fica com detalhes]

ðŸ§  OBJETIVO: [Objetivo cognitivo claro]

ðŸ·ï¸ Grupos de ConteÃºdo:
â€¢ Grupo A: [...]
â€¢ Grupo B: [...]
â€¢ Grupo C: [...]
â€¢ Grupo D: [...]
```

---

## âš™ï¸ ConfiguraÃ§Ã£o .gemini/settings.json (por workspace)

Para workspaces que usam o Gemini CLI localmente:

```json
{
  "mcpServers": {
    "ticktick": {
      "type": "sse",
      "url": "https://mcp.ticktick.com",
      "headers": {
        "Authorization": "Bearer tp_7972769ad0ca4d9c944f11d3170fb707"
      }
    }
  }
}
```

Salvar em: `<workspace>/.gemini/settings.json`

---

## ðŸš¨ Regras para Agentes

1. **Sempre use a tag `ia-gerado`** em qualquer task criada por IA
2. **Datas em UTC**: o fuso do usuÃ¡rio Ã© `America/Sao_Paulo` (UTC-3). Para tarefas de dia inteiro, use `06:00:00.000+0000` (meia-noite em BRT)
3. **Projeto padrÃ£o para estudos**: `ðŸ“ MatemÃ¡tica` (`68334f8cebcdf700000001fd`) ou `ðŸ“š Estudos` (`67f4f5015250f258ba2c5cbe`)
4. **Priority 3** (Medium) Ã© o padrÃ£o para revisÃµes. Use **5** (High) apenas se urgente
5. **Em caso de erro no MCP**, use sempre a API REST via PowerShell como fallback
6. **NÃ£o criar tasks duplicadas**: verificar `/project/{id}/data` antes de criar
7. **Encoding de caracteres**: a API aceita UTF-8, mas PowerShell pode precisar de `-Encoding UTF8` em exports


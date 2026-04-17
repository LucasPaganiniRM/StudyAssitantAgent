# StudyAgentMD – Instruções para Agentes de IA

> Este arquivo é reconhecido automaticamente por: **Claude** (CLAUDE.md), **Gemini** (GEMINI.md), **Cursor** (.cursorrules), **Windsurf**, **Copilot** e qualquer agente compatível com o padrão `AGENTS.md`.

---

## 🎯 Propósito deste Workspace

Este é o workspace **StudyAgentMD** — um hub centralizado para , automatizar e documentar tarefas de estudo usando o **TickTick** como sistema de produtividade pessoal do usuário (Lucas Emanuel).

O foco principal é criar e gerenciar **tarefas de revisão espaçada** (*spaced repetition*) com técnicas de *interleaving* no TickTick, diretamente via API REST ou MCP.

---

## 🔌 Integração com TickTick

### Método de Autenticação

O TickTick usa **OAuth2 Bearer Token** (token pessoal pré-autorizado).
> 🚨 **REGRA DE SEGURANÇA PARA AGENTES:** NUNCA escreva o token diretamente hardcoded sob hipótese alguma. Você deve sempre buscar o token nas variáveis de ambiente do sistema (`$env:TICKTICK_API_TOKEN`). O token sensitivo está salvo no diretório raiz dentro do arquivo `.env`.

```
Authorization: Bearer <TICKTICK_API_TOKEN>
Content-Type: application/json
Base URL: https://api.ticktick.com/open/v1
```

> ⚠️ Este token é pessoal e já está autenticado. Não é necessário nenhum fluxo OAuth adicional.

### Configuração MCP (Antigravity)

O servidor MCP do TickTick está configurado em:
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
        "Authorization": "Bearer <TICKTICK_API_TOKEN>"
      }
    }
  }
}
```

> ℹ️ Se o MCP não estiver disponível na sessão atual, use a **API REST diretamente via PowerShell** (veja seção abaixo).

---

## 📁 Projetos do TickTick (Mapeamento Completo)

| ID | Nome | Tipo | Visualização |
|----|------|------|-------------|
| `67f4f5015250f258ba2c5cbe` | 📚 Estudos | TASK | kanban |
| `683330eb8f08e3d3eeca31f0` | 🤖 Machine Learning | TASK | kanban |
| `68334f8cebcdf700000001fd` | 📐 Matemática | TASK | kanban |
| `6859ebbeebcdf700000005a2` | 🎓 Curso Justin | TASK | kanban |
| `687ce2dfebcdf700000003f3` | 📝 Anotações - Curso Justin | NOTE | list |
| `68ab1930ebcdf7000000045f` | 🧠 Agentes de AI | TASK | kanban |


### Colunas Kanban do Projeto Matemática

| ID | Nome |
|----|------|
| `68334fa9ebcdf70000000250` | Encoding |
| `68334fb0ebcdf70000000259` | Spacing |

---

## 🛠️ Como Criar Tarefas via API REST (PowerShell)

### Estrutura Completa de uma Task

```powershell
$token = $env:TICKTICK_API_TOKEN
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

$task = @{
    title     = "Título da Tarefa"
    projectId = "68334f8cebcdf700000001fd"    # ID do projeto
    dueDate   = "2026-04-13T06:00:00.000+0000" # UTC (BRT = UTC-3, então 06:00 UTC = 03:00 BRT = dia inteiro)
    startDate = "2026-04-13T06:00:00.000+0000" # Opcional
    priority  = 3                              # 0=None, 1=Low, 3=Medium, 5=High
    isAllDay  = $true                          # Tarefa de dia inteiro
    timeZone  = "America/Sao_Paulo"
    content   = "Descrição detalhada da tarefa"
    tags      = @("ia-gerado")                 # Array de strings
    columnId  = "68334fa9ebcdf70000000250"     # Opcional: coluna kanban
    kind      = "TEXT"                         # TEXT ou NOTE
} | ConvertTo-Json -Depth 3

$result = Invoke-RestMethod -Uri "https://api.ticktick.com/open/v1/task" -Headers $headers -Method POST -Body $task
Write-Host "Criada: $($result.id)"
```

### Endpoints Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/project` | Lista todos os projetos |
| `GET` | `/project/{projectId}/data` | Dados do projeto (tasks + colunas) |
| `GET` | `/project/{projectId}/task/{taskId}` | Busca task específica |
| `POST` | `/task` | Cria nova task |
| `POST` | `/task/{taskId}` | Atualiza task existente |
| `DELETE` | `/project/{projectId}/task/{taskId}` | Deleta task |
| `POST` | `/project/{projectId}/task/{taskId}/complete` | Completa task |

### Campos da Task (Schema Completo)

```json
{
    "id":         "string (gerado automaticamente)",
    "projectId":  "string (obrigatório)",
    "title":      "string (obrigatório)",
    "content":    "string (descrição / corpo da tarefa)",
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

## 🏷️ Tags Padrão

| Tag | Uso |
|-----|-----|
| `ia-gerado` | Qualquer tarefa criada por agente de IA |
| `revisao` | Tarefas de revisão/spaced repetition |
| `urgente` | Alta prioridade imediata |
| `gcal` | Sincronizado com Google Calendar |

> Ao criar qualquer tarefa via IA, **sempre inclua a tag `ia-gerado`**.

---

## 📅 Metodologia de Revisão Espaçada (Spaced Repetition)

> **📖 Base de Conhecimento:** Consulte SEMPRE o arquivo `INTERLEAVING_REFERENCE.md` neste repositório para aprofundar seu entendimento sobre Níveis de Maestria e escolher a Técnica de Interleaving e Retrieval ideal baseada no tipo de conhecimento (Declarativo vs Procedimental).

Quando o usuário pedir para criar tasks de revisão baseadas em um conteúdo estudado, seguir este padrão:

### Intervalos Padrão

| Revisão | Intervalo após estudo | Nível | Técnicas |
|---------|----------------------|-------|----------|
| R1 | 2–3 dias | Médio | Brain Dump + Questões Misturadas |
| R2 | 5–10 dias após R1 | Médio→Alto | Ensinar + Comparar/Contrastar |
| R3 | 10–20 dias após R2 | Alto | Modificar Variáveis + Criar Questões |
| R4 | 1–2 meses após R3 | Alto | Estudo de Caso Multi-Conceito |

### Grupos de Conteúdo (Interleaving)

Organizar conteúdos em grupos para forçar conexões:
- **Grupo A (Fundamentos)**: Conceitos base, definições, fórmulas
- **Grupo B (Discreto/Aplicação A)**: Primeiro grupo de aplicações
- **Grupo C (Contínuo/Aplicação B)**: Segundo grupo de aplicações  
- **Grupo D (Integração)**: Conceitos de ordem superior / inferência

---

## 🔄 Fluxo de Trabalho para Criar Tasks de Revisão

Quando receber um prompt pedindo tasks de revisão:

1. **Identificar os grupos de conteúdo** no material fornecido
2. **Calcular as datas** a partir da data atual:
   - R1: hoje + 2 ou 3 dias
   - R2: R1 + 7 dias (ponto médio de 5–10)
   - R3: R2 + 15 dias (ponto médio de 10–20)
   - R4: R3 + 45 dias (ponto médio de 1–2 meses)
3. **Criar as tasks via API REST** com o template abaixo
4. **Confirmar** os IDs e datas criados

### Template de Task de Revisão

```
Título: "📊 Revisão N – [Assunto]: [Técnica Principal]"

Conteúdo:
🎯 NÍVEL [MÉDIO|ALTO] – Foco em [relações|integração|modificação]

📌 TÉCNICAS:
• [Técnica 1]
• [Técnica 2]

📋 AÇÕES:
1. [Ação específica com detalhes]
2. [Ação específica com detalhes]

🧠 OBJETIVO: [Objetivo cognitivo claro]

🏷️ Grupos de Conteúdo:
• Grupo A: [...]
• Grupo B: [...]
• Grupo C: [...]
• Grupo D: [...]
```

---

## ⚙️ Configuração .gemini/settings.json (por workspace)

Para workspaces que usam o Gemini CLI localmente:

```json
{
  "mcpServers": {
    "ticktick": {
      "type": "sse",
      "url": "https://mcp.ticktick.com",
      "headers": {
        "Authorization": "Bearer <TICKTICK_API_TOKEN>"
      }
    }
  }
}
```

Salvar em: `<workspace>/.gemini/settings.json`

---

## 🚨 Regras para Agentes

1. **Sempre use a tag `ia-gerado`** em qualquer task criada por IA
2. **Datas em UTC**: o fuso do usuário é `America/Sao_Paulo` (UTC-3). Para tarefas de dia inteiro, use `06:00:00.000+0000` (meia-noite em BRT)
3. **Projeto padrão para estudos**: `📐 Matemática` (`68334f8cebcdf700000001fd`) ou `📚 Estudos` (`67f4f5015250f258ba2c5cbe`)
4. **Priority 3** (Medium) é o padrão para revisões. Use **5** (High) apenas se urgente
5. **Em caso de erro no MCP**, use sempre a API REST via PowerShell como fallback
6. **Não criar tasks duplicadas**: verificar `/project/{id}/data` antes de criar
7. **Encoding de caracteres**: a API aceita UTF-8, mas PowerShell pode precisar de `-Encoding UTF8` em exports

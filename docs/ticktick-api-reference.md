# TickTick API – Referência Técnica

## Autenticação

```
Authorization: Bearer <TICKTICK_API_TOKEN>
Content-Type: application/json
Base URL: https://api.ticktick.com/open/v1
```

> Token OAuth2 pessoal pré-autorizado. Não requer fluxo adicional.

---

## Endpoints

### Projetos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/project` | Lista todos os projetos |
| `GET` | `/project/{projectId}/data` | Projeto com tasks e colunas kanban |

### Tasks

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/project/{projectId}/task/{taskId}` | Busca task específica |
| `POST` | `/task` | Cria nova task |
| `POST` | `/task/{taskId}` | Atualiza task existente |
| `DELETE` | `/project/{projectId}/task/{taskId}` | Deleta task |
| `POST` | `/project/{projectId}/task/{taskId}/complete` | Marca task como completa |

> ⚠️ Endpoint `/tag` retorna 404 — tags são gerenciadas inline no campo `tags` da task.

---

## Schema da Task

```json
{
  "id":         "string — gerado automaticamente pela API",
  "projectId":  "string — OBRIGATÓRIO",
  "title":      "string — OBRIGATÓRIO",
  "content":    "string — corpo/descrição da tarefa (suporta quebras de linha com \\n)",
  "startDate":  "string — ISO-8601 UTC, ex: '2026-04-13T06:00:00.000+0000'",
  "dueDate":    "string — ISO-8601 UTC, ex: '2026-04-13T06:00:00.000+0000'",
  "timeZone":   "string — ex: 'America/Sao_Paulo'",
  "isAllDay":   "boolean — true para tarefas de dia inteiro",
  "priority":   "0=None | 1=Low | 3=Medium | 5=High",
  "status":     "0=ativo | 2=completo",
  "tags":       ["array", "de", "strings"],
  "columnId":   "string — ID da coluna kanban (opcional)",
  "sortOrder":  "number — posição na lista (opcional)",
  "kind":       "TEXT | NOTE",
  "items":      [{ "title": "subtarefa", "status": 0 }]
}
```

---

## Projetos Disponíveis

| ID | Emoji | Nome | Tipo | View |
|----|-------|------|------|------|
| `67f4f4115250f258ba2c5c07` | 💼 | Trabalho | TASK | list |
| `67f4f4c65250f258ba2c5c39` | 🏠 | Vida pessoal | TASK | list |
| `67f4f5015250f258ba2c5cbe` | 📚 | Estudos | TASK | kanban |
| `683330eb8f08e3d3eeca31f0` | 🤖 | Machine Learning | TASK | kanban |
| `68334f8cebcdf700000001fd` | 📐 | Matemática | TASK | kanban |
| `6837ad838f08514b10eec316` | 🍽️ | Receitas | NOTE | kanban |
| `6859ebbeebcdf700000005a2` | 🎓 | Curso Justin | TASK | kanban |
| `687ce2dfebcdf700000003f3` | 📝 | Anotações - Curso Justin | NOTE | list |
| `68ab1930ebcdf7000000045f` | 🧠 | Agentes de AI | TASK | kanban |
| `695be02febce9c00000000a0` | 🏃 | Esportes | TASK | list |
| `695d1b59ebce9c0000000137` | 📋 | Vagas referência | NOTE | list |
| `69791c43ebce9c0000000359` | 🔨 | Projetos | TASK | kanban |
| `69ce4ecd8f088767a27244a8` | 🌿 | Nelium | TASK | list |

---

## Colunas Kanban por Projeto

### 📐 Matemática (`68334f8cebcdf700000001fd`)

| ID | Nome | Ordem |
|----|------|-------|
| `68334fa9ebcdf70000000250` | Encoding | 0 |
| `68334fb0ebcdf70000000259` | Spacing | 268435456 |

---

## Exemplos PowerShell

### Criar Task Simples

```powershell
$token = $env:TICKTICK_API_TOKEN
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

$body = @{
    title     = "Minha Tarefa"
    projectId = "67f4f5015250f258ba2c5cbe"
    dueDate   = "2026-04-15T06:00:00.000+0000"
    isAllDay  = $true
    timeZone  = "America/Sao_Paulo"
    priority  = 3
    tags      = @("ia-gerado")
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri "https://api.ticktick.com/open/v1/task" `
    -Headers $headers -Method POST -Body $body
```

### Listar Projetos

```powershell
$token = $env:TICKTICK_API_TOKEN
$headers = @{ "Authorization" = "Bearer $token"; "Content-Type" = "application/json" }

Invoke-RestMethod -Uri "https://api.ticktick.com/open/v1/project" `
    -Headers $headers -Method GET
```

### Buscar Tasks de um Projeto

```powershell
$projectId = "68334f8cebcdf700000001fd"
$data = Invoke-RestMethod `
    -Uri "https://api.ticktick.com/open/v1/project/$projectId/data" `
    -Headers $headers -Method GET

$data.tasks | Select-Object id, title, dueDate, status
```

### Atualizar Task Existente

```powershell
$taskId = "ID_DA_TASK"
$update = @{
    title    = "Novo Título"
    priority = 5
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri "https://api.ticktick.com/open/v1/task/$taskId" `
    -Headers $headers -Method POST -Body $update
```

### Deletar Task

```powershell
$projectId = "68334f8cebcdf700000001fd"
$taskId    = "ID_DA_TASK"

Invoke-RestMethod `
    -Uri "https://api.ticktick.com/open/v1/project/$projectId/task/$taskId" `
    -Headers $headers -Method DELETE
```

### Completar Task

```powershell
Invoke-RestMethod `
    -Uri "https://api.ticktick.com/open/v1/project/$projectId/task/$taskId/complete" `
    -Headers $headers -Method POST
```

---

## Notas de Comportamento da API

| Comportamento | Detalhe |
|--------------|---------|
| **Datas** | Sempre em UTC. BRT = UTC-3, então meia-noite BRT = `06:00:00.000+0000` |
| **Tags** | Não há endpoint `/tag`. Gerenciar inline no campo `tags[]` da task |
| **Encoding** | API aceita UTF-8. PowerShell pode exibir emojis como `?` mas salva corretamente |
| **isAllDay** | Quando `true`, a hora da data é ignorada pelo TickTick |
| **columnId** | Só funciona em projetos com `viewMode: kanban` |
| **kind** | `TEXT` = tarefa comum; `NOTE` = nota/documento |
| **Inbox** | Acessível via `project/inbox/data` (sem ID numérico) |

---

## MCP TickTick

### O que é MCP

O **Model Context Protocol (MCP)** permite que agentes de IA se conectem ao TickTick usando ferramentas nativas, sem precisar escrever chamadas HTTP manualmente.

### Configuração SSE

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

### Onde configurar

| Ferramenta | Arquivo de config |
|-----------|-------------------|
| Antigravity (Gemini) | `C:\Users\Lucas Emanuel\.gemini\antigravity\mcp_config.json` |
| Gemini CLI (por workspace) | `<workspace>/.gemini/settings.json` |
| Claude Desktop | `%APPDATA%\Claude\claude_desktop_config.json` |

### Como instalar via Gemini CLI

```bash
gemini mcp add --transport sse \
  -H "Authorization: Bearer $TICKTICK_API_TOKEN" \
  ticktick https://mcp.ticktick.com
```

### Ferramentas disponíveis via MCP

Quando o MCP está ativo, o agente pode usar ferramentas como:
- `mcp_ticktick_list_tasks` — lista tarefas de um projeto
- `mcp_ticktick_create_task` — cria nova tarefa
- `mcp_ticktick_update_task` — atualiza tarefa existente
- `mcp_ticktick_complete_task` — completa tarefa
- `mcp_ticktick_delete_task` — deleta tarefa

> Se o MCP não estiver disponível na sessão, use sempre a API REST via PowerShell como fallback.

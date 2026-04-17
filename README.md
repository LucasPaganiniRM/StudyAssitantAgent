# StudyAgentMD

> Hub centralizado para gerenciar tarefas de estudo com **revisão espaçada** (*spaced repetition*) e *interleaving* via **TickTick**.

---

## 🗂️ Estrutura do Workspace

```
StudyAgentMD/
├── AGENTS.md                         ← Instruções para todos os agentes de IA
├── CLAUDE.md                         ← Alias → AGENTS.md (Claude)
├── GEMINI.md                         ← Alias → AGENTS.md (Gemini CLI)
├── .cursorrules                      ← Alias → AGENTS.md (Cursor)
├── .github/
│   └── copilot-instructions.md      ← Alias → AGENTS.md (GitHub Copilot)
├── .gemini/
│   └── settings.json                ← MCP TickTick para Gemini CLI
├── docs/
│   ├── ticktick-api-reference.md    ← Referência técnica da API REST
│   └── spaced-repetition-method.md ← Metodologia de revisão espaçada
└── README.md                        ← Este arquivo
```

---

## ⚡ Início Rápido

### Criar uma Task de Revisão via PowerShell

```powershell
$token = $env:TICKTICK_API_TOKEN
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

$task = @{
    title     = "📊 Revisão 1 – Meu Assunto: Brain Dump"
    projectId = "68334f8cebcdf700000001fd"   # Matemática
    dueDate   = "2026-04-13T06:00:00.000+0000"
    priority  = 3
    isAllDay  = $true
    timeZone  = "America/Sao_Paulo"
    content   = "Conteúdo detalhado da revisão..."
    tags      = @("ia-gerado", "revisao")
} | ConvertTo-Json -Depth 3

$result = Invoke-RestMethod `
    -Uri "https://api.ticktick.com/open/v1/task" `
    -Headers $headers -Method POST -Body $task

Write-Host "Criada: $($result.id)"
```

---

## 🤖 Compatibilidade com Agentes de IA

| Agente | Arquivo lido | Status |
|--------|-------------|--------|
| Claude (Anthropic) | `CLAUDE.md` | ✅ |
| Gemini (Google) | `GEMINI.md` | ✅ |
| Antigravity | `AGENTS.md` | ✅ |
| Cursor | `.cursorrules` | ✅ |
| GitHub Copilot | `.github/copilot-instructions.md` | ✅ |
| Windsurf | `AGENTS.md` | ✅ |

---

## 🔗 Links Úteis

- [TickTick API Docs](https://developer.ticktick.com/api)
- [MCP TickTick Server](https://mcp.ticktick.com)
- Ver `docs/ticktick-api-reference.md` para referência completa
- Ver `docs/spaced-repetition-method.md` para a metodologia

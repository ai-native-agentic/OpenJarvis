# EXAMPLES — OpenJarvis Use Case Demonstrations

9 standalone examples showing OpenJarvis SDK patterns: browser automation, code assistance, research, scheduling, security scanning, messaging, and multi-model routing.

## STRUCTURE

```
examples/
├── browser_assistant/           # Web browsing agent with orchestrator loop
│   ├── browser_assistant.py     # CLI: --query, --model, --engine, --max-turns
│   └── README.md
├── code_companion/              # Code review, test generation, debugging
│   ├── reviewer.py              # Git diff review with ReAct agent
│   ├── test_gen.py              # Automated test generation
│   ├── debugger.py              # Interactive debugging assistant
│   └── README.md
├── daily_digest/                # Daily summary agent
│   ├── daily_digest.py          # Aggregates news, calendar, tasks
│   └── README.md
├── deep_research/               # Multi-source research agent
│   ├── research.py              # Web + paper search, synthesis
│   ├── research.toml            # Research config (sources, depth)
│   └── README.md
├── doc_qa/                      # Document Q&A with RAG
│   ├── doc_qa.py                # PDF/Markdown indexing + retrieval
│   └── README.md
├── messaging_hub/               # Smart inbox assistant
│   ├── smart_inbox.py           # Email/Slack triage and response
│   └── README.md
├── multi_model_router/          # Multi-model orchestration
│   ├── multi_model_router.py    # Route queries to best model (local vs cloud)
│   └── README.md
├── scheduled_ops/               # Scheduled task automation
│   ├── daily_digest.py          # Morning briefing
│   ├── code_review.py           # Nightly PR review
│   ├── gym_scheduler.py         # Workout reminders
│   ├── schedules.toml           # Cron-like schedule config
│   └── README.md
└── security_scanner/            # Security audit agent
    ├── security_scanner.py      # Dependency scan, CVE check, code audit
    └── README.md
```

## WHERE TO LOOK

| Use Case | Example | Key Pattern |
|----------|---------|-------------|
| Web research | `browser_assistant/` | Orchestrator loop, web search + navigation |
| Code review | `code_companion/reviewer.py` | Git diff parsing, ReAct agent, Click CLI |
| Test generation | `code_companion/test_gen.py` | AST analysis, test template generation |
| Debugging | `code_companion/debugger.py` | Interactive REPL, stack trace analysis |
| Research synthesis | `deep_research/` | Multi-source search, citation tracking |
| Document Q&A | `doc_qa/` | RAG pipeline (FAISS/ColBERT + PDF) |
| Email triage | `messaging_hub/` | NLP classification, auto-response |
| Model routing | `multi_model_router/` | Cost/latency optimization, fallback logic |
| Scheduled tasks | `scheduled_ops/` | TOML config, cron-like scheduling |
| Security audit | `security_scanner/` | Dependency scan, CVE lookup, SAST |

## CONVENTIONS

**CLI pattern**: All examples use `argparse` or `click` for CLI. Common flags: `--model`, `--engine`, `--max-turns`.

**Config files**: TOML for structured config (`research.toml`, `schedules.toml`). YAML for agent-specific settings.

**Default model**: `qwen3:8b` via Ollama. Override with `--model gpt-4o --engine cloud` for cloud fallback.

**Execution loop**: Most examples use `agent.run(request)` with `max_steps` termination. Browser and research agents use custom orchestrator loops.

**Memory backends**: Examples use FAISS (vector), ColBERT (neural), or BM25 (sparse) depending on use case. Config in TOML.

**Error handling**: All examples catch `KeyboardInterrupt` for graceful shutdown. Log errors to stderr.

## ANTI-PATTERNS

| Forbidden | Why |
|-----------|-----|
| Hardcoding API keys | Use env vars or config files |
| Skipping `--help` documentation | Examples are teaching tools |
| Infinite loops without max_steps | Examples must terminate |
| Committing large test files | Use fixtures or download on demand |
| Cross-example imports | Each example is standalone |

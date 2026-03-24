# OPENJARVIS — LOCAL-FIRST AI FRAMEWORK

**Branch:** main | **Commit:** f228b0f

## OVERVIEW

OpenJarvis is a local-first AI framework built around three core ideas: shared primitives for on-device agents, evaluations treating energy/FLOPs/latency/cost as first-class constraints, and a learning loop improving models via local trace data. The goal is simple: make personal AI agents run locally by default, calling the cloud only when necessary.

**Architecture**: Python + Rust 19 crates, 180K LOC, 1231 files. Maturin bridges Python to Rust via `_rust_bridge.py`. 28 modules span core registry, engine, agents, channels, tools, learning, skills, MCP, A2A, and evals. FastAPI server handles HTTP. Channels include Telegram, Discord, Slack, Line, Viber. Memory backends: FAISS, ColBERT, BM25, PDF. Config via YAML + Pydantic with `OPENJARVIS_*` env vars.

**Research platform and production foundation**: Designed in the spirit of PyTorch, balancing research flexibility with production readiness. Intelligence Per Watt research showed local models handle 88.7% of single-turn chat/reasoning queries with 5.3× efficiency improvement from 2023 to 2025.

## STRUCTURE

```
OpenJarvis/
├── src/openjarvis/
│   ├── __init__.py              # SDK exports: Jarvis, JarvisSystem, MemoryHandle, SystemBuilder
│   ├── sdk.py                   # High-level API surface
│   ├── core/
│   │   ├── registry.py          # Decorator-based component discovery (agents, engines, memory)
│   │   └── config.py            # YAML + Pydantic config loader
│   ├── engine/                  # Inference engines (Ollama, vLLM, SGLang, llama.cpp)
│   ├── agents/                  # Agent implementations
│   ├── channels/                # Multi-platform messaging (Telegram, Discord, Slack, Line, Viber)
│   ├── tools/                   # Tool registry and implementations
│   │   └── storage/             # Memory backends (FAISS, ColBERT, BM25, PDF)
│   ├── learning/                # Local trace-based learning loop
│   ├── skills/                  # Skill definitions
│   ├── mcp/                     # Model Context Protocol integration
│   ├── a2a/                     # Agent-to-Agent protocol
│   ├── evals/                   # Evaluation harness (11 subdirs)
│   └── _rust_bridge.py          # Maturin Python-Rust bridge
├── rust/crates/                 # 19 Rust crates
│   └── openjarvis-python/       # Maturin build target
├── tests/                       # Test suite
├── docs/                        # MkDocs documentation
├── pyproject.toml               # uv project config
└── Cargo.toml                   # Rust workspace manifest
```

## WHERE TO LOOK

| Task | File/Directory | Notes |
|------|----------------|-------|
| SDK entry point | `src/openjarvis/__init__.py` | Exports Jarvis, JarvisSystem, MemoryHandle, SystemBuilder |
| Component registry | `src/openjarvis/core/registry.py` | Decorator-based discovery for agents, engines, memory backends |
| Config management | `src/openjarvis/core/config.py` | YAML + Pydantic, `OPENJARVIS_*` env vars |
| Inference engines | `src/openjarvis/engine/` | Ollama, vLLM, SGLang, llama.cpp adapters |
| Agent implementations | `src/openjarvis/agents/` | Agent logic and orchestration |
| Messaging channels | `src/openjarvis/channels/` | Telegram, Discord, Slack, Line, Viber integrations |
| Memory backends | `src/openjarvis/tools/storage/` | FAISS, ColBERT, BM25, PDF indexing |
| Learning loop | `src/openjarvis/learning/` | Local trace-based model improvement |
| MCP integration | `src/openjarvis/mcp/` | Model Context Protocol support |
| A2A protocol | `src/openjarvis/a2a/` | Agent-to-Agent communication |
| Evaluation suite | `src/openjarvis/evals/` | 11 evaluation modules |
| Rust bridge | `src/openjarvis/_rust_bridge.py` | Maturin Python-Rust FFI |
| Rust crates | `rust/crates/` | 19 crates, security, tools, agents |
| FastAPI server | `src/openjarvis/server/` | HTTP API (requires `--extra server`) |

## CONVENTIONS

**Python**: 3.10+ required. Use `uv sync` for core, `uv sync --extra server` for FastAPI, `uv sync --extra dev` for development. Decorator-based registry pattern for all pluggable components (agents, engines, memory). YAML config files with Pydantic validation. Environment variables prefixed `OPENJARVIS_*`.

**Rust**: Edition 2021, maturin for Python bindings. Build with `uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml`. 19 crates provide security, tools, and agent primitives. Rust toolchain required for full functionality.

**Testing**: `uv run pytest tests/ -v` for Python tests. Rust tests via `cargo test` in workspace.

**Config**: YAML files in project root or `~/.openjarvis/`. Pydantic models validate structure. Override via `OPENJARVIS_*` env vars.

**Hardware detection**: `uv run jarvis init` auto-detects hardware and recommends best engine. `uv run jarvis doctor` diagnoses config/connectivity issues.

**Local-first design**: Default to local inference backends. Cloud calls only when necessary. Energy, FLOPs, latency, and cost are first-class evaluation metrics.

## ANTI-PATTERNS

| Forbidden | Why |
|-----------|-----|
| Hardcoded cloud API calls | Violates local-first principle; use engine abstraction |
| Skipping hardware detection | `jarvis init` ensures optimal engine selection |
| Ignoring energy/latency metrics | Core design constraint, not optional |
| Direct registry mutation | Use `@register` decorator or `register_value()` |
| Bypassing Pydantic config | Type safety and validation required |
| Missing Rust toolchain | Full functionality requires Rust extension |
| Committing model artifacts | Large binary churn, usually generated |
| Skipping `jarvis doctor` | Diagnostic tool catches config/connectivity issues early |

## COMMANDS

```bash
# Installation
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
uv sync                           # core framework
uv sync --extra server            # + FastAPI server
uv sync --extra dev               # + development tools

# Development (requires Rust)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml

# Setup and diagnostics
uv run jarvis init                # detect hardware, generate config
uv run jarvis doctor              # diagnose config/connectivity

# Usage
uv run jarvis ask "What is the capital of France?"

# Testing
uv run pytest tests/ -v           # Python tests
cargo test                        # Rust tests (in workspace)

# Local inference backend (example: Ollama)
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
ollama pull qwen3:8b
```

## NOTES

**Maturin bridge**: Python calls Rust via `_rust_bridge.py`. Build with `maturin develop`. Requires Rust toolchain for full functionality (security, tools, agents).

**Registry pattern**: All pluggable components (agents, engines, memory backends) use decorator-based discovery via `core/registry.py`. Each typed subclass gets isolated storage.

**Local-first philosophy**: 88.7% of single-turn chat/reasoning queries handled locally (Intelligence Per Watt research). Cloud calls only when necessary. Energy, FLOPs, latency, and cost are first-class constraints.

**Inference backends**: Supports Ollama, vLLM, SGLang, llama.cpp. `jarvis init` auto-detects hardware and recommends best engine.

**Memory backends**: FAISS for vector search, ColBERT for neural retrieval, BM25 for sparse retrieval, PDF for document indexing.

**Channels**: Multi-platform messaging via Telegram, Discord, Slack, Line, Viber. FastAPI server requires `--extra server`.

**Research platform**: Designed for both research and production. Clean, modular architecture. Learning loop improves models via local trace data.

**Stanford affiliation**: Developed at Hazy Research and Scaling Intelligence Lab at Stanford SAIL. Part of Intelligence Per Watt research initiative.

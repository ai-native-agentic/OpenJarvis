# FRONTEND — React + Tauri Chat Interface

Tauri v2 desktop application with React 19, TypeScript, Vite, and shadcn/ui components.

## STRUCTURE

```
frontend/
├── src/
│   ├── App.tsx                  # Root component, routing
│   ├── main.tsx                 # React entry point
│   ├── components/
│   │   ├── Chat/                # Chat interface components
│   │   ├── Dashboard/           # Dashboard widgets
│   │   ├── Sidebar/             # Navigation sidebar
│   │   ├── ui/                  # shadcn/ui primitives
│   │   ├── CommandPalette.tsx   # Keyboard-driven command interface
│   │   ├── ErrorBoundary.tsx    # React error boundary
│   │   ├── Layout.tsx           # App layout wrapper
│   │   ├── OptInModal.tsx       # Onboarding/consent modal
│   │   ├── SetupScreen.tsx      # Initial setup flow
│   │   └── SystemPulse.tsx      # System status indicator
│   ├── pages/
│   │   ├── AgentsPage.tsx       # Agent management UI
│   │   ├── ChatPage.tsx         # Main chat interface
│   │   ├── DashboardPage.tsx    # Overview dashboard
│   │   ├── GetStartedPage.tsx   # Onboarding page
│   │   ├── LogsPage.tsx         # System logs viewer
│   │   └── SettingsPage.tsx     # Configuration UI
│   ├── hooks/                   # React hooks (state, effects)
│   ├── lib/                     # Utilities, helpers
│   └── types/                   # TypeScript type definitions
├── src-tauri/                   # Tauri Rust backend
│   ├── src/                     # Rust IPC handlers
│   ├── Cargo.toml               # Rust dependencies
│   └── tauri.conf.json          # Tauri app config
├── public/                      # Static assets
├── package.json                 # npm dependencies
└── vite.config.ts               # Vite build config
```

## WHERE TO LOOK

| Task | File/Directory | Notes |
|------|----------------|-------|
| Chat UI | `src/components/Chat/` | Message rendering, input, streaming |
| Agent management | `src/pages/AgentsPage.tsx` | Agent list, install, configure |
| Dashboard widgets | `src/components/Dashboard/` | System metrics, recent activity |
| Command palette | `src/components/CommandPalette.tsx` | Keyboard shortcuts (Cmd+K) |
| Settings UI | `src/pages/SettingsPage.tsx` | Model config, API keys, preferences |
| Tauri IPC | `src-tauri/src/` | Rust handlers for system calls |
| Routing | `src/App.tsx` | React Router v7 routes |
| State hooks | `src/hooks/` | Zustand stores, custom hooks |
| UI primitives | `src/components/ui/` | shadcn/ui components |

## CONVENTIONS

**React 19**: Use new hooks (`useTransition`, `useDeferredValue`). Avoid legacy patterns.

**Tauri IPC**: Call Rust backend via `@tauri-apps/api/core` `invoke()`. All system operations (file I/O, process spawn) go through Tauri.

**Styling**: Tailwind CSS v4 with `@tailwindcss/vite`. Use `cn()` helper from `lib/utils.ts` for conditional classes.

**State management**: Zustand for global state. React Context for component trees. Avoid prop drilling.

**Error handling**: Wrap async boundaries with `ErrorBoundary.tsx`. Show user-friendly messages.

**Markdown rendering**: `react-markdown` with `remark-gfm`, `remark-math`, `rehype-katex`, `rehype-highlight` for code blocks.

## ANTI-PATTERNS

| Forbidden | Why |
|-----------|-----|
| Direct Node.js APIs (fs, child_process) | Use Tauri IPC instead (security sandbox) |
| Inline styles | Use Tailwind classes or CSS modules |
| Uncontrolled components for forms | Controlled inputs required for state sync |
| Skipping ErrorBoundary | Crashes leak to user without recovery |
| Hardcoded API keys in frontend | Use Tauri secure storage or env vars |
| Blocking main thread | Use Web Workers or Tauri async commands |

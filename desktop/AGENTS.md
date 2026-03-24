# DESKTOP — Tauri Desktop Application Wrapper

Tauri v2 desktop application shell that delegates to `../frontend` for UI. Minimal wrapper with platform-specific bindings.

## STRUCTURE

```
desktop/
├── src-tauri/
│   ├── src/                     # Rust IPC handlers, system integration
│   ├── binaries/                # Bundled executables (platform-specific)
│   ├── capabilities/            # Tauri permission manifests
│   ├── Cargo.toml               # Rust dependencies
│   ├── tauri.conf.json          # Desktop app config (window, menu, updater)
│   ├── build.rs                 # Build-time codegen
│   └── Entitlements.plist       # macOS sandbox entitlements
├── src/                         # Minimal React shim (delegates to ../frontend/src)
├── scripts/                     # Build/release automation
├── package.json                 # npm scripts (proxies to ../frontend)
└── README.md                    # Desktop-specific setup
```

## WHERE TO LOOK

| Task | File/Directory | Notes |
|------|----------------|-------|
| Tauri config | `src-tauri/tauri.conf.json` | Window size, menu, updater, permissions |
| Rust IPC handlers | `src-tauri/src/` | System calls, file I/O, process spawn |
| macOS entitlements | `src-tauri/Entitlements.plist` | Sandbox permissions (camera, mic, network) |
| Bundled binaries | `src-tauri/binaries/` | Platform-specific executables (e.g., Ollama) |
| Build scripts | `scripts/` | Release automation, code signing |
| UI components | `../frontend/src/` | Shared React components |

## CONVENTIONS

**Build delegation**: `npm run dev` and `npm run build` proxy to `../frontend` with `--outDir dist` override. Desktop does not maintain separate UI code.

**Tauri plugins**: Uses `@tauri-apps/plugin-*` for autostart, global shortcuts, notifications, updater, shell, process. Configure in `tauri.conf.json`.

**Capabilities**: Permission manifests in `capabilities/` define allowed IPC commands. Follows principle of least privilege.

**Platform binaries**: `binaries/` contains platform-specific executables. Tauri bundles them into app package. Use `sidecar` API to spawn.

**Updater**: Configured for GitHub Releases. `@tauri-apps/plugin-updater` checks for updates on launch.

## ANTI-PATTERNS

| Forbidden | Why |
|-----------|-----|
| Duplicating UI code from frontend/ | Desktop is a wrapper, not a fork |
| Skipping capabilities manifests | IPC calls fail without explicit permissions |
| Bundling large binaries without compression | Bloats app size (use external download if >50MB) |
| Hardcoding paths in Rust | Use Tauri path resolver APIs |
| Skipping code signing on macOS | App won't run on Gatekeeper-enabled systems |

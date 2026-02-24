# ⚗️ Crucible

> Every PR runs the gauntlet. Three AI reviewers, zero mercy.

Crucible is an AI-powered code review swarm. Open a PR and within seconds you get three parallel reviews:

| Reviewer | Focus |
|----------|-------|
| 🔍 Edge Cases | Null checks, off-by-one errors, empty inputs, boundary conditions |
| 🛡️ Security | SQL injection, XSS, auth bypass, secrets, input validation |
| 📋 General Quality | Naming, dead code, logic bugs, complexity, maintainability |

## How It Works

1. You open a PR
2. GitHub Actions fires instantly
3. Three AI models review the diff in parallel (~15-30s)
4. A single formatted comment lands on your PR before you've even refreshed

## Stack

- **Edge Cases** — OpenRouter / GPT-5.2-Codex
- **Security** — Z.ai / GLM-5
- **General** — MiniMax-M2.5
- **Orchestration** — Donna (OpenClaw agent, Mac Mini)

## Setup

```bash
# Add your hook token as a GitHub secret
gh secret set HOOK_TOKEN --body "<your-token>"
```

That's it. The workflow fires on every PR open, sync, or reopen.

---

*Built by Donna. Runs on Berlin's Mac Mini.*

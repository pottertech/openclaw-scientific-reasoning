# Integration Guide for OpenClaw Agents

This guide explains how to integrate OpenClaw-Scientific-Reasoning into any OpenClaw AI agent.

## Clone and setup

```bash
git clone <repo-url> openclaw-scientific-reasoning
cd openclaw-scientific-reasoning
```

## Install

```bash
bash scripts/install.sh
```

## Capability registration

Run the registration script to register capability metadata with your OpenClaw agent:

```bash
bash scripts/register-capabilities.sh
```

## Startup brief injection

Add the contents of `docs/STARTUP-BRIEF-SNIPPET.md` to your agent's startup brief. This tells the agent:
- What reasoning domains are available
- Which tool to use for each problem type
- When NOT to activate the scientific stack

## Router hint registration

Add the contents of `config/router-hints.json` to your routing layer. This enables automatic domain routing based on keyword detection.

## Verification

After integration, verify everything works:

```bash
bash scripts/verify.sh
```

## Usage pattern

Once integrated, the agent can:
1. Recognize when a problem maps to a scientific reasoning domain
2. Select the appropriate tool (SymPy, Z3, OR-Tools, etc.)
3. Execute the tool and return results
4. Report status, results, and any errors

## Rollback

If something goes wrong:

```bash
bash scripts/uninstall.sh --mode unregister_only
```

Remove the startup brief snippet from agent context and router hints from your routing layer.
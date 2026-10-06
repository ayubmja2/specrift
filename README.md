# specrift

# specrift

**Catch breaking API changes before they reach your users.**

specrift compares two versions of an OpenAPI spec, flags changes that would break existing clients, and explains each one in plain English with migration notes.

> 🚧 **Status:** In active development. See the roadmap below.

## The problem

A backend developer renames a response field from `temp` to `temperature`. The server works, the tests pass, and the change ships. But every mobile app still reading `temp` now breaks, and nobody notices until users complain.

specrift catches this at the pull request, before it ships.

## How it works

1. **Load** two versions of your OpenAPI spec (from files or git commits)
2. **Resolve** all `$ref` pointers into comparable trees
3. **Diff** them using deterministic, unit-tested rules that classify each change as *breaking*, *safe*, or *risky*
4. **Explain** each breaking change using an LLM, grounded in the exact diff, so it can't invent endpoints or fields
5. **Report** in the terminal, as JSON/Markdown, or as a pull request comment

The rules decide what's broken. The AI only explains it.

## Example (planned)
```
$ specrift diff main feature-branch

✗ BREAKING  GET /weather/{city}
  Response field `temp` was removed.
  Clients reading `temp` will receive undefined.
  Migration: read `temperature` instead (added in this change).
```
## Roadmap

- [x] Load and validate OpenAPI specs
- [ ] Resolve `$ref` pointers (including circular references)
- [ ] Core breaking-change rules with full test coverage
- [ ] CLI with terminal, JSON, and Markdown output
- [ ] LLM explanations with structured, validated output
- [ ] Support for local (Ollama) and hosted LLM providers
- [ ] Evaluation set comparing explanation quality across models
- [ ] GitHub Action with pull request comments
- [ ] Real-world demo against a public API's history

## Tech

Python · uv · Pydantic · Typer · Rich · pytest · GitHub Actions

## License

MIT

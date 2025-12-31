# Copilot instructions for python_for_web

This project is a tiny Flask tutorial app. The goal of these instructions is to help an AI coding agent be immediately productive in this repository.

Summary
- Single-file Flask application: `app.py` is the primary entrypoint and contains the Flask app definition.
- Virtual environment: a local `venv/` contains project dependencies; `.vscode/settings.json` points to `venv/bin/python`.

How to run locally (discoverable from files)
- Activate venv: `source venv/bin/activate` (macOS/Linux).
- Two runnable options:
  - `python app.py` — if `app.py` contains an `if __name__ == '__main__': app.run(...)` block.
  - `FLASK_APP=app.py flask run` — a safe alternative using the Flask CLI.

Project-specific patterns
- Single-module structure: features, routes, and configuration live in `app.py`. Avoid creating assumptions about Blueprints, packages, or templates unless new files appear.
- Minimal dependencies: do not add heavy frameworks without justification for this tutorial-sized project.

Developer workflows and commands
- Use the repository's `venv` python for consistency: `.vscode/settings.json` points to `venv/bin/python`.
- If adding dependencies, update a `requirements.txt` at project root and document pip install steps: `pip install -r requirements.txt`.

Conventions for AI edits
- Keep changes minimal and focused: prefer small edits to `app.py` unless adding a clear new feature.
- When adding routes or handlers, follow the existing coding style: top-level `Flask` import and simple function-based views.
- Don't remove the `venv/` folder; it's part of the workspace setup. If you add CI/workflow files, do not reference secrets or external services.

Integration points and external dependencies
- There are no external APIs or DB integrations visible in the repo. If implementing integrations, add explicit configuration and document expected environment variables in `README.md`.

What the agent should check before proposing changes
- Confirm the presence of `if __name__ == '__main__'` or runnable app entry before recommending `python app.py`.
- Verify `.vscode/settings.json` when changing Python interpreter paths.

Files to reference when summarizing behavior
- `app.py` — app entrypoint and routes.
- `.vscode/settings.json` — local interpreter config.

If anything is unclear
- Ask a human for the intended runtime command and whether the `venv` should be regenerated. Prefer small, reversible commits and request review.

End of file

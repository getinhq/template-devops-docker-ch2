# Multi-service Docker Compose app

## Task
Containerize a simple full-stack app (Flask API + Streamlit UI) with `docker-compose.yml`: shared network and a named volume for SQLite (or documented data path).

## Starter (not finished)
Services build, but you must wire persistence, env, and health checks per the roadmap. Document setup in this README.

## Your work
- Ensure API and UI communicate on the compose network.
- Add a named volume mounted where SQLite (or data file) lives.
- Document `docker compose up --build` and how to verify both services.
- Optional: add a simple healthcheck to each service.

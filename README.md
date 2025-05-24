# Prompt Engineering Framework

A lightweight framework for developing and testing AI-driven TRPG narrative options.

## Features

- Prompt management with JSON templates
- Multi-model support (DeepSeek, OpenAI, Claude)
- XMind integration with AI Agent assistance
- CLI and FastAPI Web UI
- MongoDB and Redis for data storage
- Plugin system for extensibility

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and configure your environment variables
4. Start MongoDB and Redis:
   ```bash
   docker-compose up -d
   ```
5. Run the application:
   ```bash
   uvicorn api.endpoints:app --host 0.0.0.0 --port 8000
   ```

## Development

- Run tests: `pytest --cov=services tests/`
- Format code: `black .`
- Type checking: `mypy .`

## License

MIT 
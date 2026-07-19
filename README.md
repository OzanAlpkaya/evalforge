# EvalForge

LLM evaluation, RAG quality, and prompt regression platform built with Python and FastAPI.

## Problem

Changes to prompts, models, and retrieval pipelines can improve one aspect of an AI system while degrading another. A new configuration may produce more accurate answers but increase latency, cost, hallucination risk, or retrieval noise.

EvalForge provides a reproducible way to evaluate these changes against versioned datasets and compare quality, operational, and cost metrics before release.

## Planned Core Capabilities

- Versioned evaluation datasets and test cases
- Immutable prompt versions and model configurations
- Asynchronous evaluation runs
- Deterministic, semantic, and LLM-as-a-judge evaluators
- RAG retrieval and groundedness metrics
- Token usage, estimated cost, latency, and error tracking
- Regression thresholds with machine-readable results
- Integration tests using real PostgreSQL and RabbitMQ services

## Architecture Direction

- Python 3.13 and FastAPI
- PostgreSQL with pgvector
- SQLAlchemy 2 and Alembic
- Celery and RabbitMQ
- Provider-independent LLM and embedding adapters
- Docker Compose and GitHub Actions

## Scope

EvalForge is an evaluation platform, not a chatbot or agent platform. The first version intentionally excludes authentication, multi-tenancy, a large frontend, fine-tuning, Kubernetes, and Terraform so the project can remain focused on AI evaluation quality.

## Project Status

Sprint 0 - Foundation is in progress.

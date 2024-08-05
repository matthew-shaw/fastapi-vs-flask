# FastAPI vs Flask Experiments

This experiment demonstrates:

- WIP

## Getting started

```bash
docker compose up --build
```

## Design

```mermaid
flowchart TB
    client(Client):::C
    subgraph Docker compose
        subgraph Python container
            app1(Uvicorn / FastAPI):::A
        end

        subgraph Python container
            app2(Gunicorn / Flask):::A
        end
        
        subgraph Postgres container
            db1[(Database)]:::D
        end
        
        subgraph Postgres container
            db2[(Database)]:::D
        end
    end

    client -- http --> app1 & app2
    app1 --> db1
    app2 --> db2

    classDef A fill:#DAE8FC,stroke:#6C8EBF,stroke-width:2px
    classDef D fill:#F8CECC,stroke:#B85450,stroke-width:2px
    classDef C fill:#D5E8D4,stroke:#82B366,stroke-width:2px
```

## Performance

### Test environment

| Dependency     | Version | Used by     |
|----------------|---------|-------------|
| Alembic        | 1.13.2  | Common      |
| Docker         | 27.1.1  | Common      |
| Docker Compose | 2.29.1  | Common      |
| Postgres       | 16.4    | Common      |
| Psycopg        | 3.2.1   | Common      |
| Python         | 3.12.4  | Common      |
| SQLAlchemy     | 2.0.31  | Common      |
| FastAPI        | 0.112.0 | FastAPI App |
| Pydantic       | 2.8.2   | FastAPI App |
| Starlette      | 0.37.2  | FastAPI App |
| Uvicorn        | 0.30.5  | FastAPI App |
| Flask          | 3.0.3   | Flask App   |
| Gunicorn       | 22.0.0  | Flask App   |
| Werkzeug       | 3.0.3   | Flask App   |

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

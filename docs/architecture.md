# Architecture

```mermaid
flowchart TD
    P[examples/playbooks/*.yaml] --> L[loader.py]
    L --> M[models.py validation]
    M --> S[safety.py command policy]
    S --> X[executor.py dry-run executor]
    X --> E[evidence.py run directory]
    E --> R[report.py Markdown report]
```

The architecture is intentionally local and conservative. The MVP does not connect to real infrastructure. It validates synthetic playbooks, records what would happen, and produces evidence suitable for review.

# Architectural Decision Records

This folder contains all key architectural decisions made in the SPLiT project.
Each ADR file describes one specific decision and follows a consistent structure.

---

## 📄 ADR Index

| Date       | Title |
|------------|-------|
| 2025-04-25 | [Storing architectural information in the `architecture/` folder](20250425-keep-architecture-folder.md) |
| 2025-04-25 | [Splitting MySQL into multiple databases by subsystem](20250425-split-mysql-databases.md) |
| 2025-04-25 | [Split `src/` into logical modules: Core and Users Interaction](20250425-split-src-into-logical-modules-core-and-users-interaction.md) |
| 2025-04-25 | [Use Log4brains to manage the ADRs](20250425-use-log4brains-to-manage-the-adrs.md) |
| 2025-04-25 | [Use Qdrant for vector storage](20250425-use-qdrant-for-vector-storage.md) |
| 2025-05-25 | [Logger Module Description](20250525-logger-module-description.md) |
| 2025-05-27 | [Adopt Peewee as ORM for SPLit MVP](20250527-adopt-peewee-as-orm-for-split-mvp.md) |
| 2025-05-27 | [Limit initial MySQL schema to five core databases](20250527-limit-initial-mysql-schema-to-five-core-databases.md) |
| 2025-05-28 | [Infrastructure Stack for Task Execution (Redis + Celery)](20250528-infrastructure-stack-for-task-execution-redis-celery.md) |
| 2025-05-28 | [Initial Module Set for the MVP](20250528-initial-module-set-for-the-mvp.md) |

---

## Development

To preview the knowledge base locally, run:

```bash
log4brains preview
```

To create a new ADR interactively, run:

```bash
log4brains adr new
```

## More information

- [Log4brains documentation](https://github.com/thomvaill/log4brains/tree/develop#readme)
- [What is an ADR and why should you use them](https://github.com/thomvaill/log4brains/tree/develop#-what-is-an-adr-and-why-should-you-use-them)
- [ADR GitHub organization](https://adr.github.io/)

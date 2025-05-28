# Splitting MySQL into multiple databases by subsystem

- Status: superseded by [20250527-limit-initial-mysql-schema-to-five-core-databases](20250527-limit-initial-mysql-schema-to-five-core-databases.md)
- Date: 2025-04-24
- Tags: db, mysql

## Context

During architectural planning, it became clear that all data — from user profiles to API configurations and analytical strategies — were stored in a single monolithic MySQL database. This design increased complexity in backups, migrations, and access control.

## Decision

The project now uses multiple logically separated MySQL databases:

- `split_stocks` — stock analytics  
- `split_events` — event logs (news, signals)  
- `split_notifications` — user notifications  
- `split_api_gates` — API gateway configurations  
- `split_processing_config` — parsing and processing parameters

Each database can have its own security schema, be mounted independently, and scale separately. Modules interact only with the databases they need.

## Consequences

✅ Improved data isolation  
✅ Simplified backups and recovery  
✅ Easier to manage access based on least privilege  

⚠️ Slightly more complex setup and configuration  
⚠️ Requires synchronization of models and migrations across multiple databases

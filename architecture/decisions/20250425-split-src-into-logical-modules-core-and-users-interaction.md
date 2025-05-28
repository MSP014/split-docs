# Split `src/` into logical modules: Core and Users Interaction

- Status: accepted
- Date: 2025-04-25
- Tags: project-structure, modularity

## Context

As the project grew, the number of modules increased and the flat structure of `src/` became hard to navigate and maintain. There was no clear separation between analytical logic and user-facing components.


## Decision

The `src/` folder is now split into:
- `core/` — data analysis and math modules  
- `users_interaction/` — user-facing API, UI, assistant  
- `data_inputs/` — parsers and ingestion logic  
- `utils/` and `storage/` — helpers and DB logic

This structure aligns with the C4 container diagram and improves modularity.

## Consequences

✅ Easier to understand module boundaries  
✅ Scales well as the number of containers increases  
⚠️ Requires maintenance of cross-module import boundaries
# Storing architectural information in the `architecture/` folder

- Status: accepted
- Date: 2025-04-25
- Tags: architecture, documentation

## Context

The project requires centralized storage of all materials describing the system’s architecture: C4 diagrams, methodologies, conceptual documentation, source structure, and container/module organization.

## Decision

A dedicated `architecture/` folder was created to include:

- `C4 Diagrams/` — architectural diagrams  
- `methods/` — mathematical methods used in analysis  
- `concepts/` — project philosophy and conceptual documents  
- `decisions/` — ADR (Architectural Decision Records)

This structure is aligned with the C4 container diagram and the actual file organization of the project.

## Consequences

✅ All architectural assets are organized and accessible in one place  
✅ Simplifies navigation, documentation maintenance, and team onboarding  
⚠️ Requires consistent maintenance to stay up to date  
⚠️ Possible redundancy between `docs/` and `architecture/` during export workflows

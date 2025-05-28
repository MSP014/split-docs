# SPLiT — Documentation Repository

This repository contains the core documentation for **SPLiT** — the **Strategic Performance & Long-term Investment Toolkit**.  
SPLiT is a data-driven assistant designed to support long-term investment decisions.  
This repo is intended as a first look into the project’s architecture, concept, and methodology.

---

## 📁 Structure

### `architecture/` — Project Architecture
- **`C4 Diagrams/`**  
  Visual representation of the system design:
  - Context-Level Diagram
  - Container-Level Diagram (focused on MVP)

- **`decisions/`**  
  Architectural Decision Records ([ADR](https://github.com/MSP014/split-docs/blob/main/architecture/decisions/README.md)) documenting key design choices.

  Not all decisions were made in strict chronological order — ADRs reflect the evolving design logic and architectural vision.  
  For example: the [initial MVP module set](https://github.com/MSP014/split-docs/blob/main/architecture/decisions/20250528-initial-module-set-for-the-mvp.md).

- **`project_structure.md / project_structure_ASCII.txt`**  
  Current folder and file layout, including ORM layer (Peewee).

---

### `concepts/` — Philosophy & Context
- **`SPLit_Project_Concept.md`** — concise overview of the project idea and functional scope.
- **`Project_S_Article_en.md / ru.md`** — the Medium-ready article describing the vision, architecture, and personal motivation behind SPLiT (in English and Russian).

---

### `methods/` — Mathematical Core
- **`Mathematical_Methods.md`**  
  Detailed overview of planned analytical modules — from initial filtering and risk assessment to portfolio optimization and Monte Carlo simulation.

---

## 🔒 Who This Is For — and Why

This repository is for those considering contributing to SPLiT.  
The materials here are meant to help you:

- understand the philosophy and objectives behind the project;
- assess the architectural maturity;
- decide whether you’d like to get involved.

---

## 🙋 What’s Next?

If you find the project compelling after reading through the docs —  
[reach out](mailto:mail@pospelkov.com) and I’ll provide access to the main development repository (`dev` branch, source code, Docker setup, ORM layer, analytical logic, etc.).

If not — no hard feelings.  
Thanks for taking the time to read and explore.

---

**SPLiT isn’t built for hype.**  
If you’re chasing quick wins and promises of 10x returns, this probably isn’t the project for you — and that’s fine.  
This is a long-term tool, built slowly and carefully — first and foremost for myself, but if it proves useful to others, all the better.

If you think the same way — welcome aboard.

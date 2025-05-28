
# SPLiT — Структура проекта

from pathlib import Path

content = """# SPLiT — Структура проекта

## Корневая структура

- `.git/`
- `.idea/`
- `architecture/` — Описание архитектуры проекта
  - `C4 Diagrams/`
    - `SPLiT - C4 Diagram - 01 Context Level.md`
    - `SPLiT - C4 Diagram - 02 Container Level.md`
  - `project_structure.md`
- `concepts/` — Концептуальные документы проекта
  - `Project_S_Article_en.md`
  - `Project_S_Article_ru.md`
  - `SPLit_Project_Concept.md`
- `methods/` — Детальное описание математических методов
  - `Mathematical_Methods.md`
- `src/` — Исходный код проекта
  - `data_inputs/` — API-шлюзы и загрузка файлов
    - `api_gates/`
      - `yahoo_api/`
      - `news_api/`
      - `telegram_api/`
      - `youtube_api/`
      - `gmail_api/`
      - `podcast_api/`
      - `scraping_api/`
      - `other_api/`
    - `file_inputs/`
      - `downloader/`
      - `file_service/`
  - `data_processing/` — Обработка данных и оркестрация
    - `security/`
      - `security_scanner/`
    - `routing/`
      - `orchestrator/`
    - `parsing/`
      - `pdf_processing/`
      - `text_processing/`
      - `media_processing/`
      - `video_processing/` (будет позже)
  - `core/` — Ядро аналитики
    - `preliminary_analysis/`
      - `news_analysis/`
      - `media_analysis/`
      - `forecast_eval/`
      - `report_analysis/`
      - `visual_semantics/` (будет позже)
    - `math_methods/`
      - `01_init_filter/`
      - `02_risk_assessment/`
      - `03_growth_efficiency/`
      - `04_profit_forecast/`
      - `05_risk_mitigation/`
      - `06_breakeven_analysis/`
      - `07_adv_risk/`
      - `08_final_selection/`
    - `final_correction/`
      - `analysis_correction/`
      - `rag_memory/`
  - `users_interaction/` — Взаимодействие с пользователем
    - `user_security/`
      - `auth/`
      - `user_mgmt/`
      - `subscription/`
    - `webface/`
      - `web_ui/`
      - `mobile_app/`
      - `assistant/`
    - `backend/`
      - `strategy_planner/`
      - `portfolio_mngr/`
      - `wishlist_mngr/`
      - `points_mngr/`
      - `user_intgr/`
      - `data_viz/`
      - `external_api/`
  - `orm/` — ORM-слой (Peewee)
    - `models/`
      - `base.py` — Database connections & `BaseModel`
      - `logs.py` — `split_logs.logs`
      - `events_log.py` — `split_events.events_log`
      - `users.py` — `split_users.users`
      - `portfolios.py` — `split_portfolios.portfolios`
      - `portfolio_items.py` — `split_portfolios.portfolio_items`
      - `portfolio_history.py` — `split_portfolios.portfolio_history`
      - `initial_filtration.py` — `split_math_core.initial_filtration`
      - `final_selections.py` — `split_math_core.final_selections`
    - `dao/` — Data Access Objects
      - `logs_dao.py`
      - `events_dao.py`
      - `users_dao.py`
      - `portfolios_dao.py`
      - `portfolio_items_dao.py`
      - `portfolio_history_dao.py`
      - `initial_filtration_dao.py`
      - `final_selections_dao.py`
  - `utils/` — Утилиты и инфраструктура
    - `event_service/`
    - `log_service/`
    - `notification_service/`
    - `semantic_log_analyzer/`
    - `scheduler/`
  - `storage/` — Скрипты и структуры баз данных
    - `mysql/`
    - `qdrant/`
- `tests/` — Тесты (будет позже)
- `docker/` — Docker-конфигурация
  - `mysql/`
- `.env`
- `.gitignore`
- `docker-compose.yml`
- `README.md`


# 📜 Примечания

- **`architecture/`** — хранит полное описание проектной архитектуры, диаграммы, принципы модульности.
- **`concepts/`** — концептуальные статьи, миссия проекта и обоснование решений.
- **`methods/`** — детальное описание используемых математических методов и логики их применения.
- **`src/`** — исходный код проекта, организованный по модульной структуре.
- **`tests/`** — папка под автоматические тесты.
- **`docker/`** — конфигурация контейнеров для разработки и деплоя.
- **`orm/`** — слой для модели данных на Peewee, включая модели и DAO.
- **Корневые файлы** (`docker-compose.yml`, `.env`, `.gitignore`, `README.md`) обеспечивают базовую конфигурацию и настройку проекта.

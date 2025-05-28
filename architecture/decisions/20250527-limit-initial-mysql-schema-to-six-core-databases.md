# Limit initial MySQL schema to six core databases

- Status: accepted
- Date: 2025-05-27
- Tags: storage, mysql, mvp-scope, simplification

## Context

Initial architectural drafts for SPLit included the following MySQL databases:

- `split_stocks` — used to store historical market data and price time series
- `split_logs` — used by the centralized logger module (`logSrv`)
- `split_events` — used by `eventSrv` to log system-wide task execution and event chains
- `split_users` — used by `userMgmt` to manage user profiles and access roles
- `split_portfolios` — used by `portfolioMngr` to store current portfolio state and its modification history
- `split_math_core` — used by all mathematical analysis modules (`initlFilter`, `finalSel`, etc.)

However, during MVP planning, it became clear that not all of these components will be implemented from the start. In particular:
- No notification module is required initially, making `split_notifications` redundant.
- Media parsing will be deferred, so `split_processing_config` is not needed yet.
- Only a single API Gateway will be active at launch, with configuration stored in a flat file instead of a dedicated database, making `split_api_gates` unnecessary.

## Decision

The following reduced database set will be used at MVP stage:

---

### `split_stocks`

Stores historical time series for stock prices and volumes

```sql
stock_prices(
  id,
  ticker,
  date,
  open,
  close,
  high,
  low,
  volume,
  adj_close
)
```

---



### `split_logs`

Used by the centralized logger module (`logSrv`)

```sql
logs(
  id,
  timestamp,
  level,
  module,
  user_id,
  session_id,
  message,
  metadata
)
```

---

### `split_events`

Stores task executions and module-level event chains

```sql
events_log(
  event_id,
  user_id,
  event_type,
  source_module,
  target_module,
  status,
  payload,
  created_at,
  updated_at
)
```

---

### `split_users`

Used by `userMgmt` for managing core user identities

```sql
users(
  id,
  username,
  email,
  role,
  created_at,
  last_login,
  is_active,
  preferences
)
```

---

### `split_portfolios`

Used by `portfolioMngr` to manage user portfolios

```sql
portfolios(
  portfolio_id,
  user_id,
  name,
  description,
  is_active,
  created_at
)

portfolio_items(
  item_id,
  portfolio_id,
  ticker,
  enabled,
  added_at
)

portfolio_history(
  history_id,
  portfolio_id,
  ticker,
  action,
  timestamp,
  initiator,
  reason
)
```

---

### `split_math_core`

Stores results of mathematical analysis modules

```sql
initial_filtration(
  result_id,
  user_id,
  session_id,
  ticker,
  normalized_score,
  reasons_json,
  created_at
)

final_selections(
  rec_id,
  user_id,
  session_id,
  ticker,
  final_decision,
  score,
  created_at
)
```

---

## Consequences

✅ Simpler initial database schema  
✅ Reduced complexity for development and deployment  
✅ Matches the actual MVP implementation scope  
⚠️ Future rework will be required if/when excluded modules are reintroduced

# Use Qdrant for vector storage

- Status: accepted
- Date: 2025-04-25
- Tags: storage, vector-db

## Context

A vector database is required to store high-dimensional representations of news, media, forecasts, and semantic memory. The chosen database must support filtering, local deployment, and simple integration.

## Decision

Qdrant was selected due to its open-source nature, built-in filtering, solid documentation, and easy deployment via Docker. It provides good performance and is sufficient for the needs of the SPLiT project at the current stage.

## Consequences

✅ Simple setup and fast prototyping  
✅ Filtering out irrelevant vectors using metadata  
✅ Local and open-source friendly  
⚠️ Less mature ecosystem than alternatives like Pinecone or Weaviate

# Day 61–75: Data Management & Pipeline Integration

## What's New
- Kafka consumer integrated for real-time inference log streaming
- `/dashboard` API for analytics summary
- SQL schema for structured log storage

## Setup
1. Make sure Kafka is running locally (`localhost:9092`)
2. Producer should write inference logs as JSON:
```json
{ "prompt": "Hello", "result": "Hello world..." }

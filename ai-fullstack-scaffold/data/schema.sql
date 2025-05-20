CREATE TABLE inference_logs (
  id SERIAL PRIMARY KEY,
  prompt TEXT,
  result TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

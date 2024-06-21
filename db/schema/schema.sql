CREATE TABLE backtest_results (
    id SERIAL PRIMARY KEY,
    scene_id INT REFERENCES scenes(id),
    gross_profit FLOAT NOT NULL,
    net_profit FLOAT NOT NULL,
    number_of_trades INT NOT NULL,
    winning_trades INT,
    losing_trades INT,
    max_drawdown FLOAT,
    sharpe_ratio FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scenes (
    id SERIAL PRIMARY KEY,
    period INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE  IF NOT EXISTS users (
  "id" SERIAL PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL,
  "email" varchar NOT NULL,
  "password" varchar NOT NULL,
  "created_at" timestamp NOT NULL
  "updated_at" timestamp NOT NULL
  "deleted_at" timestamp NOT NULL

  UNIQUE (email)
);

CREATE TABLE indicators (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);
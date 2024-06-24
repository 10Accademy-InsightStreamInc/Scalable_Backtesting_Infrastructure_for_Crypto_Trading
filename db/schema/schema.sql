CREATE TABLE "indicators" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL,
  "symbol" VARCHAR(255) NOT NULL,
  "description" TEXT
);

CREATE TABLE "stocks" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL,
  "symbol" VARCHAR(255) NOT NULL,
  "description" TEXT
);

CREATE TABLE "scenes" (
  "id" SERIAL PRIMARY KEY,
  "period" INT NOT NULL,
  "start_date" DATE NOT NULL,
  "end_date" DATE NOT NULL,
  "stock_id" INT,
  "indicator_id" INT
);

CREATE TABLE "backtest_results" (
  "id" SERIAL PRIMARY KEY,
  "scene_id" INT,
  "gross_profit" DECIMAL(15,2),
  "net_profit" DECIMAL(15,2),
  "number_of_trades" INT,
  "winning_trades" INT,
  "losing_trades" INT,
  "max_drawdown" DECIMAL(5,2),
  "sharpe_ratio" DECIMAL(5,2),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

ALTER TABLE "scenes" ADD FOREIGN KEY ("indicator_id") REFERENCES "indicators" ("id");

ALTER TABLE "scenes" ADD FOREIGN KEY ("stock_id") REFERENCES "stocks" ("id");

ALTER TABLE "backtest_results" ADD FOREIGN KEY ("scene_id") REFERENCES "scenes" ("id");

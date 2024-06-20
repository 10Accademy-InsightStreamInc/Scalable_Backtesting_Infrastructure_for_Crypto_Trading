CREATE TABLE IF NOT EXISTS scenes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    period INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS backtests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    scene_id INT,
    gross_profit FLOAT,
    net_profit FLOAT,
    number_of_trades INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scene_id) REFERENCES scenes(id)
);

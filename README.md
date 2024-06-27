# Scalable Stock and Crypto Backtesting Infrastructure

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)
- [Kafka Integration](#kafka-integration)
- [LSTM Integration](#lstm-integration)
- [License](#license)

## Overview

Mela, a startup, aims to simplify cryptocurrency trading for everyone and provide reliable investment sources while mitigating risks. This project is focused on designing and building a reliable, large-scale trading data pipeline that can run various backtests and store useful artifacts in a robust data warehouse.

## Key Objectives

- **Run Multiple Backtests**: Utilize various technical indicators and assets to perform backtests.
- **Design Database Schema**: Store backtest artifacts in a well-structured database.
- **Integrate MLOps Tools**: Use Apache Kafka, Airflow, MLflow, and CML.
- **Build Frontend**: Create an interface for users to run backtests.
- **Test Pipeline**: Ensure the pipeline's functionality and reliability.

## Skills and Knowledge

- **Skills**: Technical analysis, backtesting, trading, data pipeline building, structured streaming, workflow orchestration.
- **Knowledge**: Financial prediction, enterprise-grade data engineering using Apache and Databricks tools.

## Technical Skills

- **Python Programming**
- **SQL Programming**
- **Data & Analytics Engineering**
- **MLOps**
- **Software Development Frameworks**

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/dev-abuke/Scalable_Backtesting_Infrastructure_for_Crypto_Trading.git
```
### Move to Working Directory

```bash
cd Scalable_Backtesting_Infrastructure_for_Crypto_Trading
```
## Set Up Local Development Environment

**Create a virtual environment for the project**

```bash
python -m venv env
```

```sh
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

**Install necessary packages**

```bash
pip install -r requirements.txt
```
## Project Structure
```bash
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py   
│   ├── auth.py
│   ├── requirements.txt
│   ├── README.md
│   └── scripts
│       ├── backtesting
│       ├── init_data.py
│       ├── kafka_config.py
│       │   ├── main.py
│       └── init_db.py
├── scripts/
│   └── download_data.py
├── tests/
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
└── README.md
```

### Set Up Kafka

If you do not have Kafka installed, you can run it using Docker:

docker run -d --name zookeeper -p 2181:2181 zookeeper:3.4.9
docker run -d --name kafka -p 9092:9092 --link zookeeper wurstmeister/kafka:latest

Alternatively, follow the [Kafka Quickstart](https://kafka.apache.org/quickstart) guide to set up Kafka.

### Configure Environment Variables

Create a `.env` file in the root directory and add the following configurations:

- KAFKA_BROKER_URL=localhost:9092
- SCENE_TOPIC=scene_parameters
- RESULT_TOPIC=backtest_results

### Initialize the Database

python -m scripts.init_db

## Backend Usage

### Run the FastAPI Application

uvicorn main:app --reload

### Sending Requests

Use a tool like Postman, Thunder Client, or Curl to interact with the API.

### Endpoints

### Health Check

**GET /health**

### Create Indicator

**POST /indicators/**

```sh
Body
{
  "name": "Simple Moving Average",
  "symbol": "SMA",
  "description": "A simple moving average indicator"
}
```

### Read Indicators

**GET /indicators/**

### Create Stock

**POST /stocks/**

```sh
Body
{
  "name": "Apple Inc.",
  "symbol": "AAPL",
  "description": "Apple Inc. stock"
}
```

### Read Stocks

**GET /stocks/**

### Create Scene

**POST /scenes/**

```sh
Body
{
  "period": 20,
  "indicator_id": 1,
  "stock_id": 1,
  "start_date": "2023-01-01",
  "end_date": "2023-12-31"
}
```

### Read Scenes

**GET /scenes/**

### Perform Backtest

**POST /backtests/{scene_id}**

### Read Backtest Results

**GET /backtest_results/**

## Contributors
- Abubeker Shamil
- Michael George

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
**Instructors** 
- Yabebal
- Nathnael
- Emtinan
- Rehmet

**References:** 
backtrader, Freqtrade, Vectorbt, Kafka, Airflow, MLflow, CML
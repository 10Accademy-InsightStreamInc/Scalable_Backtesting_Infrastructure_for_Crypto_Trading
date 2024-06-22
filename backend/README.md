# FastAPI Application Documentation

This documentation provides an overview and instructions for a FastAPI application that interfaces with a database to manage indicators, stocks, and scenes, and performs backtests based on the provided scenes.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
    - [Virtual Environment](#virtual-environment)
3. [API Endpoints](#api-endpoints)
    - [Health Check](#health-check)
    - [Indicators](#indicators)
    - [Stocks](#stocks)
    - [Scenes](#scenes)
    - [Backtests](#backtests)
    - [Backtest Results](#backtest-results)
4. [Database Models](#database-models)
5. [Utility Functions](#utility-functions)
6. [Data Fetching](#data-fetching)

## Introduction

This FastAPI application provides endpoints for managing financial indicators, stocks, scenes, and performing backtests. The app interacts with a database using SQLAlchemy ORM and includes endpoints for creating, reading, and managing these entities.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/10Accademy-InsightStreamInc/Scalable_Backtesting_Infrastructure_for_Crypto_Trading
    cd Scalable_Backtesting_Infrastructure_for_Crypto_Trading
    ```

2. **Set up the virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    Ensure that your database configuration in `database.py` is correct. The database tables will be created automatically upon running the application.

5. **Run the FastAPI application**:
    ```sh
    uvicorn backend.main:app --reload
    ```

## API Endpoints

### Health Check

#### Check API Health

- **Endpoint**: `/health`
- **Method**: `GET`
- **Response**: "API is healthy"

This endpoint checks the health status of the API.

### Indicators

#### Create Indicator

- **Endpoint**: `/indicators/`
- **Method**: `POST`
- **Request Body**: 
    ```sh
    {
      "name": "string",
      "symbol": "string",
      "description": "string"
    }
    ```
- **Response**:
    ```sh
    {
      "id": 1,
      "name": "string",
      "symbol": "string",
      "description": "string"
    }
    ```
Creates a new financial indicator and saves it to the database.

#### Read Indicators

- **Endpoint**: `/indicators/`
- **Method**: `GET`
- **Query Parameters**:
  - `skip` (default: 0)
  - `limit` (default: 10)
- **Response**:
    ```sh
    [
      {
        "id": 1,
        "name": "string",
        "symbol": "string",
        "description": "string"
      }
    ]
    ```
Retrieves a list of indicators from the database.

### Stocks

#### Create Stock

- **Endpoint**: `/stocks/`
- **Method**: `POST`
- **Request Body**:
    ```sh
    {
      "name": "string",
      "symbol": "string",
      "description": "string"
    }
    ```
- **Response**:
    ```sh
    {
      "id": 1,
      "name": "string",
      "symbol": "string",
      "description": "string"
    }
    ```
Creates a new stock entry and saves it to the database.

#### Read Stocks

- **Endpoint**: `/stocks/`
- **Method**: `GET`
- **Query Parameters**:
  - `skip` (default: 0)
  - `limit` (default: 20)
- **Response**:
    ```sh
    [
      {
        "id": 1,
        "name": "string",
        "symbol": "string",
        "description": "string"
      }
    ]
    ```
Retrieves a list of stocks from the database.

### Scenes

#### Create Scene

- **Endpoint**: `/scenes/`
- **Method**: `POST`
- **Request Body**:
    ```sh
    {
      "period": 1,
      "start_date": "2023-01-01",
      "end_date": "2023-12-31",
      "stock_name": "string",
      "indicator_id": 1
    }
    ```
- **Response**:
    ```sh
    {
      "id": 1,
      "period": 1,
      "start_date": "2023-01-01",
      "end_date": "2023-12-31",
      "stock_name": "string",
      "indicator_id": 1
    }
    ```
Creates a new scene entry and saves it to the database.

#### Read Scenes

- **Endpoint**: `/scenes/`
- **Method**: `GET`
- **Query Parameters**:
  - `skip` (default: 0)
  - `limit` (default: 10)
- **Response**:
    ```sh
    [
      {
        "id": 1,
        "period": 1,
        "start_date": "2023-01-01",
        "end_date": "2023-12-31",
        "stock_name": "string",
        "indicator_id": 1
      }
    ]
    ```
Retrieves a list of scenes from the database.

### Backtests

#### Perform Backtest

- **Endpoint**: `/backtests/{scene_id}`
- **Method**: `POST`
- **Path Parameters**: `scene_id`
- **Response**:
    ```sh
    [
      {
        "id": 1,
        "scene_id": 1,
        "gross_profit": 1000.0,
        "net_profit": 900.0,
        "number_of_trades": 10,
        "winning_trades": 7,
        "losing_trades": 3,
        "max_drawdown": 5.0,
        "sharpe_ratio": 1.5,
        "created_at": "2023-01-01T00:00:00Z"
      }
    ]
    ```
Performs a backtest based on the provided scene ID and returns the results.

### Backtest Results

#### Read Backtest Results

- **Endpoint**: `/backtest_results/`
- **Method**: `GET`
- **Query Parameters**:
  - `skip` (default: 0)
  - `limit` (default: 10)
- **Response**:
    ```sh
    [
      {
        "id": 1,
        "scene_id": 1,
        "gross_profit": 1000.0,
        "net_profit": 900.0,
        "number_of_trades": 10,
        "winning_trades": 7,
        "losing_trades": 3,
        "max_drawdown": 5.0,
        "sharpe_ratio": 1.5,
        "created_at": "2023-01-01T00:00:00Z"
      }
    ]
    ```
Retrieves a list of backtest results from the database.

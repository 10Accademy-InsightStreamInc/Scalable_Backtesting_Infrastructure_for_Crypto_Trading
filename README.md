# Scalable Crypto Backtesting Infrastructure

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
├── data/
├── scripts/
│   └── download_data.py
├── tests/
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
└── README.md
```
## Contributors
- Abubeker Shamil
- Addisu Alemu
- Michael George 
- Sheila Murugi

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

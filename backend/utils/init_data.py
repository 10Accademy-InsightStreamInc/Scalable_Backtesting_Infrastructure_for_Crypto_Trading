import json
from sqlalchemy.orm import Session
from backend.models import Stock, Indicator

def initialize_data(db: Session):

    print("Initializing data Population...")

    # Check if stocks table is empty
    if db.query(Stock).count() == 0:

        with open('backend/data/stocks.json') as f:
            stocks = json.load(f)

        print("Populating stocks table...")

        for stock in stocks:
            db.add(Stock(**stock))
        db.commit()

    # Check if indicators table is empty
    if db.query(Indicator).count() == 0:

        with open('backend/data/indicators.json') as f:
            indicators = json.load(f)

        print("Populating indicators table...")
        
        for indicator in indicators:
            db.add(Indicator(**indicator))
        db.commit()

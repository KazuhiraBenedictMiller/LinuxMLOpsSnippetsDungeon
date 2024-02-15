import pymongo
import pandas as pd
import sys

def ConnectMongoDB():
    # Connect to MongoDB
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["YOUR_MongoDB_Database"]
        collection = db["TestCollection"]
        return collection
        
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection = ConnectMongoDB()

    # Example data for SOME_LIST
    SOME_LIST = [{"Date": "2024-02-15 10:00:00", "Close": 25.5},
                 {"Date": "2024-02-15 11:00:00", "Close": 30.2}]

    # Insert data into MongoDB
    if collection:
        collection.insert_many(SOME_LIST)

    # Check Inserted Data
    check_data = collection.find({}, {"_id": 0})  # Exclude _id field from results
    checkdf = pd.DataFrame(list(check_data))
    print(checkdf)

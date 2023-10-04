
# Imports
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Database connection && objects preparation
Base = automap_base()
db_url = "postgresql+psycopg2://my_user:secret@127.0.0.1/my_database"
engine = create_engine(db_url)
engine.echo = True
# Save database model into Base variable
Base.prepare(engine, reflect=True)

FoodItem = Base.classes.fooditem
session = Session(engine)
result = session.query(FoodItem).all()

# Check where I am and set to custom directory
from os import getcwd, chdir
chdir(r"C:\Users\localadmin\PycharmProjects\Python-2023_ola\17_Wykorzystanie_baz_danych")
print("Current directory is: ", getcwd())

# Convert csv to dict
import pandas as pd
dataframe = pd.read_csv("foods.csv")
columns_mapping = {"Food ID":"id", "Food Item":"name", "Price":"price"}
dataframe = dataframe.rename(columns=columns_mapping)
print("Dataframe: ", dataframe)
dict_data = dataframe.to_dict("records")
print("Dictionary to be load: ", dict_data)

# Create rows objects
items = [FoodItem(**item) for item in dict_data]
print("Object prepared: ", items)
# Open transaction to database and insert objects
session.bulk_save_objects(items)
# Close transaction (aka save database)
session.commit()
print("Success.")
import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine
import csv


Base = automap_base()
db_url = "postgresql+psycopg2://my_user:secret@127.0.0.1/my_database"
engine = create_engine(db_url)

# reflect the tables
Base.prepare(engine, reflect=True)

class Foods_csv(Base):
    __tablename__ = 'foods_csv'

    id = sa.Column('id', sa.Integer, primary_key=True)
    item = sa.Column('name', sa.Text)
    price = sa.Column('price', sa.Numeric(14,2))

Base.metadata.create_all(engine)

with open('foods.csv') as f:
    lista=[]
    reader = csv.DictReader(f)
    for row in reader:
        lista.append(row)
lista

lista2=[{'id': item.get("Food ID"),'name':item.get('Food Item'),'price':item.get('Price')} for item in lista]
lista2

# Imports
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import csv

# Database connection && objects preparation
Base = automap_base()
db_url = "postgresql+psycopg2://my_user:secret@127.0.0.1/my_database"
engine = create_engine(db_url)
engine.echo = True
# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
FoodItem = Base.classes.fooditem
session = Session(engine)
result = session.query(FoodItem).all()




##################
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import csv

Base = automap_base()
db_url = "postgresql+psycopg2://my_user:secret@127.0.0.1/my_database"
engine = create_engine(db_url)
engine.echo = True
# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
FoodItem = Base.classes.fooditem
session = Session(engine)
result = session.query(FoodItem).all()
n = 1
for row in result:
    print(row.__dict__)
    n += 1

with open('foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item_id = int(row["Food ID"])+n
        name = row["Food Item"]
        price = float(row["Price"])
        item = FoodItem(id=item_id, name=name, price=price)
        session.add(item)

    session.commit()
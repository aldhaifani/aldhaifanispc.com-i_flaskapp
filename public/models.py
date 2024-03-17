from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

import os
import base64


Base = declarative_base()


class orders_tbl(Base):
    __tablename__ = "orders_tbl"

    id = Column("id", Integer, primary_key=True)
    date = Column("date", String(50))
    order_qty = Column("order_qty", Integer)
    customer_name = Column("customer_name", String(50))
    phone_number = Column("phone_number", String(50))
    email = Column("email", String(100))
    completed = Column("completed", Boolean, default=False)
    location = Column("location", String(256))
    notes = Column("notes", String(256), default="")

    def __init__(
        self,
        date,
        order_qty,
        customer_name,
        phone_number,
        email,
        location,
        notes="",
        completed=False,
    ):
        self.date = date
        self.order_qty = order_qty
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.email = email
        self.location = location
        self.completed = completed
        self.notes = notes

    def __repr__(self):
        return "{}\nid: {}\nQty: {}\nName: {}\nPhone: {}\nEmail: {}\nCompleted: {}\nLocation: {}\nNotes: {}".format(
            self.date,
            self.id,
            self.order_qty,
            self.customer_name,
            self.phone_number,
            self.email,
            self.completed,
            self.location,
            self.notes,
        )


user = base64.b64decode(os.environ.get("orders_db_usr").encode("utf-8")).decode("utf-8")
password = base64.b64decode(os.environ.get("orders_db_pass").encode("utf-8")).decode(
    "utf-8"
)

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@72.167.207.37/orders", echo=False
)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

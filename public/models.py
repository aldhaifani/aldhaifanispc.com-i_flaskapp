from public import db


def add_to_session(order):
    db.session.add(order)


def commit_to_session():
    db.session.commit()


class orders_tbl(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    date = db.Column("date", db.String(50))
    order_qty = db.Column("order_qty", db.Integer)
    customer_name = db.Column("customer_name", db.String(50))
    phone_number = db.Column("phone_number", db.String(50))
    email = db.Column("email", db.String(100))
    location = db.Column("location", db.String(256))
    completed = db.Column("completed", db.Boolean, default=False)
    notes = db.Column("notes", db.String(256))

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

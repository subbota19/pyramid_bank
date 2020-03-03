from bank_system.model import meta


class Client(meta.Base.base):
    __tablename__ = "clients"
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(40), nullable=False, unique=True)
    password = meta.Column(meta.String(20), nullable=False)

    client_card = meta.relationship('Card', back_populates='card_client', passive_deletes=True)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return self.name


class Bank(meta.Base.base):
    __tablename__ = "banks"
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(40), nullable=False, unique=True)
    negative_percent = meta.Column(meta.DECIMAL(precision=3, scale=2), default=0.00)
    budget = meta.Column(meta.DECIMAL(precision=9, scale=2))
    creation_date = meta.Column(meta.DateTime, nullable=False)

    bank_card = meta.relationship('Card', back_populates='card_bank', passive_deletes=True)

    def __init__(self, name, negative_percent, budget):
        self.name = name
        self.negative_percent = negative_percent
        self.budget = budget
        self.creation_date = meta.datetime.datetime.now()

    def __repr__(self):
        return self.name


class Card(meta.Base.base):
    __tablename__ = 'cards'
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(60), nullable=False, unique=True)
    password = meta.Column(meta.String(20), nullable=False)
    budget = meta.Column(meta.DECIMAL(precision=7, scale=2))
    creation_date = meta.Column(meta.DateTime, nullable=False)

    bank_id = meta.Column(meta.Integer, meta.ForeignKey('banks.id', ondelete='CASCADE'), nullable=False)
    client_id = meta.Column(meta.Integer, meta.ForeignKey('clients.id', ondelete='CASCADE'), nullable=False)

    card_client = meta.relationship('Client', back_populates='client_card')
    card_bank = meta.relationship('Bank', back_populates='bank_card')

    def __init__(self, name, password, budget, client_id, bank_id):
        self.name = name
        self.password = password
        self.budget = budget
        self.client_id = client_id
        self.bank_id = bank_id
        self.creation_date = meta.datetime.datetime.now()

    def __repr__(self):
        return self.name


class Operation(meta.Base.base):
    __tablename__ = "operations"
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(60), nullable=False)
    cost = meta.Column(meta.DECIMAL(precision=5, scale=2))
    creation_date = meta.Column(meta.DateTime, nullable=False)

    card = meta.relationship('Transaction', back_populates='operation', passive_deletes=True)

    def __init__(self, name, cost=0):
        self.name = name
        self.cost = cost
        self.creation_date = meta.datetime.datetime.now()

    def __repr__(self):
        return self.name


class Transaction(meta.Base.base):
    __tablename__ = 'transactions'
    id = meta.Column(meta.Integer, primary_key=True)
    operation_id = meta.Column(meta.Integer, meta.ForeignKey('operations.id', ondelete='CASCADE'), nullable=False)
    card_id_received = meta.Column(meta.Integer, meta.ForeignKey('cards.id', ondelete='CASCADE'), nullable=False)
    card_id_send = meta.Column(meta.Integer, meta.ForeignKey('cards.id', ondelete='CASCADE'), nullable=False)
    creation_date = meta.Column(meta.DateTime)
    status = meta.Column(meta.Boolean)

    operation = meta.relationship('Operation', back_populates='card')
    card_r = meta.relationship('Card', foreign_keys=[card_id_received])
    card_s = meta.relationship('Card', foreign_keys=[card_id_send])

    def __init__(self, operation_id, card_id_send, card_id_received, status=False):
        self.operation_id = operation_id
        self.card_id_received = card_id_received
        self.card_id_send = card_id_send
        self.status = status
        self.creation_date = meta.datetime.datetime.now()

    def __repr__(self):
        return 'card_recipient:{},card_sender:{},operation_name:{}'.format(self.card_r.name, self.card_s.name,
                                                                           self.operation.name)

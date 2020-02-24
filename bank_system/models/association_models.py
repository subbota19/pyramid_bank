from bank_system.models import meta


class Admin(meta.Base.base):
    __tablename__ = "admins"
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(40), nullable=False)
    password = meta.Column(meta.String(20), nullable=False)
    creation_date = meta.Column(meta.DateTime, nullable=False)

    client_id = meta.Column(meta.Integer, meta.ForeignKey('clients.id'))

    admin_bank = meta.relationship('Bank', back_populates='bank_admin')
    admin_client = meta.relationship('Client', back_populates='client_admin')

    def __init__(self, password, name):
        self.creation_date = meta.datetime.datetime.now()
        self.name = name
        self.password = password

    def __repr__(self):
        return self.name


class Client(meta.Base.base):
    __tablename__ = "clients"
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(40), nullable=False)
    password = meta.Column(meta.String(20), nullable=False)

    card_id = meta.Column(meta.Integer, meta.ForeignKey('cards.id'), nullable=False)

    client_card = meta.relationship('Card', back_populates='card_client')
    client_admin = meta.relationship('Admin', back_populates='admin_client')

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return self.name


class Bank(meta.Base.base):
    __tablename__ = "banks"
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(40), nullable=False)
    negative_percent = meta.Column(meta.DECIMAL(precision=3, scale=2), default=0.00)
    budget = meta.Column(meta.DECIMAL(precision=5, scale=2))
    creation_date = meta.Column(meta.DateTime, nullable=False)

    card_id = meta.Column(meta.Integer, meta.ForeignKey('cards.id'))
    admin_id = meta.Column(meta.Integer, meta.ForeignKey('admins.id'))

    bank_admin = meta.relationship('Admin', back_populates='admin_bank')
    bank_card = meta.relationship('Card', back_populates='card_bank')

    def __init__(self, name, negative_percent, budget, admin_id, card_id):
        self.name = name
        self.negative_percent = negative_percent
        self.budget = budget
        self.card_id = card_id
        self.admin_id = admin_id
        self.creation_date = meta.datetime.datetime.now()

    def __repr__(self):
        return self.name


class Card(meta.Base.base):
    __tablename__ = 'cards'
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(60), nullable=False)
    password = meta.Column(meta.String(20), nullable=False)
    budget = meta.Column(meta.DECIMAL(precision=5, scale=2))
    creation_date = meta.Column(meta.DateTime, nullable=False)

    operation = meta.relationship('Transaction', back_populates='card')
    card_client = meta.relationship('Client', back_populates='client_card')
    card_bank = meta.relationship('Bank', back_populates='bank_card')

    def __init__(self, name, password, budget):
        self.name = name
        self.password = password
        self.budget = budget
        self.creation_date = meta.datetime.datetime.now()

    def __repr__(self):
        return self.name


class Operation(meta.Base.base):
    __tablename__ = "operations"
    id = meta.Column(meta.Integer, primary_key=True)
    name = meta.Column(meta.String(60), nullable=False)
    cost = meta.Column(meta.DECIMAL(precision=5, scale=2))
    creation_date = meta.Column(meta.DateTime, nullable=False)

    card = meta.relationship('Transaction', back_populates='operation')

    def __init__(self, name, cost):
        self.creation_date = meta.datetime.datetime.now()
        self.name = name
        self.cost = cost

    def __repr__(self):
        return self.name


class Transaction(meta.Base.base):
    """This model allows to create relation between Card and Operation model"""

    __tablename__ = 'transactions'
    id = meta.Column(meta.Integer, primary_key=True)
    operation_id = meta.Column(meta.Integer, meta.ForeignKey('operations.id'), nullable=False)
    card_id = meta.Column(meta.Integer, meta.ForeignKey('cards.id'), nullable=False)

    operation = meta.relationship('Operation', back_populates='card')
    card = meta.relationship('Card', back_populates='operation')

    def __init__(self, operation_id, card_id):
        self.operation_id = operation_id
        self.card_id = card_id

    def __repr__(self):
        return 'card_name:{},operation_name:{}'.format(self.card.name, self.operation.name)

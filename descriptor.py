class Value:
	"""
	Descriptor class to customize objects' attribute lookup, storage and deletion.
	"""
    def __init__(self, amount=None):
        self.amount = amount

    def __set__(self, obj, value):
        self.amount = value * (1 - obj.commission)

    def __get__(self, obj, obj_type):
        return self.amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


a = Account(100)
print(a.amount)

class Value:
    def __init__(self):
        self.netto = None

    def __get__(self, obj, obj_type):
        return self.netto

    def __set__(self, obj, value):
        self.netto = (1-obj.commission)*value
        return self.netto

class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)

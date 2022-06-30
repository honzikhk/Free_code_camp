# line 92 not nice slicing [0:-1]

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []        # moved from "under - class Category:". Now the ledgers are separated

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})   # "format" makes strings

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": - amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        changes = [i["amount"] for i in self.ledger]
        return sum(changes)

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __repr__(self):
        result = ""
        stars_before = (30 - len(self.name)) // 2
        if len(self.name) % 2 == 0:
            stars_after = stars_before
        else:
            stars_after = stars_before + 1

        result += stars_before * "*" + self.name + stars_after * "*" + "\n"
        for item in self.ledger:
            description = item["description"][0:23]
            result += str(description) + (30 - len(description) - len(format(item["amount"], ".2f"))) * " " + format(item["amount"], ".2f")
            result += "\n"
        result += "Total: " + str(self.get_balance())
        return result


def create_spend_chart(list_of_categories):
    list_of_withdraws = []
    sum_of_all_withdraw = 0
    list_of_names_categories = []       # make list of names for easier manipulation on chart

    for cat in list_of_categories:
        list_of_withdraws.append(extract_withdraws(cat))

    for cat in list_of_withdraws:
        for key, value in cat.items():
            sum_of_all_withdraw += value
            list_of_names_categories.append(key)        # make list of names for easier manipulation on chart

    for cat in list_of_withdraws:
        calculate_percentages(cat, sum_of_all_withdraw)

    result = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        result += ((3 - len(str(i))) * " " + str(i) + "| ")         # 100|
        for withdraw in list_of_withdraws:
            for key, value in withdraw.items():
                if value >= i:
                    result += "o  "
                else:
                    result += "   "
        result += "\n"                                                 # 0|

    result += 4 * " " + "-" + len(list_of_categories) * "---"           # ---------------------
    result += "\n"

    for i in range(len(max(list_of_names_categories, key=len))):
        result += 5 * " "
        for name in list_of_names_categories:
            try:
                result += name[i] + "  "
            except:
                result += "   "
        result += "\n"
    return result[0:-1]


def calculate_percentages(cat, sum_of_all_withdraw):       # receive dictionary of one category {"food": 105.55} and sum all withdraw (100%)
    for key, value in cat.items():
        cat[key] = ((cat[key] / (sum_of_all_withdraw / 100)) // 10) * 10
    return cat


def extract_withdraws(cat):     # helper of ->create_spend_chart<-. Returns dictionary {cat: withdraw}
    withdraws = {cat.name: 0}
    for record in cat.ledger:
        if record["amount"] < 0:
            withdraws[cat.name] -= record["amount"]
    return withdraws

"""
food = Category("Food")
food.deposit(1000, "just deposit")
# print(food.ledger)

food.withdraw(105.55, "pizza")
# print(food.get_balance())
print(food)
clothing = Category("Clothing")
clothing.deposit(2534, "salary")

clothing.withdraw(33.4, "shoes")
clothing.withdraw(53.85, "jacket")
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(10.99, "what?")
# print(food.get_balance())
# print(food)
# print(clothing.get_balance())
print(clothing)

print(create_spend_chart([clothing, food]))
"""
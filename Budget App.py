class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    
    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})
 
    def withdraw(self,amount,description=""):
        sum=0
        for i in self.ledger:
            sum +=i["amount"]
        if sum>amount:   
            self.ledger.append({"amount": amount*-1, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        blance=0
        for i in self.ledger:
            blance +=i["amount"]
        return blance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False   
        
    def check_funds(self,amount):
        sum=0
        for i in self.ledger:
            sum +=i["amount"]
        if sum>=amount:   
            return True
        else:
            return False

    def __str__(self):
        bas = (30 - len(self.name)) // 2
        result = bas * "*" + self.name + bas * "*" + "\n"
        for i in self.ledger:
            result += f"{i['description'][:23]:23}" + f"{i['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance()}"
        result += total
        return result
            

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    
    
    total_spent = sum(-transaction['amount'] for category in categories for transaction in category.ledger if transaction['amount'] < 0)
    
    
    percentages = [sum(-transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0) / total_spent * 100 for category in categories]
    
   
    for i in range(100, -1, -10):
        line = f"{i:3}| "
        for percent in percentages:
            if percent >= i:
                line += "o  "
            else:
                line += "   "
        chart += line + "\n"
    
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    
    max_name_length = max(len(category.name) for category in categories)
    
    
    for i in range(max_name_length):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += f"{category.name[i]}  "
            else:
                line += "   "
        if i < max_name_length - 1:
            line += "\n"
        chart += line
    
    return chart
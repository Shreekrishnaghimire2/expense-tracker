


def add_expense(expenses,name,amount,category):
   
   
    if not name or name.strip() =="":
        return False
    elif not isinstance(amount,(int,float)) or amount <= 0:
        return False
    
    new_expenses= {
        "name":name.strip(),
        "amount":amount,
        "category":category
        }
    expenses.append(new_expenses)
    return True
def total_spent(expenses):
    if len(expenses) == 0:
        return 0
    else:
        total = 0
        for item in expenses:
            total += item['amount']
        return total
def spending_by_category(expenses):
    categories ={}
    for expense in expenses:
       new_category = expense["category"].lower()
       new_amount = expense["amount"]
       if new_category in categories:
            categories[new_category] =  categories[new_category] + new_amount
       else:
           categories[new_category]= new_amount    
    return categories
def main():
  
    while True:
        print("1.Add Expense")
        print("2. Show Total")
        print("3. Show Spending by Category")
        print("4. Exit")
        try:
            choose = int(input("Enter your Choice"))
            
        except ValueError:
            print("Invalid Input")
            continue

        if choose ==1:
            name = input("Enter the name of the expense")
            amount = input("Enter amount")
            try:
                amount =float(amount) 

            except ValueError:
                print('Invalid Input')
                continue
            if amount<=0:
                print("Invalid Input")
                continue
       
            category = input("Enter the category of the Particular Expense")
            if add_expense(expenses,name,amount,category):
              print("Added")
              save_expenses(expenses,"expenses.json")
            else:
                print("Invalid input")
               
        elif choose ==2:
            print("Total spent is",total_spent(expenses))
        elif choose ==3:
            print(spending_by_category(expenses))
        elif choose ==4:
            print("Bye Bye")
           
            break
        else:
            print("Invalid Choice")
def save_expenses(expenses,filename):
   
    import json
    with open(filename,"w") as f:
        json.dump(expenses,f)
def load_expense(filename):
   
    import json
    try:
      with open(filename,"r") as f:
        data = json.load(f)
        return data
    except FileNotFoundError:
        print("There is nothing named such file")
        return []
    except json.JSONDecodeError:
        print("The file is empty or not in valid JSON format")
        return []
expenses = []
# Load existing expenses if the file exists
if __name__ =="__main__":
    expenses = load_expense("expenses.json")

    main()



    

       

    
    
     
       
    


from os import name as osName, system as osSystem
from sys import exit as closeProcess
from time import sleep as delay
Configuration = {
    "Store": {
        "products": { 
            "drinks":["Gatorade","Sprite" ,"Summit" ,"Vitamilk","Mountain Dew"],
            "foods": ["Hamburger","Siomai","Spaghetti", "Footlong"]
        },

        "prices": {
            "drinks":[12.00 , 10.00 , 30.00, 12.00 ,12.00],
            "foods":[20.00 , 75.00 , 30.00, 40.00]
        }
    },

    "cartProducts": {
        "product":[],
        "quantity":[],
        "price":[]

    },
    "loginCredential": {
        "username":"admin",
        "password": "12345",
        
    }
}
productCollection = []
quantityCollection = []
productPrice = []


def clearConsole():
    if osName == "nt":
        osSystem("cls")
    else:
        osSystem("clear")

def Login():
    clearConsole()
    attemptCount = 1
    completeAttempts = 3
    print("--------------------------------------")
    print("--------------------------------------")
    print("-----------Please Login--------------")
    print("--------------------------------------")
    print("--------------------------------------")
    
    while True:
        if completeAttempts == 2 or completeAttempts <= 2:
            print("Remaining attempts:{0}".format(completeAttempts))
        completeAttempts = completeAttempts - 1
        usernameField = input(str("Enter Username:"))
        passwordField = input(str("Enter Password:"))
        if usernameField != Configuration['loginCredential']['username']:
            clearConsole()
            print("Invalid Username, Please Try again!")
            if attemptCount >= Configuration['loginCredential']['attempts']:
                clearConsole()
                closeProcess()
                break
            attemptCount = attemptCount + 1
            continue
        if passwordField != Configuration['loginCredential']['password']:
            delay(2)
            clearConsole()
            print("Invalid Password, Please Try again!")
            if attemptCount >= Configuration['loginCredential']['attempts']:
                clearConsole()
                closeProcess()
                break
            attemptCount = attemptCount + 1
            continue
        if usernameField == Configuration['loginCredential']['username'] and passwordField == Configuration['loginCredential']['password']:
            
            while True:
                clearConsole()
                print("1. Shop")
                print("2. Logout")
                option = input(str("choose option above:"))
                if option == 1 or option == "1":
                    delay(2)
                    showStore()
                    break
                elif option == 2 or option == "2":
                    main()
                    break
                else:
                    print("invalid value!")
                    clearConsole()
                    continue
            break

        




def CartProducts(products , quantities , prices):
    clearConsole()
    grandTotal = 0
   
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    print("-------------------CART ITEMS-------------------------------")
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    for product in products:
        Configuration['cartProducts']['product'].append(product)
    for quantity in quantities:
        Configuration['cartProducts']['quantity'].append(quantity)
    for price in prices:
        Configuration['cartProducts']['price'].append(price)

    productCart = len(Configuration['cartProducts']['product'])
    print("product inside your cart:{0}".format(productCart))
    index = 0
    productNumber = 1
    print("Product\t\tprice\t\tQuantity\ttotal price")
    while index < len(Configuration['cartProducts']['product']):
        computeTotal = Configuration['cartProducts']['price'][index] * Configuration['cartProducts']['quantity'][index]

        grandTotal = grandTotal  + computeTotal
        print("{0}.{1}\t{2} php\t{3}\t\t{4} php".format(productNumber , Configuration['cartProducts']['product'][index] , Configuration['cartProducts']['price'][index] , Configuration['cartProducts']['quantity'][index] ,computeTotal))
        index = index + 1
        productNumber = productNumber + 1

    
    print("___________________________________________________________")
    print("\t\t\t\t    grand total:{0} {1}".format(grandTotal, "php"))
    
    print("")
    
    print("1. Buy")
    print("2. add more products")
    print("3. Cancel product")
    change = 0
    while True:
        option = input(str("choose option above:"))
        money = 0
        if option == 1 or option == "1":
            while True:
                option = input("enter the your money:")
                try:
                    money = int(option)
                    if money >= grandTotal:
                        change = money - grandTotal
                        break
                    elif money < grandTotal:
                        print("Insuficient Money!")
                        continue
                except ValueError:
                    print("invalid value!")
                    continue
               
            print("Transaction Success!")
            print("your money: {0}".format(money))
            print("your change: {0}".format(change))
           
            while True:
                print("1. Yes")
                print("2. logout")
                option = input(str("go back to store?:"))
                if option == 1 or option == "1":
                    productCollection.clear()
                    quantityCollection.clear()
                    productPrice.clear()
                    Configuration['cartProducts']['product'].clear()
                    Configuration['cartProducts']['quantity'].clear()
                    Configuration['cartProducts']['price'].clear()
                    showStore()
                    break
                if option == 2 or option == "2":
                    productCollection.clear()
                    quantityCollection.clear()
                    productPrice.clear()
                    Configuration['cartProducts']['product'].clear()
                    Configuration['cartProducts']['quantity'].clear()
                    Configuration['cartProducts']['price'].clear()
                    main()
                    break
                else:
                    print("invalid input!")
                    continue
        elif option == 2 or option == "2":
            productCollection.clear()
            quantityCollection.clear()
            productPrice.clear()
            clearConsole()
            showStore()
            break
        elif option == 3 or option == "3":
            print('1. Yes')
            print("2. No")
            while True:
                option = input(str("cancel products?:"))
                if option == 1 or option == "1":
                    productCollection.clear()
                    quantityCollection.clear()
                    productPrice.clear()
                    Configuration['cartProducts']['product'].clear()
                    Configuration['cartProducts']['quantity'].clear()
                    Configuration['cartProducts']['price'].clear()
                    showStore()
                    break
                elif option == 2 or option == "2":
                    Configuration['cartProducts']['product'].clear()
                    Configuration['cartProducts']['quantity'].clear()
                    Configuration['cartProducts']['price'].clear()
                    CartProducts(productCollection, quantityCollection , productPrice)
                    break
                else:
                    print("invalid value!")
                    continue
        else:
            print("invalid value!")
            continue

def RedirectcalculateCartProduct():
    calculateCartProduct()

def calculateCartProduct():
   
    while True:
        indexProduct = 0
        productName = 0
        option = input("what would you like to buy:")
        try:
            productName = int(option)
            if productName >= 1 and productName <= 9 and productName != 0:
                if productName <= 4 or productName == 4 and productName  != 0:
                    if productName == 1:
                        indexProduct = 0
                    elif productName == 2:
                        indexProduct = 1
                    elif productName == 3:
                        indexProduct = 2
                    elif productName == 4:
                        indexProduct = 3
                    productCollection.append(Configuration['Store']['products']['foods'][indexProduct])
                    productPrice.append(Configuration['Store']['prices']['foods'][indexProduct])
                    
                    while True:
                        productQuantity = int(input("how many quantity:"))
                        if productQuantity >= 1 and productQuantity != 0:
                            quantityCollection.append(productQuantity)
                            break
                        else:
                            print("invalid value")
                            continue
                    del indexProduct
                    del productName
                elif productName >= 5 and productName <= 9:
                    if productName == 5:
                        indexProduct = 0
                    elif productName == 6:
                        indexProduct = 1
                    elif productName == 7:
                        indexProduct = 2
                    elif productName == 8:
                        indexProduct = 3
                    elif productName == 9:
                        indexProduct = 4

                    productCollection.append(Configuration['Store']['products']['drinks'][indexProduct])
                    productPrice.append(Configuration['Store']['prices']['drinks'][indexProduct])
                    
                    
                    while True:
                        productQuantity = int(input("how many quantity:"))
                        if productQuantity >= 1 and productQuantity != 0:
                            quantityCollection.append(productQuantity)
                            break
                        else:
                            print("invalid value")
                            continue
                    del indexProduct
                    del productName
                else:
                    continue
            
                print("1. Yes")
                print("2. No")
                while True:
                    option = input("would you like to add another product? choose option above:")
                    if option == 1 or option == "1":
                        calculateCartProduct()
                        break
                    elif option == 2 or option == "2":
                        delay(2)
                        CartProducts(productCollection , quantityCollection ,productPrice)
                        break
                    else:
                        print("invalid value!")
                        continue
                break
            else:
                print("invalid value!")
                continue
            break
        except ValueError:
            print("invalid value!")
            RedirectcalculateCartProduct()
            break
        

def showStore():
    clearConsole()
    product = ""
    counter = 1
    index = 0
    price = 0
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("------------PRODUCTS WE ARE SELLING --------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")

    productCart = len(Configuration['cartProducts']['product'])
    print("product inside your cart:{0}".format(productCart))
    print("A. Foods")
    print("Product\t\t Price")
    for foods in Configuration["Store"]["products"]["foods"]:
        product = foods
        print(("{0}. {1}\t{2} php".format(counter , product , Configuration['Store']['prices']['foods'][index])))
        counter = counter + 1
        index = index + 1
    print("B. Drinks")
    print("Product\t\t Price")
    index = 0
    for drinks in Configuration["Store"]["products"]["drinks"]:
        product = drinks
        print(("{0}. {1}\t{2} php".format(counter , product , Configuration['Store']['prices']['drinks'][index])))
        counter = counter + 1
        index = index + 1
    print("\n")

    calculateCartProduct()
    
        
        
        

def main():
    clearConsole()
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("-------------GEM SARI SARI STORE POS--------------")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print("1. Login")
    print("2. Exit the Program")
    while True:
        option = input("please choose an option:")
        if option == 1 or option == "1":
            delay(2)
            Login()
            break
        elif option == 2 or option == "2":
            print("1. Yes")
            print("2. No")
            while True:
                option = input(str("do you want to exit?"))
                if option == 1 or option == "1":
                    clearConsole()
                    closeProcess(0)
                elif option == 2 or option == "2":
                    clearConsole()
                    main()
        else:
            print("Invalid Option!")
            continue



if __name__ == "__main__":
    main()
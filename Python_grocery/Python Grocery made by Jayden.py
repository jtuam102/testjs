#TUAM CHUN WAI
#TP068683

# Groceries Management System

'''
MENU
'''

def menu ():    #Main menu of the system
    while (True):    #To keep looping the system until a correct input
        print ("Welcome to FRESHCO's Groceries Management System!\n")
        print ("1 for Admin")
        print ("2 for New Customer")
        print ("3 for Registered Customer")
        user = input("\nPlease select a user: ")  #User selection 
        
        if (user =="1"):  #To login as Admin
            admin_login ()
            admin_choose()
            
        elif (user == "2"):  #To login as New Customer
            new_customer ()

        elif (user=="3"):   #To login as Registed Customer
            login_username = reg_customer_login()
            regcustomer_menu (login_username)
            
        else:  #Error shown if input does not match the with options
            print ("Invalid Input, Please try again. \n")
            print ("")

            
'''
groceries
'''

def open_groceries():   #Functioning as a "groceries file" opener, returns the groceries into a list
    try:
        grocer = open("grocer.txt","r")    #Open "grocer text file" as READ
    except:
        print ("File can't be opened")      #Show error if file cannot be opened
        exit()

    masterlist_grocer = []           #Create a masterlist for groceries
    
    for groceries in grocer:      #Looping through the items line by line in "grocer text file"
        grocer_name,grocer_price, grocer_stock = groceries.strip().split(",")  #Split the item name, price and stock with comma (,)
        masterlist_grocer.append ([grocer_name,grocer_price, grocer_stock])   #Add the item name, price and stock into masterlist
    return (masterlist_grocer)    #Returns the masterlist



def groceries_view():   #For Admin, New and Registered Customer to view groceries 
    
    masterlist_grocer = open_groceries()    #Returning the values of masterlist groceries from function

    print ("\nItem \t\t\t Price(RM) \t\t        Stock")
    print ("=======================================================")
    for groceries in masterlist_grocer:    #Looping through the small lists in masterlist
        for x in groceries:     #Looping through the first small list
            print (x.ljust(45),end="")     #Printing the elements in first small list with 45 spaces between before moving to a new line
        print()   #Print a space line after every small lists

    print()
            
    
def groceries_upload():   #For Admin to upload groceries 
    itemExist=False    #Setting itemExist to False to allow only some of the statements to work
    masterlist_grocer = open_groceries()    #Returning the values of masterlist from function

    grocery_item = input ("Please input the grocery name: ")   #Reading input from user
    
    for items in masterlist_grocer:    #Looping through the small lists in masterlist
        name = items[0]   #Setting first element as grocery name
        if (grocery_item.lower() == name.lower()):   #If both of the grocery name and user input matches (Both are same in lowercase)
            print ("Item already exist\n")
            itemExist=True    #Avoid the function from running again, back to Admin Menu
            
    if itemExist==False:   #Runs function if itemExist remains False
            grocery_price = input ("Please input the grocery price: ")   
            grocery_stock = input ("Please input the grocery stock: ")  
            total = grocery_item +","+ grocery_price + "," + grocery_stock  #Combining the new item name,price and stock 
            print (grocery_item, "uploaded! \n")
            
            with open("grocer.txt","a") as t:   #Opens "grocer text file" as APPEND
                t.write("\n" + total)    #Append new items into "grocer text file"



def writetofile (masterlist_grocer):   #Functioning as to write the newest masterlist into "grocer text file"
    with open ("grocer.txt", "w") as f:  #Opens "grocer text file" as WRITE
        x = 0   #Set count to 0
        z = len(masterlist_grocer)   #Max length of masterlist
        
        while x < len(masterlist_grocer):  #Looping through the lists in masterlist using while loop iteration
            total = masterlist_grocer[x][0] + "," + masterlist_grocer[x][1] + "," + masterlist_grocer[x][2]  #Combining the new item name,price and stock 
            if (x==0) or ( x == z):  #Avoid printing lines at the first and last line when overwriting 
                f.write (total)

            else:
                f.write ("\n" + total )

            x = x + 1
            



'''
ADMIN
'''

def admin_login ():   #Login as Admin
    while(True):
        print ("\nLogin to admin (Press ENTER for MENU)")
        login_admin_1 = input("Enter Admin username: ")    #Reading Admin Username
        
        
        if (login_admin_1 == "ADMIN"):    #Validating Admin Username
            print ("Admin Username Valid. \n")

             
            login_admin_2 = input("Enter Admin password: ")   #Reading Admin Password
            if (login_admin_2 == "ADMIN"):   #Validating Admin Password
                print ("Admin Password Valid. \n")
                admin_choose ()    #Jumping to Admin Menu Function

            else:
                print ("Wrong Password, Please Re-enter!\n")
                


        elif (login_admin_1 == ""):    #Input Enter to go back Main Menu Function
            print("\n")
            menu()

        else:
            print ("Wrong username, Please Re-enter! \n")
            



def admin_choose ():  #Admin Menu
    while (True):
        print ("=======================================================")
        print ("Greatings, Admin!")
        print ("\n1 to Upload Groceries Detail")
        print ("2 to View all Groceries Detail")
        print ("3 to Modify Groceries Detail")
        print ("4 to Delete Groceries information")
        print ("5 to Search Groceries Detail")
        print ("6 to View order of customers")
        print ("7 to View all customers")
        print ("Press ENTER for MENU")

        admin_pick = input("\nPlease select your option: ")   #Reading Admin Options
        if (admin_pick == "1"):     #1 to Upload Groceries Detail
            groceries_upload() 
          
        elif (admin_pick == "2"):    #2 to View all Groceries Detail 
            groceries_view()

        elif (admin_pick == "3"):    #3 to View all Groceries Detail
            groceries_view()
            print ()
            modifygroceries ()

        elif (admin_pick == "4"):   #4 to Delete Groceries information
            groceries_view()
            print ()
            deletegroceries ()

        elif (admin_pick == "5"):    #5 to Search Groceries Detail
            groceries_view()
            print ()
            searchgroceries ()

        elif (admin_pick == "6"):  #View either all or specific customer's orders
            while (True):
                print ("\n1 to View all orders from customers")
                print ("2 to View specific orders from a customer")
                print ("ENTER to go back to Admin Menu\n")
                
                
                pick = input("Choose your option: ")
                
                if (pick == "1"):
                    vieworder ()
                    

                elif (pick == "2"):
                    viewspecific_order()

                
                elif (pick == ""):    #Input Enter to go back Main Menu Function
                    print("\n")
                    break

                else:
                    print ("Invalid Input, Please try again. \n")
                    

                
            print ('')

        elif (admin_pick == "7"):    #View either all or specific customers
            while (True):
                print ("\n1 to View all customers")
                print ("2 to View specific customer")
                print ("ENTER to go back to Admin Menu\n")
                
                pick = input("Choose your option: ")
                if (pick == "1"):
                    viewcustomer ()

                elif (pick == "2"):
                    viewspecific_customer()

                elif (pick == ""):
                    print()
                    break
                
                else:
                    print ("Invalid Input, Please try again. \n")
                    

        elif (admin_pick == ""):
            print("\n")
            menu()

            
        else:
            print ("Invalid Input, Please try again. \n")
            

def admin_vieworder ():    #Functioning as a "customer orders file" opener, returns the orders into a list
    cart_admin = []      #Creating masterlist for orders
    with open ("customerorder.txt", "r") as a:      #Open "customer order text file" as READ
        for customer in a:       #Looping through "customer order text file"
            customername,name,quantity,price = customer.strip().split(",")      #Split the customer name, item name, price and stock with comma (,)
            cart_admin.append([customername,name,quantity,price])      #Add the customer name, item name, price and stock into masterlist of orders

    return cart_admin   #Returns the value of masterlist of orders
            

def vieworder ():     #Functioning for Admin to view all customers orders
    cart_admin = admin_vieworder ()     #Retrieving the masterlist of orders from function
    print("Customer         Items        Quantity    Total Price(RM)")
    print("=========================================")
    
    for orders in cart_admin:   #Looping orders in masterlist of orders
        for order in orders:
            print (order.ljust(20),end="")  #Displaying all the elements per line of a single small list
        print("\n")


def viewspecific_order():     #Functioning as for Admin to view specific orders according to input
    cart_admin = admin_vieworder ()       #Retrieving the masterlist of orders from function
    
    userExist = False     #Setting userExist to False to allow only some of the statements to work
    
    user = input("Which customer order do you want to find: ")       #Reading specific customer name
    print("Customer         Items        Quantity    Total Price(RM)")
    print("=========================================")

    
    for orders in cart_admin:     #Looping orders in masterlist of orders
        for order in orders:
            if order.lower() == user.lower():    #Checking whether if the input and customer name matches
                print (orders[0].ljust(20),end="")
                print (orders[1].ljust(20),end="")
                print (orders[2].ljust(20),end="")     #ljust is a function for spacing 
                print (orders[3].ljust(20),end="")     #Display all the orders of the specific customer
                userExist = True     #Setting userExist to True to stop if statement below from activating
                print("\n")


    if userExist == False:     #If customer name is NOT in the masterlist of orders
        print("Customer Not Found!")


    
def writeadmin_vieworder(login_username, cart):    #Functioning as for Admin to record the payment into order lists
    cart_admin = admin_vieworder()      #Retrieving the masterlist of orders from function

    x = 0     #Sets count to 0
    while x < len(cart):      #Using while iteration to add current cart of the customer into the masterlist of orders
        cart[x][1] = str(cart[x][1]) 
        cart[x][2] = str(cart[x][2])   #Setting both integers into strings
        total = login_username,cart[x][0],cart[x][1],cart[x][2]       #Combining customer name, item name,quantity and total price
        cart_admin.append (total)   #Add the combination into the masterlist of orders 

        x = x + 1
                
    with open ("customerorder.txt", "w") as y:  #Open "customer orders file" as WRITE
        for customer in cart_admin: #Looping through masterlist of orders
            customer_all = customer[0] + "," + customer[1] + "," + customer[2] + ","  + customer[3]   #Combining elements of orders with comma (,)
            y.write(customer_all)  #Overwrites the combination into the "customer orders file"
            y.write("\n")


def modifygroceries ():     #Functioning as for Admin to edit the groceries list
    masterlist_grocer = open_groceries()      #Returning the values of masterlist groceries from function
    
    while (True):
        usersearch = input("What do you want to modify: ")      #Reading item name 
        groceryFound = False     #Setting groceryFound to False to allow only some of the statements to work

        for item in masterlist_grocer:    #Looping through masterlist of groceries
            if (usersearch.lower() == item[0].lower()):    #Checking whether if the input and grocery name matches
                
                while (True):       #Loop inputs until it matches the condition
                    newitem = input("Please input a new item name: ")     #Reading new item name 
                    newprice = input("Please input a new price: ")     #Reading new item price

                    try:     
                        newprice = int(newprice)     #try to convert price into integer 
                        print()
                        break       #break out of loop
                    
                    except:
                        print ("Please enter a valid number\n")

                    
                while (True):         #Loop inputs until it matches the condition
                    newstock = input("Please input a new stock: ")      #Reading new item stock

                    try:
                        newstock = int(newstock)     #try to convert stock into integer 
                        print()
                        break         #break out of loop
                    
                    except:
                        print ("Please enter a valid number\n")



                item[0] = newitem        #Replacing old item name 
                item[1] = str(newprice)  #Converting new price into string
                item[2] = str(newstock)   #Converting new stock into string
                groceryFound = True    #Setting groceryFound to True to avoid looping inputs
                break
                

        if groceryFound == True:     #Checking whether if all the conversion and inputs have no issues
            writetofile (masterlist_grocer)     #Jumps to writetofile function to update the groceries list
            print (usersearch, "edited successfully.")   
            break
                



def deletegroceries ():     #Functioning as for Admin to delete certain grocery 
    masterlist_grocer = open_groceries()    #Returning the values of masterlist groceries from function
    
    while (True):
        usersearch = input("What do you want to delete: ")   #Read search input
        groceryFound = False   #Setting groceryFound to False to allow only some of the statements to work

        t = 0
        while t < (len (masterlist_grocer)):    #Looping through the length of the masterlist groceries
            if (usersearch.lower() == masterlist_grocer[t][0].lower() ):
                masterlist_grocer.pop(t)     #Delete the small lists according to the given name
                groceryFound = True #Avoid the function from running again, go to write file instead
                break
            t = t + 1

        if groceryFound == False:    #If no item matches the input
            print("Grocery not found!")
            return

        else:
            writetofile (masterlist_grocer)    #Overwrites new masterlist grocery into file
            print (usersearch + " deleted!")
            break

                
    

def searchgroceries ():     #Functioning as for Admin to searcch certain grocery 
    
    masterlist_grocer = open_groceries()    #Returning the values of masterlist groceries from function

    while (True):    #Looping the search of groceries until it is found
        usersearch = input("What do you want to find: ")  #Reading input 
        groceryFound = False    #Setting groceryFound to False to allow only some of the statements to work
        for name in masterlist_grocer:   #Looping through masterlist of groceries
            if (usersearch.lower() == name[0].lower() ):   #Checking if item name matches with user input
                print ("Grocery is found!\n")
                print ("\nItem \t\t\t Price(RM) \t\t        Stock")
                print ("=======================================================")
                for others in name:    #Looping the elements in small lists
                    print (others.ljust(45),end="")   #Print elements with 45 spaces in between
                print("\n")
                groceryFound = True
                return
                
                    
        if groceryFound == False:   #If no item matches the input
            print("Grocery not found!")


def viewcustomer ():    #Functioning as for Admin to view all the registered customer 
    try:
        regfile = open("regcustomer.txt","r")   #Try to open latest "registered customer text file"

    except:
        print ("File can't be opened")  
        exit()

    masterlist_cusdata = []   #Creates a masterlist of registered customer
    print()
    
    for customer in regfile:    #Looping to Import data from "registered customer text file"
        username,password,name,gender,dob,address,email,number = customer.strip().split(";")[0:8]    #Splitting data with comma (,)
        masterlist_cusdata.append ([username,password,name,gender,dob,address,email,number])    #Add data into masterlist of registered customer

    
    print ("Username /Password/ Name/ Gender /  D.O.B   /     Address    /     Email   /  Phone Number")
    print("===========================================================\n")
    t = 0
    
    while (t < len(masterlist_cusdata)):  #Looping through masterlist of registered customer
        print (masterlist_cusdata[t])   #Print data line by line 
        print()
        t = t + 1


def viewspecific_customer():     #Functioning as for Admin to view specific registered customer 

    try:
        regfile = open("regcustomer.txt","r")     #Try to open latest "registered customer text file"
        
    except:
        print ("File can't be opened")
        exit()


    masterlist_cusdata = []         #Creates a masterlist of registered customer
    
    for customer in regfile:       #Looping to Import data from "registered customer text file"
        username,password,name,gender,dob,address,email,number = customer.strip().split(";")[0:8]    #Splitting data with comma (,)
        masterlist_cusdata.append ([username,password,name,gender,dob,address,email,number])      #Add data into masterlist of registered customer

    customerFound = False     #Setting customerFound to False to allow only some of the statements to work
    user = input("Which customer do you want to find: ")    #Read input 
    for name in masterlist_cusdata:  #Looping though masterlist of registered customers
        if user == name[0]:    #If input matches registered customer name
            print ("\nUsername /Password/ Name/ Gender /  D.O.B   /     Address    /     Email   /  Phone Number")
            print("===========================================================")
            print(name)   #Print the specific line of the registered customer detail
            print()
            customerFound = True     #Setting customerFound to True to end the loop
   
    if customerFound == False:     #If specific customer is NOT in the masterlist of registered customers
        print ("Customer not found.\n")



'''
New Customer
'''
    
def new_customer():    #New Customer Menu
    while (True):
        print ("\n=======================================================")
        print ("Greatings, NEW Customer!")
        print ("\n1 to View Groceries Detail")
        print ("2 to Sign up")
        print ("Press ENTER for MENU")
            
        new_customer_pick = input("\nPlease select your option: ")  #Read Input
            
        if (new_customer_pick == '1'):   #If new customer type 1
            groceries_view()
                

        elif (new_customer_pick == '2'):   #If new customer type 2
            new_customer_save ()


        elif (new_customer_pick == ""):    #If new customer type ENTER
            print("\n")
            menu()
            
        else:
            print ("Invalid, Try again\n")   #Otherwise
            

        

def new_customer_sign():    #Sign up for New customer
        
        masterlist = []   #Masterlist of customer detail
        new_cusdata = []     #Small list of customer detail

        new_id = input("\nPlease enter your new USERNAME ID : ")    #Read input
        new_cusdata.append (new_id)    #Add details to small list
        
        while (True):    #Validation for new password

            new_password_1 = input("Please enter your NEW PASSWORD : ")  #First new password
            new_password_2 = input("Please re-enter your NEW PASSWORD : ")  #Re-enter same password
            
            if (new_password_2 == new_password_1):    #Check if the passwords are the same
                print ("Pasword is matched. \n")
                new_cusdata.append (new_password_2)   #If same, it will add to small list
                break

            else:
                print ("Password is not the same!\n")   #Otherwise, repeat the process of enter new password
                

        new_name = input("\nPlease enter your name: ")
        new_cusdata.append (new_name)
        new_gender = input("Please enter your gender (male/female): ")
        new_cusdata.append (new_gender)
        new_dob = input("Please enter your date of birth (exp: 1/1/2022): ")
        new_cusdata.append (new_dob)

        new_address = input("Please enter your address: ")
        new_cusdata.append (new_address)
        new_email = input("Please enter your email: ")
        new_cusdata.append (new_email)
        new_number = input("Please enter your number: ")
        new_cusdata.append (new_number)

        masterlist.append(new_cusdata)  #Add the small list into masterlist of registered customer
        print ("Registered Successful!")
        return masterlist    #Returns the value masterlist 





def new_customer_save():   #Functioning to append new customers into "registered customer text file"
    try:
        regfile = open("regcustomer.txt","a")   #Opens "registered customer text file" as APPEND
    except:
        print ("File can't be opened")
        exit()
        
    masterlist = new_customer_sign()   #Retrieiving the value of masterlist new customers
    
    for new_cus in masterlist:   #Loop through small lists
        for nc in new_cus:    #Loop through elements in small lists 
            regfile.write(nc)   
            regfile.write(";")    #Write each element with semicolon in between
        regfile.write('\n')    #Writes a line for next new customer to register
    regfile.close()      #Close file to save details

    
    print ("\n")
    menu()    #Jumps back to Main menu



'''
Registerd Customer
'''
    
def reg_customer_login():   #Registered Customer Login
    try:
        regfile = open("regcustomer.txt","r")   #Opens "registered customer text file" as READ

    except:
        print ("File can't be opened")
        exit()


    login = False     #Setting login to False to allow only some of the statements to work
    masterlist_cusdata = []    #Opens a masterlist of registered customer
    
    for customer in regfile:   #Looping through the "registered customer text file and retrieve username and password
        username,password = customer.strip().split(";")[0:2]
        masterlist_cusdata.append ([username,password])   #Add all username and password into lists


    while (True):   
        reg_customer_login_1 = input("Please enter your USERNAME ID : ")            #Read Username Input
        reg_customer_login_2 = input("Please enter your Password : ")                   #Read Password Input

        for login_cred in masterlist_cusdata:    #Loop through small lists
            if (reg_customer_login_1 == login_cred[0]) and (reg_customer_login_2 == login_cred[1]):    #Check if inputs are correct according to username and password
                print ("\nLogin Success!\n")
                login = True       #Setting login to True to end the loop
                return reg_customer_login_1    #Returns the username into registered customer menu
            
        if (login == False):   #If inputs are not correct
                print("Login Failed.\n")
                menu()          #Jump back to Main menu

    
def regcustomer_menu(login_username):     #Registered Customer Menu
    cart = []     #Creates a cart that saves the orders returned by the functions related
    
    while (True):     #Looping the function if conditons does not match
            print ("=======================================================")
            print ("Greatings," + login_username + ".")
            print ("\n1 to View Groceries Detail")
            print ("2 to Place Order")
            print ("3 to View OWN Order")
            print ("4 to Do payment")
            print ("5 to View OWN personal information")
            print ("Press ENTER for MENU\n")

            user = input("Please choose your option: ")   #Read input
            if (user == "1"):
                groceries_view()

            elif (user =="2"):
                groceries_view()   #Shows groceries before entering order
                cart = regcustomer_order(cart)
                                            

            elif (user =="3"):
                viewcart (cart)

                
            elif (user =="4"):
                if len(cart) != 0:   #Registered Customer can only go back to Main menu when cart is empty
                    payment(login_username, cart)
                    break

                else:
                    print("\nCART IS EMPTY!\n")
                    
                
            elif (user == "5"):
                viewpersonal_info (login_username)
                
            elif (user == ""):
                if len(cart) == 0:
                    print("\n")
                    menu()

                else:
                    print("\n")
                    print ("You have to make payment before exiting Registered Customer Menu!")
                    print("\n")
                    

                    
            else:
                print ("Invalid, Try again\n")

    return cart  #Return the cart values

        
            
def regcustomer_order(cart):

    
    masterlist_grocer = open_groceries()   #Returning the values of masterlist groceries from function

    print ()

    while (True):   #Loop function
        
        itemExists = False     #Setting itemExists to False to allow only some of the statements to work
        user = input("What do you want to buy: ")   #Read input
        
        for item in masterlist_grocer:    #Looping through the masterlist of groceries
            name = item[0]  #Set first element as name
            price = item[1]    #Set second element as price
            stock = item [2]    #Set thrid element as stock
            price = int(price)     
            stock = int(stock)   #Sets both price and stock as integer for calculation 

            if (user.lower() == name.lower()):    #Checking if input matches with grocery name
                user_quantity = input("How many do you want to buy: ")   #Reads quantity input

                try:
                    user_quantity = int(user_quantity)    #Sets quantity input as integer with try
                    if (user_quantity <= stock) and (stock > 0 ):   #Checks again if there is sufficient stocks for customer to purchase
                        quan = stock - user_quantity   #Minus stocks according to input
                        total_price = price * user_quantity  
                        total_price = str(total_price)     #Calculate total price and turns it to string, so that there is no errors when concatenating strings
                        item[2] = str(quan)  #Sets latest stock to string
                        itemFound = True      #Setting itemFound to True to run certain statement
                        
                        if len(cart) != 0:    #Checking if the customer bought the same item
                            for item in cart:   #Looping through current cart
                                if item [0] ==user:    #If there is a same item previously bought in cart
                                    item_quantity = str(int(item[1]) + int(user_quantity))   #Updates the the total quantity
                                    item_price = str(int(item[2]) + int(total_price))       #Updates the total price
                                    item[1] = item_quantity  #Replace old total quantity with new total quantity 
                                    item[2] = item_price     #Replace old total price with new total price 
                                    itemFound = False     #Setting itemFound to False to avoid redundancy

                        if itemFound == True:  #If items bought are different from previous ones
                            cart.append ([name, user_quantity, total_price])   #New items will be added to cart

                        stock = str(stock)    #Sets latest stock to string
                        writetofile (masterlist_grocer)  #Overwrites masterlist of groceries with function
                        print (name + " added to cart.")
                        itemExists = True   #Setting itemExists to True to stop looping
                        return cart   #Returns the newest cart value
                    
                        
                    else:
                        print ("Quantity not valid")
                        return cart

                except:
                    print("Quantity not valid")
                    return cart
                        
        if itemExists == False:   #If no item is found in masterlist of groceries
            print ("Item is unavailable!!")
            return cart


                    
def viewcart (cart):   #Functions as for registered customer to view cart
    print ("\nThis is your cart list\n")
    print ("Item \t\t\t  Quantity     \t\t        Total Price (RM)")
    print ("=======================================================")
    items = False  #Setting item to False to avoid repetition 

    for groceries in cart:   #Looping through the small lists of the cart
            for x in groceries: #Looping through each element
                x = str(x)   #Set each element as string
                print (x.ljust(45),end="")    #Print out the elements in small lists in one line with 45 spaces between
                items = True   #Setting item to True to stop looping 
            print()
        
    



def payment(login_username, cart):   #Function as for registered customer do payment, retrieving the username and cart
    
    viewcart(cart)   #Activate the view cart function to show ordered items
    total = 0   #Start iteration
    for groceries in cart:   #Looping through the small lists in cart
        price = groceries[2]
        price = int(price)   #Sets the thrid element to integer price
        total = total + price   #Adds up the total price
    
    
    writeadmin_vieworder(login_username, cart)    #Activates the function and writes the paid order into a text file

    print("\n\n\n" + login_username, "'s total payment is RM", total)
    print("\n")


        
        
    
def viewpersonal_info (login_username):    #Function as for registered customer to view their own personal info
    try:
        regfile = open("regcustomer.txt","r")    #Opens "registered customer text file" as READ

    except:
        print ("File can't be opened")
        exit()

    masterlist_cusdata = []    #Creates a masterlist of registered customer
    print()
    for customer in regfile:   #Loops through the "registered customer text file"
        username,password,name,gender,dob,address,email,number = customer.strip().split(";")[0:8]
        masterlist_cusdata.append ([username,password,name,gender,dob,address,email,number])   #Append all the data in "registered customer text file" into masterlist registered customer

    for customer_data in masterlist_cusdata:   #Loops through the masterlist registered customer
        if login_username == customer_data[0]:  #Checks the customer name in the registered customer masterlist
            print (customer_data)    #Prints out the line accordingly
 
    print()


menu()   #Starts the Main Menu Function


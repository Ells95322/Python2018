# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2017/2018 EXAMPLE TEST - v09.01.2017
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Grocery Store - Customer Receipt
DESCRIPTION: There are many large tasks at a grocery store where software plays an important role.
One task is generating a customer receipt. Each of the questions below break down this large task into
smaller tasks. By completing the questions, you will be able to generate a receipt, which is produced
by the main function. Some of your questions may require you to call previous functions.

1. For each question, write your code to solve the objectives.
2. Each objective is worth a designated number of points. 70 Points Total.
3. Highest number of points wins. Question X is a tie breaker.
4. Do not modify the main function at the bottom of this file.
5. Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
6. Run your program often to test and check for errors.

GOOD LUCK! '''

# QUESTION 0: RECEIPT TITLE
# Objective (2) A store name and store number are passed into the function below. Return the a string
# with the name and number concatenated separated by a hyphen. ex) "store - number"
def getReceiptTitle(storeName, storeNumber):

    return ''

# QUESTION 1: GENERATE TIMESTAMP
# Objective (2) The customers receipt will have a timestamp of when it was generated. Import datetime and return a current timestamp as a string.
# Objective (2) Format the timestamp to return in this format: MONTH/DAY/YEAR HOUR:MINUTE:SECOND
def getTimeStamp():
    
    return ''

# QUESTION 2: SALES TAX
# Objective (2) Given an amount and percentage(decimal), calculate the salestax and
# return the salestax. Format the tax for 2 decimal places ('%.2f' % 1.234)
# Objective (1) Amounts under 20 dollars should have no salestax added.
# Objective (2) Amounts 100 and greater always have 5% salestax.
def getSalesTax(amount, percent):

    return ''

# QUESTION 3: PRODUCT PRICES
# Objective (5) This function should return a new dictionary. The dictionary will contain key : value pairs
# for the products and their associated price. The products and prices are as follows:
# Apple : 1
# Orange : 1.5
# Chicken : 5
# Milk : 3.75
# Candy : 1.25
def getPrices():

    return ''

# QUESTION 4: SALE PRICE
# Objective (5) Complete this function to return the price of the product passed as a parameter. (Call your getPrices function).
# The list of products is a parameter as well, so you can count the quantity of a single product.
# Objective (2) If the product is an apple or an orange and the quantity parameter is 3 or greater, subtract .25 from the price.
# Objective (2) If the product is candy and the quantity parameter is 5 or greater, subtract .50 from the price.
# Objective (2) If the product is not found, return a price of 0.00.
def getSalePrice(product, products):

    return ''

# QUESTION 5: PRODUCT ALERT
# Objective (5) A list of products representing the customer's shopping cart is passed into the function. If there is 5 or more of any single item,
# return true, else return false.
# Objective (2)  Make an exception for Candy, in which case there must be more than 10 in order to return true.
def hasAlerts(products):

    return ''

# QUESTION 6: SORT THE CART
# Objective (5) A list of products representing the customer's shopping cart is passed into the function. Return the list of products sorted
# in alphabetical order.
# Objective (2) If the list of products is greater than 10, add the item 'Gift Card' to the end of the list.
def sortCart(products):

    return products

# QUESTION 7: CUSTOMER'S SUB TOTAL
# Objective (6) A list of products representing the customer's shopping cart is passed into the function. Return the total 
# of the cart before tax and before calculating sale prices. Use getPrices() to find each items price.
# NOTE: Make sure to check if a product exists before getting the price.
# Objective (2) If no items are in the list, return 0.00 . 
def getSubTotal(products):

    return ''

# QUESTION 8: CUSTOMER'S FINAL TOTAL
# Objective (10) A list of products representing the customer's shopping cart is passed into the function. Return the final total
# including sales prices. Use getSalePrice().
def getFinalTotal(products):

    return ''

# QUESTION 9: DATA ANALYTICS
# Objective (2) Write your own function that generates and returns a statistic based on the customers data. Function return type should be a string.
# Objective (2) Define what the statistic is with comments in the function.
# Objective (3) The customers product list is passed in. Use at least one of the previous functions in this function.
# Objective (4) Use a built in function or function from Python's Math library in your function.
def getDataAnalytics(products):

    return ''


###############################
# Main Function. Do Not Modify.
# NOTE: Input for the programming questions is only test data. 
# Different values will be used to grade the questions.
###############################
def main():
    products = ['Apple','Apple','Candy','Chicken','Milk','Milk','Candy', 'Candy','Candy', 'Orange','Apple','Chicken','Apple','Apple']
    
    print('Source Code - Division B/C - v09.01.2017')
    print('Question 0: '+getReceiptTitle('The Source Code Store', '00001'))
    print('Question 1: '+getTimeStamp())
    print('Question 2: '+str(getSalesTax(104.50, .06)))
    print('Question 3: '+str(getPrices()))
    print('Question 4: '+str(getSalePrice('Apple', products)))
    print('Question 5: '+str(hasAlerts(products)))
    print('Question 6: '+str(sortCart(products)))
    print('Question 7: '+str(getSubTotal(products)))
    print('Question 8: '+str(getFinalTotal(products)))
    print('Question 9: '+getDataAnalytics(products))

    print('')
    # Display the Receipt
    products = ['Apple','Apple','Candy','Chicken','Milk','Milk','Candy', 'Candy','Candy', 'Orange','Apple','Chicken','Apple','Apple']
    prices = getPrices()
    subtotal = getSubTotal(products)
    saletotal = getFinalTotal(products)
    tax = getSalesTax(saletotal,.06)
    finaltotal = saletotal + tax
    
    print('-------------------------------');
    print(''+getReceiptTitle('The Source Code Store', '00001')+'')
    print('Time: '+getTimeStamp())
    print('-------------------------------');
    for item in sortCart(products):
        line = item+'\t \t'
        if (len(prices) > 0 and prices.get(item) != None):
            line += '$'+str(prices.get(item)) + '\t$'+str(getSalePrice(item, products))
        print(line)
    print('')
    print('Sub Total:\t$'+str(subtotal)+'\t'+str(saletotal))
    print('Tax:\t\t\t'+str(tax))
    print('Final Total: \t \t$'+str(finaltotal))
    print('-------------------------------');
    if (hasAlerts(products)): print('Your order has an alert!')
    else: print('Your order has no alerts.')
    print('-------------------------------');
    print('Statistics: '+getDataAnalytics(products))

    
main()

#Program: bookstore()
#create and test bookstore()
#bookstore() takes 2 string arguments: book & price
#bookstore returns a string in sentence form
#bookstore() should call title_it_rtn() with book parameter
#gather input for book_entry and price_entry to use in calling bookstore()
#print the return value of bookstore()
#example of output:Title: The Adventures Of Sherlock Holmes, costs $12.99
def bookstore(book,price):
    return 'Title: ' + book + 'costs $' + price


x=bookstore("summer sunset's","12.75")
print(x)

 
#Write MyBook class

class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price = price

    def display(self):
        strr = "Title: "+title+"\nAuthor: "+author+"\nPrice: "+str(price)
        print(strr)


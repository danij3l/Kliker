from cgitb import text
from operator import contains
import sys
import re
from bs4 import BeautifulSoup

#   TODO NAPRAVITI KLASE ZA SVAKU VRSTU HTML-A
#   TODO SVAKA OD TIH KLASA TREBA IMATI METODU parse() KOJA PRIMA SOUP IZ MAIN-A I VRAĆA ARRAY OBJEKATA

#   TODO SVAKA OD KLASA TREBA DA VRATI LISTU OBJEKATA SA ODREĐENOM STRUKTUROM, OVISNO O KOJOJ SE STRANICI RADI

#   ZADATAK 1:
#   http://quotes.toscrape.com/
#   quotes_to_scrape_test.html MORA VRATITI LISTU OBJEKTA KOJI SVI IMAJU:
#                                                                        url -> URL NA KOJEM SE MOGU VIDJETI DETALJI AUTORA
#                                                                        author -> IME AUTORA
#                                                                        text -> TEXT QUOTE-A
#                                                                        tags -> ARRAY (LISTA) SA TEXTOM SVIH TAGOVA U QUOTE-U

#   ZADATAK 2
#   https://books.toscrape.com/
#   books_to_scrape_test.html i MORAJA VRATITI LISTU OBJEKTA KOJI SVI IMAJU:
#                                                                            url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
#                                                                            title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
#                                                                            stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
#                                                                            price -> CIJENA KJNIGE (MORA BITI float TIP)
#                                                                            rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)

#   ZADATAK 3
#   https://www.bookdepository.com/category/2638/History-Archaeology
#   books_depository_test.html i MORAJA VRATITI LISTU OBJEKTA KOJI SVI IMAJU:
#                                                                            url -> URL NA KOJEM SE MOGU VIDJETI DETALJI TE KNJIGE
#                                                                            title -> TITLE TE KNJIGE (PO MOGUĆNOSTI UZETI CIJELI TITLE)
#                                                                            stock -> 0 ILI 1 OVISNO O JELI KNJIGA DOSTUPNA ZA KUPITI (0-NE, 1-DA)
#                                                                            price -> CIJENA KJNIGE (MORA BITI float TIP)
#                                                                            low_price -> NAJNIŽA CIJENA KJNIGE U 30 DANA (30-day low price), AKO NE POSTOJI MORA BITI ISTI KAO I PRICE (MORA BITI float TIP)
#                                                                            rating -> RATING KNJIGE (OD 0-5, OVISNO KOLIKO ZVIJEZDA IMA KNJIGA)
#                                                                            category -> KATEGORIJA U KOJOJ JE KNJIGA SVRSTANA (New and recent, Bestselling History Titles, ...)


class QuotesToScrapeClass():
    def __init__(self, name="QuotesToScrapeClass"):
        self.results = []

    def parse(self, soup):
	
        quoteObjectList = []

        quotes = soup.find_all(class_="quote")
        for quote in quotes:

            url = quote.find("a").get('href')

            author = quote.find("small").string

            text = quote.find("span").string

            tagList = []
            tags = quote.find_all(class_="tags")
            for tag in tags:
                tagText = tag.find_all("a")
                for txt in tagText:
                    tagList.append(txt.string)

            quoteObjectList.append( (url, author, text, tagList) )

        return quoteObjectList

class BooksToScrapeClass():
    def __init__(self, name="BooksToScrapeClass"):
        self.results = []
    
    def parse(self, soup):
	
        booksObjectList = []

        for book in soup.find_all("h3"): # interator

            books = soup.find_all("h3")
            for book in books:
                url = book.find("a").get('href')
            
            products = soup.find_all(class_ = "image_container")
            for product in products:
                title = product.select('img')[0]['alt']

            productData = soup.find_all(class_ = "instock availability")

            for pd in productData:
                x = pd.text

                if "In stock" in x:
                    stock = 1
                else: stock=0

            prices = soup.find_all(class_ = "price_color")
            for price in prices:
                priceFloatedAndWithoutPoundPrefix = float(price.text[1:]) # [1:] erases pound symbol from price

            ratings = soup.find_all(class_ = "product_pod")
            for rating in ratings:
                r = rating.p['class'][1] # fetches second word in rating

                numericalRating=0 #default

                if r == "One": numericalRating = 1
                elif r == "Two":numericalRating = 2
                elif r == "Three":numericalRating = 3
                elif r == "Four":numericalRating = 4
                elif r == "Four":numericalRating = 5

            booksObjectList.append( (url, title, stock, priceFloatedAndWithoutPoundPrefix, numericalRating) )

        return booksObjectList


class BookRepositiryToScrapeClass():
    def __init__(self, name="BookRepositiryToScrapeClass"):
        self.results = []
    
    def parse(self, soup):  
        bookRepositiryObjectList = [] 
        return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Invalid number of arguments.")
    else:
        file_name = sys.argv[1]

        acceptedFileNames = ["quotes_to_scrape_test.html", "books_to_scrape_test.html", "book_depository_test.html"]
        for i in acceptedFileNames:
            if file_name==acceptedFileNames[0]:
                 with open(file_name, encoding="utf8") as fp:
                    soup = BeautifulSoup(fp, "html.parser")                   
                    instance = QuotesToScrapeClass()
                    print (instance.parse(soup))
                    break

            elif file_name==acceptedFileNames[1]:
                 with open(file_name, encoding="utf8") as fp:
                    soup = BeautifulSoup(fp, "html.parser")     
                    instance = BooksToScrapeClass()
                    print (instance.parse(soup))
                    break

            elif file_name==acceptedFileNames[2]:
                 with open(file_name, encoding="utf8") as fp:
                    soup = BeautifulSoup(fp, "html.parser")     
                    instance=BookRepositiryToScrapeClass()
                    print (instance.parse(soup))
                    break

            else: 
                print ("Invalid file name, are you missing .html extension?") 
                break

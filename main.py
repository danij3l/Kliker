from cgitb import text
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



class ClassTemplate():
    def __init__(self, name="ClassTemplate"):
        self.results = []
    
    def parse(self, soup):
        print("CODE HERE")
        
        #   PRIMJER LISTE OBJEKATA (ATRIBUTI SU DUMMY PODATCI, SLUŽI SAMO KAO PRIMJER STRUKTURE OUTPUTA)
        self.results = [
            {
                "title": "Object 1",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas bibendum nisl eu maximus convallis. Maecenas suscipit, augue eu viverra suscipit, quam est luctus neque, vel consequat eros felis eu eros. Ut mollis suscipit vulputate. Aliquam erat volutpat. Phasellus nec dui aliquet, ornare urna vitae, placerat justo. Fusce mauris ipsum, porttitor sed cursus id, venenatis a erat. Nulla dui urna, semper sit amet porta in, dapibus eget ante. Sed consequat lacinia vestibulum. Donec porttitor nisl vel dui congue vulputate. Quisque hendrerit neque vel libero lobortis efficitur.",
                "price": 100
            },
            {
                "title": "Object 2",
                "description": "Proin ac tortor et nisl pretium hendrerit eu sit amet arcu. Integer risus purus, varius eget dui auctor, dictum mollis lacus. Etiam sit amet metus ante. Donec et tortor mattis, efficitur purus vitae, porta arcu. Phasellus dictum, felis viverra euismod tristique, libero lorem facilisis odio, non luctus diam nisl vitae turpis. Aliquam at turpis quis nisl placerat tincidunt. Nam a hendrerit elit. Vivamus eget mi porta, pulvinar massa in, eleifend augue. ",
                "price": 150
            },
            {
                 "title": "Object 2",
                 "description": "Integer neque ex, tincidunt in suscipit in, elementum sit amet neque. Quisque pulvinar dui eget tellus porttitor, sed fringilla ligula imperdiet. Sed eu sem justo. Etiam a ullamcorper ipsum. Pellentesque varius orci vel velit cursus suscipit. Proin at congue nisl. Suspendisse vitae dolor in risus molestie tempor. Suspendisse nec metus magna. Proin sed quam lectus. Proin scelerisque dui purus, aliquam vehicula purus commodo id. Praesent fermentum ante semper erat rhoncus, eu congue ligula sollicitudin. Pellentesque viverra vehicula auctor. Sed quis lacus sem. ",
                 "price": 250
            }
        ]
        
        return self.results


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
        return "Not yet implemented ^^"

class BookRepositiryToScrapeClass():
    def __init__(self, name="BookRepositiryToScrapeClass"):
        self.results = []
    
    def parse(self, soup):     
        return "Not yet implemented ^^"


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

import requests, bs4


web_url = 'https://books.toscrape.com/catalogue/page-{}.html'

books_N5Best = 0
books_N4Best = 0

for i in range(1,51):
    web_request = requests.get(web_url.format(str(i)))
    web_soup = bs4.BeautifulSoup(web_request.text, 'lxml')
    product_view = web_soup.select(".product_pod")


    for book in range(len(product_view)):
        product_rating5 = product_view[book].select(".star-rating.Five")
        product_rating4 = product_view[book].select(".star-rating.Four")
        product_title = product_view[book].select("a")[1]["title"]

        if product_rating5 != []:
            print(f"Page: {i}, Book_N: {book+1}, Name: {product_title} Rating: 5 stars")
            books_N5Best += 1
        elif product_rating4 != []:
            print(f"Page: {i}, Book_N: {book+1}, Name: {product_title} Rating: 4 stars")
            books_N4Best += 1

    print(f"{"-"*50}")

print("Summary:")
print(f"Total books with 5 stars rating: {books_N5Best}")
print(f"Total books with 4 stars rating: {books_N4Best}")
print(f"Total books: {books_N5Best + books_N4Best}")
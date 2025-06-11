import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Solution 👇


response = requests.get(URL)
movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")
movies_html_doc = soup.find_all(name = "h3", class_ = "title")

movie_titles = []
for movie in movies_html_doc:
    movie_titles.append(movie.get_text())

movie_titles.reverse()
for title in movie_titles:
    print(title)


# Generating a .txt file of all 100 movies
with open("movies.txt", "w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}.\n")

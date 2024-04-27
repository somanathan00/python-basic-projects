from bs4 import BeautifulSoup
import requests
resopnse = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = resopnse.text


soup = BeautifulSoup(content, "html.parser")
movie_title = soup.find_all(name='h3', class_='title')
movie_title = [movie.getText() for movie in movie_title]
movie_title = movie_title[::-1]
print(movie_title)


with open("movie.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_title:
        file.write(f"{movie}\n")

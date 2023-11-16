import requests
from bs4 import BeautifulSoup
from functools import lru_cache


@lru_cache(maxsize=None)
def get_html(url):
    response = requests.get(url)
    result = response.text
    return result


news_html = get_html("https://news.ycombinator.com/")
news_soup = BeautifulSoup(news_html, "html.parser")
titles = news_soup.find_all(name="span", class_="titleline")
scores = news_soup.find_all(name="span", class_="score")

titles_list = (title.find(name="a").getText() for title in titles)
links_list = (title.find(name="a").get("href") for title in titles)
scores_list = (int(score.getText().split()[0]) for score in scores)

news_data = list(zip(titles_list, links_list, scores_list))
print(news_data)

movies_html = get_html(
    "https://www.empireonline.com/movies/features/best-movies-2/")
movies_soup = BeautifulSoup(movies_html, "html.parser")
movie_titles = movies_soup.find_all(
    name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movie_images = movies_soup.find_all(
    name="div", class_="listicleItem_listicle-item__image__EWbyD")
movie_titles_list = list(reversed([title.getText() for title in movie_titles]))
movie_images_list = list(
    reversed([image.find(name="img").get("src") for image in movie_images]))
movies_data = list(zip(movie_titles_list, movie_images_list))
print(movies_data)

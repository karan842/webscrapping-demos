from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests, openpyxl



excel = openpyxl.Workbook()
# print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Top Rated Movies'
# print(excel.sheetnames)
sheet.append(['Movie_Rank','Moviue_Name','Movie_Year','Movie_Rating'])


try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    movies = soup.find('tbody',class_="lister-list").find_all("tr")
    # print(movies)
    for movie in movies:
        name = movie.find('td',class_="titleColumn").a.text
        rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        year = movie.find('td',class_='titleColumn').span.text.strip('()')
        rating = movie.find('td',class_='ratingColumn imdbRating').strong.text
        # print(rank,name,year,rating)
        sheet.append([rank, name, year, rating])
    
except Exception as e:
    print(e)
    
excel.save('IMDB_TOP_MOVIES.xlsx')
print("DATA SAVED!!")
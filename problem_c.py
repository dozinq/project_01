import json
from pprint import pprint
import problem_b

def movie_info(movies, genres):
    dict_names_changer = list()

    for movie in movies:
        dict_names_changer.append(problem_b.movie_info(movie, genres))
    return dict_names_changer
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
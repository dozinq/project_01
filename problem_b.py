import json
from pprint import pprint
import problem_a


def movie_info(movie, genres):
    #이전 문제에서의 movie_info 함수를 불러오며, genre_names 리스트를 생성한다.
    my_dict = problem_a.movie_info(movie)
    genre_names = list()
    genre_id_repository = my_dict.pop('genre_ids')

    for i in genres:
        if i.get('id') in genre_id_repository:
            genre_names.append(i.get('name'))
        my_dict['genre_names'] = genre_names
    

    return my_dict
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
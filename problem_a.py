import json
from pprint import pprint


def movie_info(movie):
    # 여기에 코드를 작성합니다.
    my_dict = dict()
    my_dict['id'] = movie.get('id')
    my_dict['title'] = movie.get('title')
    my_dict['poster_path'] = movie.get('poster_path')
    my_dict['vote_average'] = movie.get('vote_average')
    my_dict['overview'] = movie.get('overview')
    my_dict['genre_ids'] = movie.get('genre_ids')
    return my_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
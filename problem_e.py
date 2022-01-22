import json

def dec_movies(movies):
    my_lst = list()
    for i in movies:
        movie_id = i.get('id')
        movie_info_json = open('data/movies/%d.json' % movie_id, encoding='UTF8') 
        movie_info = json.load(movie_info_json)
        movie_when = movie_info.get('release_date')
        if movie_when[5:7:1] == '12':
            my_lst.append(i.get('title'))
    return my_lst
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
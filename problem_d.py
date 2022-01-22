from encodings import utf_8
import json

def max_revenue(movies):
    revenue_first = 0
    revenue_name = ''
    
    for i in movies:
        movie_id = i.get('id')
        movie_info_json = open('data/movies/%d.json' % movie_id, encoding='UTF8') 
        movie_info = json.load(movie_info_json)
        if revenue_first <= movie_info.get('revenue'):
            revenue_first = movie_info.get('revenue')
            revenue_name = i.get('title')

    return revenue_name
    

            
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
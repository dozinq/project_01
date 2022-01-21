# 📌 My First Project 📋

---

##### - Outline : 2022년 1월 21일, 나는 인생에서 첫 프로젝트를 접하였다. 간단한 프로젝트라고 생각되었지만, 무엇이든 나에게는 소중한 경험이라고 생각한다. 진행하면서 내가 느꼈던 점을 중심으로 소개해 보고자 한다.

---
<br/>


# **< Title : " Python을 활용한 데이터 수집 Ⅰ *"* >**

*(This project was carried out in **Python 3.9.9 environment.**)*

- *요구사항 : 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를 추출해 나가는 과정을 진행합니다. 총 5개의 구현 과정이 있으며, 데이터를 수집하고 활용하는 과정을 요구합니다.*


<br/>


#### - case #1. 제공되는 영화 데이터의 주요내용 수집

*: 샘플 영화데이터가 주어질 때, 서비스 구성에 필요한 정보만을 반환하는 함수를 완성한다.*

```python
import json
from pprint import pprint

def movie_info(movie):
    my_dict = dict()							#비어있는 딕셔너리 만들기.
    my_dict['id'] = movie.get('id')				#생성된 딕셔너리에 원하는 정보만을 담는다.
    my_dict['title'] = movie.get('title')
    my_dict['poster_path'] = movie.get('poster_path')
    my_dict['vote_average'] = movie.get('vote_average')
    my_dict['overview'] = movie.get('overview')
    my_dict['genre_ids'] = movie.get('genre_ids')
    return my_dict								#원하는 정보들을 담은 딕셔너리를 반환.
```

>  　첫 번째 유형의 케이스를 수행하면서, 배웠던 딕셔너리를 활용하는 방법에 대한 고찰이 필요했으며 지식을 깨우침으로 끝나는 것이 아니라 활용하여 표현해 내야 하는 것에 대한 부담을 느꼈다. 
>
>  　또한, 점차 해결해 나아갈수록 이 프로젝트가 요구하는 것이 이와 같은 문제 해결 역량이라는 것을 깨닫게 되었다.


<br/>


#### - case #2. 제공되는 영화 데이터의 주요내용 수정

*: 이전 단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함수를 완성한다.*

```python
import json
from pprint import pprint
import problem_a            #이전 문제에서 만들었던 problem_a를 가져온다.

def movie_info(movie, genres):
    #이전 문제에서의 movie_info 함수를 불러오며, genre_names 리스트를 생성한다.
    my_dict = problem_a.movie_info(movie)
    genre_names = list()         
    #pop함수를 사용하여, genre_ids를 genre_names로 바꾸려고 계획하였다.
    genre_id_repository = my_dict.pop('genre_ids')

    #반복문을 통해 id를 name으로 대체할 수 있도록 합니다.
    for i in genres:
        #반복문 안에 조건문을 통해 동일한 id의 name을 가져올 수 있도록 하였다.
        if i.get('id') in genre_id_repository:
            genre_names.append(i.get('name'))
        my_dict['genre_names'] = genre_names
    
    return my_dict
```

>  　두 번째 유형의 케이스를 수행하면서, 이전 함수를 그대로 불러오는 과정 또한 직접 활용해 볼 수 있었으며, 약간의 시행착오 끝에 결국 완성할 수 있었던 것 같다.
>
>  　반복문 안에 조건문을 설계하는 과정에서 많이 고민할 필요가 있었으며, 마지막 변경 단계에서 del 함수를 삭제하고 pop 함수로 변경하여 직관적으로 표현될 수 있도록 가꾸어 주었다.

<br/>



#### - case #3. 다중 데이터 분석 및 수정

*: TMDB기준 평점이 높은 20개의 영화데이터가 주어지는데, 그 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성한다. 완성된 함수는 향후 커뮤니티 서비스에서 제공되는 영화 목록을 제공하기 위한 기능으로 사용된다고 한다.*

```python
import json
from pprint import pprint
import problem_b			#이전 문제에서 만들었던 problem_b를 가져온다.

def movie_info(movies, genres):
    dict_names_changer = list()
    for movie in movies:
        #리스트에 각 영화마다 id값을 장르로 반환하여 영화들의 전체 정보를 수정한다.
        dict_names_changer.append(problem_b.movie_info(movie, genres))
        #누적된 리스트를 반환시켜준다.
    return dict_names_changer
```

>  　세 번째 유형의 케이스를 수행하면서, 그동안 배웠었던 모든 개념을 혼합하여 사용하려 하였다.
>
>  　그랬기에 잦은 오류를 마주하게 되었고, 오류 사항들을 수정하면서 더 많은 것을 배울 수 있었다고 생각한다.
>
>  　결국 모든 항목들을 수정시켜주는 함수를 성공적으로 구현할 수 있었다.

<br/>



#### - case #4. 알고리즘을 통한 데이터 출력 (1)

*: 세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화를 출력하는 알고리즘을 작성하게 한다. 또한 해당 데이터는 향후 커뮤니티 서비스에서 메인 페이지 기본정보로 사용된다고 한다.*

```python
from encodings import utf_8
import json

def max_revenue(movies):
    revenue_first = 0
    revenue_name = ''
    
    for i in movies:
        #반복문을 통해, 'id'를 수집하게 하는 변수를 만들었다.
        movie_id = i.get('id')
        #해당 폴더를 오픈하여 그에 맞는 정보만을 확인할 수 있도록 구현하였다.
        movie_info_json = open('data/movies/%d.json' % movie_id, encoding='UTF8') 
        movie_info = json.load(movie_info_json)
        #조건문을 통해, 'revenue'의 값을 비교해 보면서 가장 높은 값만을 발견할 수 있게 하였다.
        if revenue_first <= movie_info.get('revenue'):
            revenue_first = movie_info.get('revenue')
            revenue_name = i.get('title')

    return revenue_name			#끝으로, 목표로 설정한 영화의 제목을 반환할 수 있게 하였다.
```

>   　네 번째 유형의 케이스를 수행하면서, 정말 해당 목적을 가진 의뢰를 해결해 나아갈 수 있어야 한다고 생각했다. 어떤 상황을 직면하게 될지 모르니깐 말이다.
>
>   　반복문 안에 조건문을 설계했던 과정과 새로운 변수를 만들어서 비교할 수 있게 만드는 알고리즘을 구현해 나아가면서 그동안의 학습에 대한 보람을 느낄 수 있었던 것 같다.


<br/>


#### - case #5. 알고리즘을 통한 데이터 출력 (2)

*: 세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성한다. 해당 데이터는 향후 커뮤니티 서비스에서 추천기능의 정보로 사용된다고 한다.*

```python
import json

def dec_movies(movies):
    my_lst = list()
    for i in movies:
        movie_id = i.get('id')
        #해당 폴더를 오픈하여 그에 맞는 정보만을 확인할 수 있도록 구현하였다.
        movie_info_json = open('data/movies/%d.json' % movie_id, encoding='UTF8') 
        movie_info = json.load(movie_info_json)
        movie_when = movie_info.get('release_date')
        #12월에 만들어진 영화의 제목을 찾는 과정에서 많은 접근방법들이 떠올랐지만,
        #결국 조건문 안에서 slicing으로 접근할 수 있었다.
        if movie_when[5:7:1] == '12':
            my_lst.append(i.get('title'))
    return my_lst			#끝으로, 목표로 설정한 영화의 제목을 리스트로 만들어 반환하였다.
```

>   　마지막 케이스를 수행하면서, 이는 네 번째 유형의 케이스를 해결할 때와 굉장히 닮아있다는 점을 많이 느꼈던 것 같다.
>
>   　단 한 번의 오류를 마주하고 끝내 실행할 수 있었다는 점은 스스로를 대견하게 만들어 주었다.


<br/>


## ✏After finishing..

>   　첫 프로젝트인 만큼 더 많은 것을 해결한 다기보다는 지금까지 배운 내용들을 얼마나 활용할 수 있는지에 대해서 초점을 맞추었다. 조바심 내지 않고 천천히 수행해도 스스로 만족하였으며, 그랬기에 실수는 최대한 줄일 수 있었던 것 같다.
>
>   　이번 프로젝트를 통해 "개발자란 무엇인가?"라는 생각을 스스로에게 많이 물어보기도 하였으며, 스스로에게 답하기도 하였다. 그 끝에 들었던 생각은 다음과 같다.
>
>   　개발자란 결국, 상황을 머릿속으로 구상하고 스케치하였던 '화가'일 수도 있고, 잘못된 점을 개선해 주는 '수리공'일 수도 있고, 상상을 결국 현실로 바꾸어 주는 '발명가'일 수도 있다고 생각하였다.
>
>   　"개발자란 분명히 어떤 것이다."라고 확실하게 말할 수는 없는 나 지만, 난 개발자가 되기 위해 나아가고 있다. 그저 걸어갈 뿐이다.


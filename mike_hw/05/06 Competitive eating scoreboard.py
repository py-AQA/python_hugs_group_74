# https://www.codewars.com/kata/571d2e9eeed4a150d30011e7
from helper import test


# не повторяйте такое в одну строку!!! горизонтальная прокрутка - ЗЛО
def scoreboard(who_ate_what):
    return sorted(sorted([{'name': item['name'], 'score': sum([who_ate_what[i][y] * {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}[y] for y in item if y != 'name'])} for i, item in enumerate(who_ate_what)], key=lambda x: x['name']), reverse=True, key=lambda x: x['score'])


# проверка
test.assert_equals(scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},{"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},{"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},{"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]), [{"name": "Big Bob", "score": 134}, {"name": "Billy The Beast", "score": 122}, {"name": "Habanero Hillary", "score": 98}, {"name": "Joey Jaws", "score": 94}])
test.assert_equals(scoreboard([{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]), [{"name": "Big Bob", "score": 134}])
test.assert_equals(scoreboard([{"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},{"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]), [{"name": "Big Bob", "score": 134}, {"name": "Joey Jaws", "score": 94}])
test.assert_equals(scoreboard([{"name": "Joey Jaws", "chickenwings": 0, "hamburgers": 1, "hotdogs": 1},{"name": "Big Bob" , "chickenwings": 1, "hamburgers": 0, "hotdogs": 0}]), [{"name": "Big Bob", "score": 5}, {"name": "Joey Jaws", "score": 5}])
test.assert_equals(scoreboard([]), [])

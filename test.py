from pprint import pprint
from requests import get, post, delete

pprint(get('http://127.0.0.1:8080/api/v2/users').json())  # кор
pprint(get('http://127.0.0.1:8080/api/v2/users/2').json())  # кор
pprint(get('http://127.0.0.1:8080/api/v2/users/99').json())  # некор несуществующий id
pprint(get('http://127.0.0.1:8080/api/v2/users/dfgyhjnm').json())  # некор id строка

pprint(post('http://127.0.0.1:8080/api/v2/users', json={}).json())  # некор пустые поля
pprint(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Sonya'}).json())  # некор не все поля заполнены
pprint(post('http://127.0.0.1:8080/api/v2/users', json={'name': 'Sonya', 'position': 'doctor',
                                                        'surname': 'Smith', 'age': 35, 'address': 'hospital',
                                                        'speciality': 'medicine',
                                                        'hashed_password': 'sonechka',
                                                        'email': 'sonyas@mars.org'}).json())  # кор
pprint(get('http://127.0.0.1:8080/api/v2/users/4').json())  # кор

pprint(delete('http://127.0.0.1:8080/api/v2/users/654').json())  # некор несущ id
pprint(delete('http://127.0.0.1:8080/api/v2/users/3').json())  # кор

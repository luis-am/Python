import requests

# r = requests.get('https://xkcd.com/353/')
# print(r.content)
# print(r.text)

# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open('dibujo.png', 'wb') as f:
    # f.write(r.content)
# print(r.status_code)
# print(r.ok)
# print(r.headers)

# payload = {'page': 2, 'count':25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url)

# parametros = {
    # 'name' : 'Luis',
    # 'edad' : 25
        # }
# response = requests.get('https://httpbin.org/get', params=parametros)
# print(response.url)


# payload = {
    # 'name' : 'Luis',
    # 'edad' : 25
        # }
# response = requests.post('https://httpbin.org/post', params=payload)
# print(response.url)


# response = requests.get('https://httpbin.org/status/504')
# if response.status_code == requests.codes.not_found:
    # print('Not found')
# else:
    # print(response.status_code)


# response = requests.get('https://cibertec.edu.pe/ip')
# print(response.text)



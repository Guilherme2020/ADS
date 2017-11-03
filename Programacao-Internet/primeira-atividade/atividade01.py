import requests

r = requests.get('http://httpbin.org/get')
#– Linha de status (número, texto e versão HTTP);
print(r.status_code)
print(r.text)
print(r.raw.version)
#– Cabeçalhos (response headers);
print(r.headers)
#– Tamanho da resposta (content length).
print(r.headers['content-length'])
print(r.headers['content-type'])
print(len(r.content))


print("######")


'''


r= requests.get('https://api.github.com/user', auth=('user', 'pass'))

print(len(request.content))

request = requests.get('https://www.google.com.br', auth=('user', 'pass'))

print(request.status_code)
print(request.text)
print(request.headers)
'''

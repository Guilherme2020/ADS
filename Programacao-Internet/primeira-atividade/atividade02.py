import requests
import shutil


url = 'https://meusanimais.com.br/wp-content/uploads/2015/05/gato.jpg'
r = requests.get(url, stream=True)
if r.status_code == 200:
    with open('gato.jpg','wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

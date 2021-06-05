import urllib
from urllib import request
try:
    site = urllib.request.urlopen('https://github.com/')
except:
    print('Não consegui acessar o site ;-;!')
else:
    print('O site ainda está disponível!')    

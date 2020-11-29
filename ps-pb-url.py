import os

os.system('cls')

def get_absolute_url(url,*args,**kwargs):
    for i in args:
        url = f'{url}/{i}'
    url = f'{url}?'
    for k,v in kwargs.items():
        url = f'{url}{k}={v}&'
    return url[:-1] 
    
print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24',author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))


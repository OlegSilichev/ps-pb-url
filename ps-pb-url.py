import os

os.system('cls')

def get_absolute_url(domen,*args,**kwargs):
    result = f'{domen}'
    for i in args:
        result = f'{result}/{i}'
    result = f'{result}?'
    for k,v in kwargs.items():
        result = f'{result}{k}={v}&'
    return result[:-1] 
    
print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24',author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))


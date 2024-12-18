import requests
def fx(url):
    '''download url content'''
    r = requests.get(url)
    if(r.status_code != 200):
        print('download/request is failed')
        return 0
    if('text/html' in r.headers['Content-Type']):
        print('response is webpage response')
    elif('application/json' in r.headers['Content-Type']):
            print('data-response')
            jd = r.text
            pd = json.loads(jd)

fx('https://www.python.org')

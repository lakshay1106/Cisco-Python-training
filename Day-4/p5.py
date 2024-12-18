import requests
pr = requests.get('https://www.python.org')
pr.headers['Content-Type']

py_page = pr.text

py_obj = bs4.BeautifulSoup(py_page)
py_obj.find('a')

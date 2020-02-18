from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
#from urllib.request import urlopen

print('working...')

def test_1():
    chromedriver = '/usr/local/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

    browser.get('http://playsports365.com/default.aspx')

def pars_1():
    url="https://totokaelo.com/womens/designers/ann-demeulemeester"
    r=requests.get(url) 
    res = r.text
    #dat = bs(urlopen(url).read(), 'html.parser')
    dat = bs(res, 'html.parser')
    #scripts = dat.find_all('script')
    img = dat.find_all('img')
    print(img)

pars_1()

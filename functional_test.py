from selenium import webdriver

browser = webdriver.Firefox()
browser.get(url='http://localhost:8000')

assert 'Django' in browser.title

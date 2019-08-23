import time
from bs4 import BeautifulSoup as b
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
dir = open('person_data.csv','a')
headers = 'Name\n'
dir.write(headers)
def getting_page():
    driver = webdriver.Firefox()
    driver.get('https://www.politico.com/interactives/databases/trump-white-house-visitor-logs-and-records/index.html')
    seearch_button = driver.find_element_by_css_selector('.btn.search-name.inactive')
    seearch_button.click()
    time.sleep(5)
    box = driver.find_element_by_css_selector('input.form-control:nth-child(1)')
    box.click()
    box.send_keys('Marillyn Hewson')
    time.sleep(50)
    click_executive = driver.find_element_by_css_selector('.dropdown-menu > li:nth-child(4) > a:nth-child(1)').click()
    time.sleep(50)
    with open('page_data.txt','wb') as f:
        f.write(driver.page_source.encode('utf-8'))
name_list = []
def get_name_list():
    soup = b(open('page_data.txt','r'),'html.parser')
    section = soup.find_all('section',class_='visitor')
    for i in section:
        name = i.find('div',class_='name').text
        name_list.append(name)
#to  get info for each people usin this site api to retrive data.
def save_data(data):
    person_info = data.find('')
    date = data.find_all('')
    for i in data:
        dir.write('{0},{1}\n'.format(person_info,date))

get_name_list()
print(name_list)
print(len(name_list))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def chordFind(songDetails):
    SEARCH_VALUE = songDetails.replace(' ', '+')
    URL = 'https://www.ultimate-guitar.com/search.php?view_state=advanced&title='+ SEARCH_VALUE+'&type%5B%5D=300&type2%5B%5D=40000&tuning%5B%5D=standard&version_la='
    driver = webdriver.PhantomJS()
    driver.maximize_window()
    driver.get(URL)
    assert 'Ultimate-Guitar' in driver.title

    if 'No results @ Ultimate-Guitar.Com Search' in driver.title:
         return ''
    else:
        parent = driver.find_element_by_class_name('search-version--link')
        link = parent.find_element_by_tag_name('a').get_attribute('href')
        return link
    driver.close()



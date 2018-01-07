from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def songsterrFind(songDetails):
    URL = 'https://www.songsterr.com/a/wa/search'
    driver = webdriver.PhantomJS()
    driver.maximize_window()
    driver.get(URL)
    assert 'Songsterr' in driver.title
    searchBar = driver.find_element_by_class_name('Search-field')
    searchBar.clear()
    searchBar.send_keys(songDetails)
    searchBar.send_keys(Keys.RETURN)
    keyWords = songDetails.lower().split()

    time.sleep(1)

    scrollList = driver.find_element_by_class_name('Scroller-flex')

    try:
        activeSong = scrollList.find_element_by_class_name('SongsItem')
        link = activeSong.get_attribute('href')
        for x in keyWords:
            assert x in link
        return link
    except Exception:
        return ''

    driver.close()

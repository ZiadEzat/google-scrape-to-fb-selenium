from selenium import webdriver
from selenium.webdriver.common.by import By
from googletrans import Translator
import time

from selenium.webdriver.common.action_chains import ActionChains

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(executable_path="J:\geckodriver-v0.24.0-win64\geckodriver.exe", firefox_profile= firefox_profile)
previousurl = "https://www.theverge.com/2019/6/8/18658147/microsoft-xbox-scarlet-teaser-e3-2019"


def init():
    print("initializing")
    driver.get("http://www.facebook.com")

    emailelement = driver.find_element(By.XPATH, '//*[@id="email"]')
    emailelement.send_keys('EMAIL')

    passelement = driver.find_element(By.XPATH, '//*[@id="pass"]')
    passelement.send_keys('PASSWORD')
    time.sleep(5)
    buttonelement = driver.find_element(By.XPATH, '//*[@id="u_0_2"]')
    buttonelement.click()
    time.sleep(5)
    driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+technology&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    link = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[7]/div[1]/div/div/div[2]/div/a[2]')
    link.click()
    driver.get("http://www.facebook.com")
    driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+technology&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    i = 1
    while i == 1:
        print("tryagain")
        scrapeToFB()
        time.sleep(1800)


def fbpost(x):
    print("posting " + x)
    driver.get("https://www.facebook.com/groups/427614381121626/")

    postelement = driver.find_element(By.CLASS_NAME, '_ikh')
    postelement.click()
    actions = ActionChains(driver)
    actions.send_keys(x)
    actions.perform()

    postelement = driver.find_element(By.CLASS_NAME, '_1mf7')
    postelement.click()

def scrapeToFB():
    global previousurl
    print("previousurl is " + previousurl )
    try:
        driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+technology&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    except:
        print("timeout error ")
        driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+technology&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    articledesc = driver.find_element(By.CLASS_NAME, "st")
    firstpost = driver.find_element(By.CSS_SELECTOR, ".g > div > a")
    firstpost.click()
    articletitle = driver.find_element(By.CLASS_NAME, 'c-page-title')
    articleurl = driver.current_url

    if articleurl[:90] != previousurl[:90]:
        print("articleurl is not equal to previousurl")
        previousurl = articleurl
        print("new previousurl = " + previousurl)
        translator = Translator()
        try:
            print("attempting to translate")
            translate = translator.translate(articletitle.text, dest='ar')
            translate2 = translator.translate(articledesc.text, dest="ar")
        except:
            print("error")
            translate = translator.translate(articletitle.text, dest='ar')
            translate2 = translator.translate(articledesc.text, dest="ar")

        print("translate succeeded")
        fbpost(articleurl + "\n" + translate.text + "\n" + translate2.text)

    else:
        print("refreshing")
        driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+technology&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")


init()


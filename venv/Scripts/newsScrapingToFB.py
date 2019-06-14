from selenium import webdriver
from googletrans import Translator
import time
from summarizer import summarize
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(executable_path="J:\geckodriver-v0.24.0-win64\geckodriver.exe", firefox_profile= firefox_profile)
firefox_profile.set_preference("dom.webnotifications.enabled", False)

previousurl = 0


def init():
    global previousurl
    print("initializing")
    #facebook login
    driver.get("http://www.facebook.com")
    emailelement = driver.find_element(By.XPATH, '//*[@id="email"]')
    #ENTER YOUR EMAIL BELOW
    emailelement.send_keys('EMAIL')
    passelement = driver.find_element(By.XPATH, '//*[@id="pass"]')
    #ENTER YOUR PASSWORD BELOW
    passelement.send_keys('PASSWORD')
    time.sleep(5)
    buttonelement = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input')
    buttonelement.click()
    time.sleep(5)
    #changes google search language from Arabic to English
    driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+tech&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    link = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[7]/div[1]/div/div/div[2]/div/a[2]')
    link.click()
    #makes sure everything is alright
    driver.get("http://www.facebook.com")
    driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+tech&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    i = 1
    while i == 1:
        print("start")
        while True:
            try:
                scrapeToFB()
                break
            except Exception as e:
                #if error happens reset this previousurl
                previousurl = 0
                print(e)
        print("end")
        # delays 10 minutes to prevent google's bot detection
        time.sleep(600)


def fbpost(x):
    print("posting " + x)
    #ENTER YOUR GROUP BELOW
    driver.get("https://www.facebook.com/groups/427614381121626/")

    postelement = driver.find_element(By.CLASS_NAME, '_ikh')
    postelement.click()
    actions = ActionChains(driver)
    actions.send_keys(x)
    actions.perform()
    time.sleep(5)
    postelement = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/button")))
    driver.execute_script("window.scrollBy(0,259)","");

    time.sleep(10)
    postelement.click()
    time.sleep(30)
    actions2 = ActionChains(driver)
    actions2.send_keys(Keys.CONTROL, Keys.ENTER)
    actions2.perform()

def scrapeToFB():
    global previousurl
    print("previousurl is " + previousurl )
    try:
        driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+tech&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    except:
        print("timeout error ")
        driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+tech&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")
    firstpost = driver.find_element(By.CSS_SELECTOR, ".g > div > a")
    firstpost.click()
    time.sleep(30)
    articletitle = driver.find_element(By.CLASS_NAME, 'c-page-title').text
    articledesc2 = summarize(articletitle, driver.find_element(By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div[1]/p").text + " " + driver.find_element(By.XPATH, "/html/body/div[3]/main/article/div[2]/div[1]/div[1]/p[2]").text)
    articledesc = articledesc2[0] + " " + articledesc2[1]
    print(articledesc)
    print(articletitle)
    articleurl = driver.current_url

    if articleurl[:90] != previousurl[:90]:
        print("articleurl is not equal to previousurl")
        previousurl = articleurl
        print("new previousurl = " + previousurl)
        translator = Translator()
        try:
            print("attempting to translate")
            translate = translator.translate(articletitle, dest='ar')
            translate2 = translator.translate(articledesc, dest="ar")
        except:
            print("error")
            translate = translator.translate(articletitle, dest='ar')
            translate2 = translator.translate(articledesc, dest="ar")
        print("translate succeeded")
        print(translate2)
        print(translate2.text +  "\n" +articleurl )
        fbpost(articleurl + "\n"+ translate2.text )

    else:
        print("refreshing")
        driver.get("https://www.google.com/search?q=site:www.theverge.com+game+%7C+tech&client=firefox-b-d&tbas=0&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwiTh9Tax9riAhW4DmMBHR2TB1wQpwUIIA&biw=1360&bih=654&dpr=1")


init()


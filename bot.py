from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

import logininfo

def gamereportBot(url):
    driver = webdriver.Chrome()

    driver.get(url=url)
    driver.set_window_size(1920,1080)

    #Login
    driver.implicitly_wait(time_to_wait=100)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/section/div[2]/fieldset/div[1]/input').send_keys(logininfo.loginInfo().id)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/section/div[2]/fieldset/div[2]/input').send_keys(logininfo.loginInfo().pw)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/section/div[2]/fieldset/button').click()

    # game select
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/header/div[2]/div[1]/button').click()
    driver.implicitly_wait(time_to_wait=2)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/header/div[2]/div[1]/div/div/ul/li[2]/label').click()

    # service Select
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/header/div[2]/div[2]/button[1]').click()
    driver.implicitly_wait(time_to_wait=2)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/header/div[2]/div[2]/div/ul/li[3]/label').click()

    # 실시간 대시보드
    sleep(1)
    realtime_dashboard(driver)

    #대시보드
    sleep(1)
    dashboard(driver)

    # 사용자 분석
    sleep(1)
    user_analysis(driver)

    # 사용자 분석 상세
    sleep(1)
    user_analysis_detail(driver)

    # 매출
    sleep(1)
    sales(driver)

    # 인게임 현황
    sleep(1)
    ingame_monitor(driver)

    # 인게임 자원
    sleep(1)
    ingame_resource(driver)

    #이벤트 분석
    sleep(1)
    event_analysis(driver)

    # 퍼널 분석
    sleep(1)
    funnel_analysis(driver)

    #랭킹 분석
    sleep(1)
    ranking_analysis(driver)

    sleep(5)
    driver.close()

def realtime_dashboard(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[1]/a').click()

    for i in range(2, 10):
        sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/section/div/ul/li['+str(i)+']').click()
    return

def dashboard(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[2]/a').click()
    for i in range(1, 4):
        sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[2]/ul/li['+str(i)+']').click()
    return
def user_analysis(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[3]/a').click()
    for i in range(1, 5):
        sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[3]/ul/li['+str(i)+']').click()
    return

def user_analysis_detail(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[4]/a').click()
    for i in range(1, 4):
        sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[4]/ul/li[' + str(i) + ']').click()
    return

def sales(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[5]/a').click()
    for i in range(1, 5):
        sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[5]/ul/li[' + str(i) + ']').click()
    return

def ingame_monitor(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[6]/a').click()
    for i in range(1, 5):
        sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[6]/ul/li[' + str(i) + ']').click()
    return
def ingame_resource(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[7]/a').click()
    for i in range(1, 7):
        sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[7]/ul/li[' + str(i) + ']').click()
    return

def event_analysis(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[8]/a').click()
    return

def funnel_analysis(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[9]/a').click()
    return

def ranking_analysis(driver):
    sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="lnbMenu"]/ul/li[10]/a').click()
    return

if __name__ == '__main__':
    url = 'https://center.beta-gamereport.naverncp.com/'
    gamereportBot(url)

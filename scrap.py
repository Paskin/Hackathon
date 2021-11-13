from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urllib import request

driver = webdriver.Chrome(executable_path='/Users/dima/Downloads/chromedriver')

for page in range (1,11):
    driver.get("https://www.spoonflower.com/en/shop?on=wallpaper&page_offset=" + str(page))

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='b-design-item x-shadowed']"))
        )
    except:
        print("Error")

    links = []

    try:
        for elem in driver.find_elements_by_xpath("//div[@class='b-design-item x-shadowed']/a"):
            href = elem.get_attribute("href")
            if "/wallpaper/" in href:
                links.append(href)
                print(href)
    except:
        pass

    for link in links:
        driver.get(link)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='swiper-wrapper']"))
            )
            elems = driver.find_elements_by_xpath("//div[@class='swiper-wrapper']/div/img")
            url = elems[-1].get_attribute("src").replace("/xs/","/m/")
            print(url)
            request.urlretrieve(url, url.split('/')[-1])

        except:
            pass



driver.quit()

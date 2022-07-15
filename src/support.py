import pandas as pd
import pickle


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def scrap_actors(list_): 

    personal_actors = {"name": [], 
                    "image": [], 
                    "description": [], 
                    "positions": [], 
                    "known_for": []}

    for element in list_: 
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)

        driver.get("https://www.imdb.com/")
        driver.find_element_by_xpath("/html/body/div[2]/nav/div[2]/div[1]/form/div[2]/div/input").send_keys(element, Keys.ENTER)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()

        
        
        personal_actors["name"].append(element)
        personal_actors["positions"].append(driver.find_element_by_css_selector('#name-job-categories').text)
        personal_actors["image"].append(driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/table/tbody/tr[2]/td/div/div[1]/a/img').get_attribute("src"))
        
        personal_actors["known_for"].append(driver.find_element_by_css_selector("#knownfor > div:nth-child(1) > div.knownfor-title-role").text)

        
        driver.find_element_by_css_selector('#name-bio-text > div > div > span > a').click()
        driver.implicitly_wait(10)
        personal_actors["description"].append(driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/p[1]').text)

        
    driver.quit()

    return pd.DataFrame(personal_actors)

def scrap_directors(list_):

    personal_directors = {"name": [], 
                    "image": [], 
                    "description": [], 
                    "positions": []}


    for director in list_: 
    
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)

        driver.get("https://www.imdb.com/")
        driver.find_element_by_xpath("/html/body/div[2]/nav/div[2]/div[1]/form/div[2]/div/input").send_keys(director, Keys.ENTER)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()

        personal_directors["name"].append(director)
        personal_directors["image"].append(driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/table/tbody/tr[2]/td/div/div[1]/a/img').get_attribute("src"))
        
        try: 
        
            personal_directors["positions"].append(driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/div[2]').text)
        except:
            personal_directors["positions"].append(driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/table/tbody/tr[1]/td/div[1]').text)

        try: 
            driver.find_element_by_css_selector('#name-bio-text > div > div > span > a').click()
            driver.implicitly_wait(10)
            personal_directors["description"].append(driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/p').text)
        except: 
            personal_directors["description"].append(f"No description for {director}")

    return pd.DataFrame(personal_directors)








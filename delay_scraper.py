import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape(data):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://portalpasazera.pl/")
    wait = WebDriverWait(driver, 1)
    
    # cookies
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[29]/div[2]/div[4]/div/button[3]"))) 
        driver.find_element(By.XPATH, "/html/body/div[29]/div[2]/div[4]/div/button[3]").click()
    except NoSuchElementException:
        response = "Cookies button was no clickable!"
        driver.quit()
        return response

    driver.find_element(By.ID, "departureFrom").send_keys(data["departure_from"])
    driver.find_element(By.ID, "arrivalTo").send_keys(data["arrival_at"])
    driver.find_element(By.ID, "main-search__dateStart").send_keys(data["date"].strftime("%m.%d.%Y"))
    driver.find_element(By.ID, "main-search__timeStart").clear()
    driver.find_element(By.ID, "main-search__timeStart").send_keys(data["time"].strftime("%H:%M"))
    driver.find_element(By.XPATH, "/html/body/div[6]/div/form/div[11]/button").click() # search

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[2]/span"))) 
        delay_el = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[2]/span")
        delay = delay_el.text.split()[0].replace("(+", "")
        return int(delay)
    except TimeoutException:
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[2]/span[2]/span"))) 
        delay_el = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[2]/span[2]/span")
        delay = delay_el.text.split()[0].replace("(+", "")
        return int(delay)
    except NoSuchElementException:
        response = 0
        driver.quit()
        return response   
    finally:
        driver.quit()


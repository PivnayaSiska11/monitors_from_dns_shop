from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Андрей\\PycharmProjects\\pythonProject123\\chromedriver.exe")
base_url = "https://www.dns-shop.ru/"
driver.get(base_url)
driver.maximize_window()
search_engine = driver.find_element(By.XPATH, '//*[@id="header-search"]/div/div[2]/div[1]/input')
search_engine = search_engine.send_keys("игровые мониторы")
button_loupe = driver.find_element(By.XPATH, '//*[@id="header-search"]/div/div[2]/div[1]/div[2]/span[2]')
button_loupe.click()



time.sleep(15)
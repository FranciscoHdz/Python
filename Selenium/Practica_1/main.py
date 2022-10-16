import os
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"D:\SeleniumDriver"

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(3)
button_elemet = driver.find_element(By.ID,'downloadButton')
button_elemet.click()


WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,"progress-label"),#ELEMENTO
        "Complete!"#TEXTO
    )
)

button_elemet2 = driver.find_element(By.CLASS_NAME,'ui-dialog-buttonset')
button_elemet2 = button_elemet2.find_element(By.CLASS_NAME,'ui-button')
button_elemet2.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(100)
driver.get("https://www.health.gov.au/health-alerts/covid-19/case-numbers-and-statistics")
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "widgetgjjZnj")))
rows = len(driver.find_elements(By.XPATH,"//*[@id=\"widgetgjjZnj\"]/div/table/tbody/tr"))
columns = len(driver.find_elements(By.XPATH,"//*[@id=\"widgetgjjZnj\"]/div/table/tbody/tr[2]/td"))
before_XPath = "//*[@id='widgetgjjZnj']/div/table/tbody/tr["
aftertd_XPath = "]/td["
aftertr_XPath = "]"
for t_row in range(1, (rows + 1)):
    for t_column in range(1, (columns + 1)):
        FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
        print(FinalXPath)
        cell_text = driver.find_element_by_xpath(FinalXPath).text
        # print(cell_text, end = '               ')
        print(cell_text)
        print() 
driver.close()



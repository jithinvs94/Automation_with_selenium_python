from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
# # randrange()

# list1 = [android smartphone,smartphone]
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("--------------------------------")
print("WebDriver Manager successfully initialized.")
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
sleep(random.randrange(2,5))
search_field = driver.find_element(By.ID, "twotabsearchtextbox")
sleep(random.randrange(2,5))
search_field.send_keys(random.choice(["android smartphone","smartphone","smartphones","android smartphones"]))
sleep(random.randrange(2,5))
driver.find_element(By.ID, "nav-search-submit-button").click()
sleep(random.randrange(2,5))
# print(driver.page_source)
# driver.find_element(By.XPATH, "//li[@id='p_n_operating_system_browse-bin/1485077031']//a[contains(.,'Android')]").click()
# sleep(random.randrange(2,5))
# driver.find_element(By.PARTIAL_LINK_TEXT, "Top Brand").click()
# sleep(random.randrange(2,5))

# driver.find_element(By.ID, "p_72/1318476031").click()
# sleep(random.randrange(2,5))
# driver.find_element(By.ID, "low-price").send_keys(random.choice([15000,17000,18000]))
# sleep(random.randrange(2,5))
# driver.find_element(By.ID, "high-price").send_keys(random.choice([20000,22000,24000]))
# sleep(random.randrange(2,5))
# driver.find_element(By.XPATH, "//li[@id='p_36/price-range']//span[@class='a-button-inner']").click()
# # driver.find_element(By.ID, "a-autoid-1").click()
# sleep(random.randrange(2,5))

# print(driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//span[@class='a-size-base puis-light-weight-text s-link-centralized-style']").text)
driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a").click()
# products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
# print(len(products))
# for prod in products:
#     print(prod.get_attribute('data-cel-widget'))
#     temp = prod.find_element(By.XPATH, ".//span[@class='a-size-base puis-light-weight-text s-link-centralized-style']")
    # if int(temp.text.strip().replace(',' , '')) > 1000:
    #     print('fuck')
    #     prod.click()
    #     break
    # elements = prod.find_elements(By.TAG_NAME, "a")
    # for element in elements:
    #     print(element.get_attribute('innerHTML'))
    # # print(element.text)
    

    # print(prod.find_element(By.XPATH, "/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/a/span"))
#//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/a/span
# sleep(10)
# filtered_prod1 = [prod.find_elements(By.XPATH, "/a/span").text for prod in products]
# # print(len(filtered_prod1))

# products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']/@")








from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime, date
import random


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("--------------------------------")
print("WebDriver Manager successfully initialized.")
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
sleep(random.randrange(2,5))
search_field = driver.find_element(By.ID, "twotabsearchtextbox")
sleep(random.randrange(2,5))
# search_field.send_keys(random.choice(["android smartphone","smartphone","smartphones","android smartphones"]))
search_field.send_keys("android smartphone")
sleep(random.randrange(2,5))
driver.find_element(By.ID, "nav-search-submit-button").click()
sleep(random.randrange(2,5))
# driver.find_element(By.XPATH, "//li[@id='p_n_operating_system_browse-bin/1485077031']//a[contains(.,'Android')]").click()
# sleep(random.randrange(2,5))
# driver.find_element(By.PARTIAL_LINK_TEXT, "Top Brand").click()
# sleep(random.randrange(2,5))

driver.find_element(By.ID, "p_72/1318476031").click()
sleep(random.randrange(2,5))
driver.find_element(By.ID, "low-price").send_keys(10000)
sleep(random.randrange(2,5))
driver.find_element(By.ID, "high-price").send_keys(15000)
sleep(random.randrange(2,5))
driver.find_element(By.XPATH, "//li[@id='p_36/price-range']//span[@class='a-button-inner']").click()
sleep(random.randrange(2,5))

# driver.find_element(By.XPATH, '//a[contains(@class,"s-pagination-next")]').click()
# print('hiiiiiii')
# sleep(random.randrange(4,5))
# driver.find_element(By.XPATH, '//a[contains(@class,"s-pagination-next")]').click()
# sleep(random.randrange(4,5))
# print('hiiiiiii')
results = []
# print(driver.find_element(By.XPATH, '//div[contains(@cel_widget_id,"MAIN-SEARCH_RESULTS-1")]').get_attribute('innerHTML'))
ct = 0
while ct < 20:
    result_count = len(driver.find_elements(By.XPATH, '//div[contains(@cel_widget_id,"MAIN-SEARCH_RESULTS-")]'))
    parent_page = driver.current_window_handle
    for n in range(1, result_count+1):
        try:
            id = "MAIN-SEARCH_RESULTS-"+str(n)
            review_count = driver.find_element(By.XPATH, '//div[contains(@cel_widget_id,\"'+id+'\")]//div[contains(@class,"s-list-col-right")]//div[@class="a-section a-spacing-none a-spacing-top-micro"]//div[@class="a-row a-size-small"]//span//span[@class="a-size-base s-underline-text"]')

            if int(review_count.text.replace(',','').replace('(','').replace(')',''))>100:
                driver.find_element(By.XPATH, '//div[contains(@cel_widget_id,\"'+id+'\")]//div[contains(@class,"s-list-col-right")]//h2//a').click()
                driver.switch_to.window(driver.window_handles[1])
                print(driver.title)
                published_date = driver.find_element(By.XPATH, '//table[@id="productDetails_detailBullets_sections1"]//tr[contains(.,"Date First Available")]//td').text
                d0 = (datetime.strptime(published_date.strip(), "%d %B %Y"))
                d1 = datetime.today()
                days_data = str(d1-d0).split()
                days_old = int(days_data[0])
                rating = (driver.find_element(By.XPATH, '//table[@id="productDetails_detailBullets_sections1"]//tr[contains(.,"Customer Reviews")]//td').text).split()
                if 'Renewed' not in driver.find_element(By.ID, 'productTitle').text and 'Add to Cart' in driver.find_element(By.ID, 'submit.add-to-cart-announce').text and days_old<365:
                    results.append([driver.find_element(By.XPATH, '//span[@id="productTitle"]').text, int(driver.find_element(By.XPATH, '//span[contains(@class,"priceToPay")]//span[@class="a-price-whole"]').text.replace(',','')), float(rating[2]), int(rating[0]), driver.current_url])
                    ct += 1
                    if ct == 20:
                        break
                    print(results)
                    driver.close()
                    driver.switch_to.window(parent_page)
                    sleep(random.randrange(6,8))

        except:
            pass
    print(len(results))
    for num, result in enumerate(results):
        print(".....")
        print(num+1)
        print(".....")
        print("Name: "+result[0])
        print("Price: "+str(result[1]))
        print("Rating: "+str(result[2]))
        print("Review Count: "+str(result[3]))
        print("URL: "+result[4])
    
    if ct < 20:
        try:
            driver.find_element(By.XPATH, '//a[contains(@class,"s-pagination-next")]').click()
        except:
            break

print(len(results))
for num, result in enumerate(results):
    print(".....")
    print(num+1)
    print(".....")
    print("Name: "+result[0])
    print("Price: "+str(result[1]))
    print("Rating: "+str(result[2]))
    print("Review Count: "+str(result[3]))
    print("URL: "+result[4])

sleep(10)











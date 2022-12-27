from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randrange
from selenium.webdriver.common.keys import Keys

class InstaUnfollowers:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("--------------------------------")
        print("WebDriver Manager successfully initialized.")
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
        sleep(2)
        # Accept cookies
        try:
            accept_all_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
            accept_all_btn.click()
            sleep(randrange(2,4))
        except:
            pass
       
        # Expect Manual-Login
        if login == "manual":
            print("Please log in to your account in the opened window and confirm any text and press enter.")
            print("You can also exit the program with 'exit'")
            waitforinput = input(">> ")
            if waitforinput == "exit":
                quit()
            print("Continue...")

    def get_unfollowers(self):
        # Go to given account
        print("Accessing profile...")
        self.driver.get(accountUrl)
        sleep(randrange(3,6))
        # Get following people
        print("Getting following people, this might take a while...")
        following_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, local2)
        following_element.click()
        following_list = self.get_people()
        # Get followers
        print("Getting followers, this might take a while...")
        followers_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, local1)
        followers_element.click()
        followers_list = self.get_people()
        # Get not following people in list
        not_following_back = [user for user in following_list if user not in followers_list]
        # print data in ordered list
        not_following_back.sort()
        print("These people are not following you:")
        for name in not_following_back:
            print(name)
        print("Total: " + str(len(not_following_back)))

    def less_active(self):
        print("Accessing profile...")
        self.driver.get(accountUrl)
        sleep(randrange(3,6))
        followers_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, local1)
        followers_element.click()
        followers_list = self.get_people()
        sleep(randrange(3,5))
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        sleep(randrange(3,5))
        active_followers = {}
        for x in range(1,3):
            for y in range(1,4):
                xpath_cus = '//article[@class="x1iyjqo2"]//div[@class="_ac7v _aang"]['+str(x)+']//div[@class="_aabd _aa8k _aanf"]['+str(y)+']//a'
                post = self.driver.find_element(By.XPATH, xpath_cus)
                post.click()
                sleep(randrange(3,6))
                self.driver.find_element(By.PARTIAL_LINK_TEXT, 'others').click()
                sleep(randrange(3,6))
                scroll_box = self.driver.find_element(By.XPATH, "//*[@class='_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o _ab9s _abcm']/div[1]")
                prev_height, height = 0, 1
                liked = {}
                # Execute while there are more people to load
                while prev_height != height:
                    prev_height = height
                    sleep(randrange(3,5))
                    height = self.driver.execute_script("""
                        arguments[0].scrollTo(0, (arguments[0].scrollTop + 400)); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
                    sleep(randrange(3,5))
                    links = scroll_box.find_elements(By.TAG_NAME, 'a')
                    names = [name.text for name in links if name.text != '']
                    for name in names:
                        if name in followers_list:
                            if name not in liked:
                                liked.update({name: 1})
                sleep(randrange(3,5))
                print("Got one list of followers: " + str(len(liked)))
                # links = scroll_box.find_elements(By.TAG_NAME, 'a')
                # names = [name.text for name in links if name.text != '']
                for name in liked:
                    if name not in active_followers:
                        active_followers.update({name: 1})
                    elif name in active_followers:
                        active_followers[name] += 1
                sleep(randrange(3,5))
                sorted_list = sorted(active_followers.items(), key=lambda x: x[1], reverse=True)
                for item in sorted_list:
                    print(item)
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                sleep(randrange(3,5))
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                sleep(randrange(3,6))
        print("...................")
        print("...................")
        print("...................")
        print("The final result is")
        print("...................")
        print("...................")
        print("...................")
        sorted_list = sorted(active_followers.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_list:
            print(item)

        print("...................")
        print("...................")
        print("...................")
        print("Not active fuckers")
        print("...................")
        print("...................")
        print("...................")
        for name in followers_list:
            if name not in active_followers:
                print(name)


        # self.driver.find_element(By.XPATH, '//article[@class="x1iyjqo2"]//div[@class="_ac7v _aang"][1]//div[@class="_aabd _aa8k _aanf"][2]//a').click()

    def get_people(self):  # Get people in list, return as list
        sleep(randrange(2,4))
        # Access scroll-box
        scroll_box = self.driver.find_element(By.CLASS_NAME, "_aano")
        prev_height, height = 0, 1
        # Execute while there are more people to load
        while prev_height != height:
            prev_height = height
            sleep(randrange(3,5))
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        # Get people by anchor elements
        links = scroll_box.find_elements(By.TAG_NAME, 'a')
        names = [name.text for name in links if name.text != '']
        print("Got one list of: " + str(len(names)))
        sleep(randrange(3,5))
        self.driver.get(accountUrl)
        sleep(randrange(3,5))
        return names


# Entry-Point
print("--------------------------------")
print("   Instagram Unfollow-Checker")
print("--------------------------------\n")
# # Ask user for account name
# print("Enter the account name you want to check.")
# account = input("*The profile has to be accessible from the credentials you set. (public or followed)*\n>> ")
accountUrl = "https://instagram.com/____ji_th_in/"

# Ask user for language and set localization
local1, local2 = "follower", "following"


login = "manual"

# Run bot
print("Initializing WebDriver Manager")
print("--------------------------------")
sleep(1)
my_bot = InstaUnfollowers()
# my_bot.get_unfollowers()
my_bot.less_active()
# try:
#     my_bot.driver.close()
# except:
#     print("Fail")
#     my_bot.driver.close()
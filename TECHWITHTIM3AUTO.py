from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#OPENS UP TECHWITHTIM, INPUT SEARCH, CHOOSE PREFERED ARTICLE.
#HANDLES CASES: 0 articles, and 1 to 10 articles.

class ChromeAuto:
    def __init__(self):
        self.driver_path = '/Users/Blaustein/desktop/chromedriver102'
        self.options = webdriver.ChromeOptions()
        self.options = self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)
    def get_links_text(self):
        time.sleep(1)
        list_links = []
        try:
            for i in range(10):
                try:
                    link = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[" + 
                    str(i + 1) + "]").text 
                    list_links.append(link)
                except: pass
            return list_links
        except:
            return False
    def get_link_name(self):
        time.sleep(1)
        list_link_text = []
        try:
            for i in range(10):
                try:
                    link = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[" + str(i + 1) + 
                    "]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                    list_link_text.append(link)
                except:
                    pass
        except:
            return False
    def click_link(self):
        time.sleep(1)
        links = {}
        try:
            for i in range(10):
                try:
                    link = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[" + str(i + 1) + 
                    "]/header[1]/div[1]/span[1]/a[1]/time[1]")
                    links[str(i + 1)] = link
                except:
                    pass
            
            print("Which article would you like to proceed to? Please type in Number: ")
            article = int(input())
            if article > 0 and article < 11:
                for i in range(len(links)):
                    if article == i:
                        links[str(article)].click()
            else:
                return False
            return True
        except:
            return False
                
        

#Compare texts. If I can assign each link  a number, I can do this. 


if __name__ == '__main__':
    driver = ChromeAuto()
    driver.chrome.get("https://www.techwithtim.net/")

    search = driver.chrome.find_element(By.NAME, "s")
    search.send_keys(input("Please search what you are looking for: "))
    search.send_keys(Keys.RETURN)
    
    if driver.get_links_text() == False or driver.get_link_name() == False:
        print("Error Has Occurred While Searching. Not Enough Articles.")
    else:
        link_list_name = driver.get_links_text() 
        list_link_text = driver.get_link_name()

        for i in range(len(link_list_name)):
            print("Article " + str(i + 1) + ":" + "\n")
            print("Name Of Link: " + link_list_name[i] + "\n")

    if driver.click_link() == True:
        pass
    else:
        print("No Links or Link Out Of Bounds")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#OPENS UP TECHWITHTIM, SEARCHES PYTHON, GIVES LIST AND DESCRIPTION OF POPUPS, ALLOWS YOU TO INPUT TO CLICK
class ChromeAuto:
    def __init__(self):
        self.driver_path = '/Users/Blaustein/desktop/chromedriver102'
        self.options = webdriver.ChromeOptions()
        self.options = self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)
    def get_links_text(self):
        time.sleep(1)
        #Vuscar sobre XPATH. /html/body/div/
        #Automticar
        link1 = self.chrome.find_element(By.ID, "post-3303").text
        link2 = self.chrome.find_element(By.ID, "post-3182").text
        link3 = self.chrome.find_element(By.ID, "post-2940").text
        link4 = self.chrome.find_element(By.ID, "post-2896").text
        link5 = self.chrome.find_element(By.ID, "post-2888").text
        link6 = self.chrome.find_element(By.ID, "post-2776").text
        link7 = self.chrome.find_element(By.ID, "post-2768").text
        link8 = self.chrome.find_element(By.ID, "post-1556").text
        link9 = self.chrome.find_element(By.ID, "post-183").text
        link10 = self.chrome.find_element(By.ID, "post-175").text
        list_links = [link1, link2, link3, link4, link5, link6, link7, link8, link9, link10]
        return list_links
    def get_link_name(self):
        link1 = self.chrome.find_element(By.LINK_TEXT, "May 28, 2019").text
        link2 = self.chrome.find_element(By.LINK_TEXT, "May 5, 2019").text
        link3 = self.chrome.find_element(By.LINK_TEXT, "March 21, 2019").text
        link4 = self.chrome.find_element(By.LINK_TEXT, "March 14, 2019").text
        link5 = self.chrome.find_element(By.LINK_TEXT, "March 12, 2019").text
        link6 = self.chrome.find_element(By.LINK_TEXT, "February 28, 2019").text
        link7 = self.chrome.find_element(By.LINK_TEXT, "February 12, 2019").text
        link8 = self.chrome.find_element(By.LINK_TEXT, "January 13, 2019").text
        link9 = self.chrome.find_element(By.LINK_TEXT, "December 3, 2018").text
        link10 = self.chrome.find_element(By.LINK_TEXT, "December 3, 2018").text
        list_link_text = [link1, link2, link3, link4, link5, link6, link7, link8, link9, link10]
        return list_link_text
    def click_link(self):
        link1 = self.chrome.find_element(By.LINK_TEXT, "May 28, 2019")
        link2 = self.chrome.find_element(By.LINK_TEXT, "May 5, 2019")
        link3 = self.chrome.find_element(By.LINK_TEXT, "March 21, 2019")
        link4 = self.chrome.find_element(By.LINK_TEXT, "March 14, 2019")
        link5 = self.chrome.find_element(By.LINK_TEXT, "March 12, 2019")
        link6 = self.chrome.find_element(By.LINK_TEXT, "February 28, 2019")
        link7 = self.chrome.find_element(By.LINK_TEXT, "February 12, 2019")
        link8 = self.chrome.find_element(By.LINK_TEXT, "January 13, 2019")
        link9 = self.chrome.find_element(By.LINK_TEXT, "December 3, 2018")
        link10 = self.chrome.find_element(By.LINK_TEXT, "December 3, 2018")
        print("Which article would you like to proceed to? Please type in Number: ")
        article = int(input())
        links = {'1': link1, '2': link2, '3': link3, '4': link4, '5': link5, 
        '6': link6, '7': link7, '8': link8, '9': link9, '10': link10}
        for i in range(13):
            if article == i:
                links[str(article)].click()
                
        

#Compare texts. If I can assign each link  a number, I can do this. 


if __name__ == '__main__':
    driver = ChromeAuto()
    driver.chrome.get("https://www.techwithtim.net/")

    search = driver.chrome.find_element(By.NAME, "s")
    search.send_keys("Python")
    search.send_keys(Keys.RETURN)
    

    link_list_name = driver.get_links_text()
    list_link_text = driver.get_link_name()

    for i in range(10):
        print("Article " + str(i + 1) + ":" + "\n")
        print("Name Of Link: " + link_list_name[i] + "\n")

    driver.click_link()


    


    



#Goal: Automaticate program

#Steps:
#1. Learn XPATH
#2. Learn XPATH tools
#3Learn how to automaticate via XPATH
#4. Secure the win. 




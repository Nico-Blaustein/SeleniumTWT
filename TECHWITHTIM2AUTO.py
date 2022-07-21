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
            #Automate: Is there always 10 per 
            try: 
                link1 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[1]").text 
                list_links.append(link1)

            except:
                pass
            try:
                link2 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[2]").text
                list_links.append(link2)

            except:
                pass
            try:
                link3 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[3]").text
                list_links.append(link3)

            except:
                pass
            try:
                link4 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[4]").text
                list_links.append(link4)

            except:
                pass
            try:
                link5 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[5]").text
                list_links.append(link5)

            except:
                pass
            try:
                link6 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[6]").text
                list_links.append(link6)

            except:
                pass
            try:
                link7 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[7]").text
                list_links.append(link7)

            except:
                pass
            try:
                link8 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[8]").text
                list_links.append(link8)

            except:
                pass
            try:
                link9 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[9]").text
                list_links.append(link9)

            except:
                pass
            try:
                link10 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[10]").text
                list_links.append(link10)
            except: pass
            return list_links
        except:
            return False
    def get_link_name(self):
        time.sleep(1)
        try:
            list_link_text = []
            try:
                link1 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[1]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link1)
            except:
                pass

            try:
                link2 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[1]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link2)
            except: 
                pass

            try:
                link3 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[3]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link3)
            except:
                pass

            try:
                link4 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[4]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link4)
            except: 
                pass

            try:
                link5 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[5]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link5)
            except:
                pass

            try:
                link6 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[6]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link6)
            except:
                pass

            try:
                link7 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[7]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link7)
            except:
                pass

            try:
                link8 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[8]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link8)
            except:
                pass

            try:
                link9 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[9]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link9)
            except:
                pass

            try:
                link10 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[10]/header[1]/div[1]/span[1]/a[1]/time[1]").text
                list_link_text.append(link10)
            except:
                pass
            return list_link_text
        except:
            return False
    def click_link(self):
        time.sleep(1)
        links = {}
        try:
            try:
                link1 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[1]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['1'] = link1
            except:
                pass

            try:
                link2 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[1]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['2'] = link2
            except:
                pass

            try:
                link3 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[3]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['3'] = link3
            except:
                pass

            try:
                link4 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[4]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['4'] = link4
            except:
                pass

            try:
                link5 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[5]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['5'] = link5
            except:
                pass

            try:
                link6 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[6]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['6'] = link1
            except:
                pass

            try:
                link7 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[7]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['7'] = link1
            except:
                pass

            try:
                link8 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[8]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['8'] = link1
            except:
                pass

            try:
                link9 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[9]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['9'] = link1
            except:
                pass

            try:
                link10 = self.chrome.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/main[1]/article[10]/header[1]/div[1]/span[1]/a[1]/time[1]")
                links['10'] = link1
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

#The problem is that if selenium attempts to grab an element and its not there, the compiler receives an error. 
#Maybe TRY blocks, because they are able to cirumvent error. 

#When I type 11, the program does not care, because I place the length of the LinksList as the condtion. Thus, it does fail and 
#returns true. Because if no links, length is zero, for loop never runs, no index out of bounds. 
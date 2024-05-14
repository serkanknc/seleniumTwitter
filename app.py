from selenium import webdriver
from selenium.webdriver.common.by import By
import infoLogin
import time

browser = webdriver.Chrome()
url = "https://twitter.com/"
browser.get(url)
time.sleep(2)

sign_in = browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div/span/span')
sign_in.click()
time.sleep(2)

username=browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
nextButton= browser.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
username.send_keys(infoLogin.username)
nextButton.click()
time.sleep(2)

password = browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
loginButton = browser.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
password.send_keys(infoLogin.password)
loginButton.click()
time.sleep(7)




searchArea = browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
searchArea.send_keys('#yazilimtest')
searchArea.submit()
time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

tweets= []
tweetCount = 1

elements = browser.find_elements(By.CSS_SELECTOR, 'div.css-146c3p1.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim')
for element in elements:
    tweets.append(element.text)

with open("tweets.txt","w",encoding="UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount)+ ".tweet\n" + tweet + "\n")
        file.write("*********************\n")

        tweetCount +=1
        


browser.close()






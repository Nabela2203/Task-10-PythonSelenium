# Using Python Selenium Automation and the URL https://www.instagram.com/guviofficial/
# kindly do the following mentioned taskS :-
# 1) Use either Relative or Absolute XPATH only for the task.
# 2) Extract the total number of Followers and Following from the URL mentioned above.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

driver.implicitly_wait(5)
driver.get("https://www.instagram.com/guviofficial/")

followers = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[2]/span").text
print("followers: ", followers)

following = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[3]/span").text
print("following: ",following)

driver.quit()
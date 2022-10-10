from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
## import pytest

url = "https://www.flipkart.com/"
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)

# def test_flipKartTest():
#     url = "https://www.flipkart.com/"
#     driver = webdriver.Firefox()
#     driver.get(url)
#     print("Launched URL: ", url)
#     checkLogin(driver)
#     checkEmailField(driver)
#     checkPasswordField(driver)
#     checkLoginButton(driver)
#     clickCloseButton(driver)
#     checkCategoriesBanner(driver)
#     clickMobiles(driver)
#     print("Waiting for 5 seconds....")
#     time.sleep(5)
#     # clickFirstPhone(driver)
#     # print("Waiting for 5 seconds....")
#     # time.sleep(5)
#     verifyFilter(driver)
#     updatePriceFilter(driver)
#     verifyNeedHelp(driver)
#     print("Waiting for 20 seconds....")
#     time.sleep(20)
#     driver.quit()
#     driver.close()

def test_checkLogin():
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[1]/span/span").text == "Login"
    print("Login Title found: ", b)
    assert b

def test_checkEmailField():
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").is_displayed()
    print("EMAIL Field Found: ", b)
    assert b

def test_checkPasswordField():
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").is_displayed()
    print("Password Field Found: ", b)
    assert b

def test_checkLoginButton():
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").is_displayed()
    print("Login Button Found: ", b)
    assert b

def test_clickCloseButton():
    print("Clicking Close Button....")
    driver.find_element("xpath", "/html/body/div[2]/div/div/button").click()
    print("Close Button Clicked")

def test_checkCategoriesBanner():
    b = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div").is_displayed()
    print("Categories Banner Found: ", b)
    assert b

def test_clickMobiles():
    print("Clicking Mobiles....")
    driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[3]/a/div[2]").click()
    print("Mobiles Clicked")

# def test_clickFirstPhone():
#     print("Clicking First Phone....")
#     driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[3]/div/div[1]").click()
#     print("First Phone Clicked")

def test_verifyFilter():
    print("Verifying Filter....")
    ## /html/body/div[1]/div/div[3]/div[2]/div[1]/div/section[1]/div/div/span
    b = driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[2]/div[1]/div/section[1]/div/div/span").text == "Filters"
    # b = driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[1]/div[1]/div[1]/span").text == "Filters"
    print("Filters Found: ", b)
    assert b

def test_updatePriceFilter():
    print("Updating Price Filter....")
    #/html/body/div[1]/div/div[3]/div[2]/div[1]/div/section[2]/div[4]/div[3]/select
    select = Select(driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[2]/div[1]/div/section[2]/div[4]/div[3]/select"))
    # select = Select(driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[3]/select"))
    select.select_by_visible_text("₹20000")
    print("Price Filter Updated")

def test_verifyNeedHelp():
    print("Scrolling Down....")
    driver.find_element("tag name", "body").send_keys(Keys.END)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Verifying Need Help....")
    ## /html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/a/div[1]/span
    elem = driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/a/div[1]/span")
    assert elem.location_once_scrolled_into_view
    b: bool = elem.text == "Need help?"
    print("Need Help Found: ", b)
    assert b
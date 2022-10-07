from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def flipKartTest():
    url = "https://www.flipkart.com/"
    driver = webdriver.Firefox()
    driver.get(url)
    print("Launched URL: ", url)
    assert checkLogin(driver)
    assert checkLogin(driver)
    assert checkEmailField(driver)
    assert checkPasswordField(driver)
    assert checkLoginButton(driver)
    clickCloseButton(driver)
    assert checkCategoriesBanner(driver)
    clickMobiles(driver)
    print("Waiting for 5 seconds....")
    time.sleep(5)
    clickFirstPhone(driver)
    print("Waiting for 5 seconds....")
    time.sleep(5)
    assert verifyFilter(driver)
    updatePriceFilter(driver)
    assert verifyNeedHelp(driver)
    print("Waiting for 20 seconds....")
    time.sleep(20)
    driver.quit()
    driver.close()

def checkLogin(driver):
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[1]/span/span").text == "Login"
    print("Login Title found: ", b)
    return b

def checkEmailField(driver):
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").is_displayed()
    print("EMAIL Field Found: ", b)
    return b

def checkPasswordField(driver):
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").is_displayed()
    print("Password Field Found: ", b)
    return b

def checkLoginButton(driver):
    b = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").is_displayed()
    print("Login Button Found: ", b)
    return b

def clickCloseButton(driver):
    print("Clicking Close Button....")
    driver.find_element("xpath", "/html/body/div[2]/div/div/button").click()
    print("Close Button Clicked")

def checkCategoriesBanner(driver):
    b = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div").is_displayed()
    print("Categories Banner Found: ", b)
    return b

def clickMobiles(driver):
    print("Clicking Mobiles....")
    driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[2]/a/div[2]").click()
    print("Mobiles Clicked")

def clickFirstPhone(driver):
    print("Clicking First Phone....")
    driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[3]/div/div[1]").click()
    print("First Phone Clicked")

def verifyFilter(driver):
    print("Verifying Filter....")
    b = driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[1]/div[1]/div[1]/span").text == "Filters"
    print("Filters Found: ", b)
    return b

def updatePriceFilter(driver):
    print("Updating Price Filter....")
    select = Select(driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[3]/select"))
    select.select_by_visible_text("₹20000")
    print("Price Filter Updated")

def verifyNeedHelp(driver):
    print("Scrolling Down....")
    driver.find_element("tag name", "body").send_keys(Keys.END)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Verifying Need Help....")
    elem = driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/a/div[1]/span")
    assert elem.location_once_scrolled_into_view
    b = elem.text == "Need help?"
    print("Need Help Found: ", b)
    return b

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flipKartTest()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

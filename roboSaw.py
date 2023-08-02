from selenium import webdriver

url = "https://techelement.neocities.org/the-back/reverse-captcha"

driver = webdriver.Chrome()

# navigate to site
driver.get(url)

equationElement = driver.find_element("id", "equation")
textBox = driver.find_element("id", "ans")
sendButton = driver.find_element("xpath", "//button")

eqText = equationElement.get_attribute("innerHTML")
eqTextCut = eqText[:-2]
# print(eval(eqTextCut))

textBox.send_keys(eval(eqTextCut))
sendButton.click()



input()
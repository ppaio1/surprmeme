import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import keys
driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options
chrome_options = Options()



print("ℙℙ𝔸𝕀𝕆")
driver = webdriver.Chrome('C:\Program Files (x86)\\chromedriver.exe')
driver.Chrome.get('https://www.supremenewyork.com/shop')
time.sleep(2) 
driver.refresh
time.sleep(1)

driver.find_element_by_xpath('//*[@id="nav-store"]/li[1]/a').click()
time.sleep(1)

driver.refresh
time.sleep(1)

driver.find_element_by_xpath('//*[@id="nav-store"]/li[6]/a').click()
time.sleep(1)


driver.get(keys['product_url'])

element = driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input')
driver.execute_script("arguments[0].click();", element)
print("ℙℙ𝔸𝕀𝕆")
print("added to cart")
time.sleep(0.1)

# auto fill 
driver.get('https://www.supremenewyork.com/checkout')
driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys['card_number'])
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
driver.find_element_by_xpath('//*[@id="pay"]/input').click()
time.sleep(999999)
print("SOLVE recaptcha")

print('when done just close the tab ;)')
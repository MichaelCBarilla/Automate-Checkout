# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 20:08:20 2019

@author: Michael
"""

import json
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class Product:
    def __init__(self, productURL = None, sizeOptions = None, colorOptions = None):
        self.productURL = productURL
        self.sizeOptions = sizeOptions
        self.colorOptions = colorOptions




def availabilityCheck(productName):
    r = requests.get('https://feature.com/products.json')
    products = json.loads((r.text))['products']
    for product in products:

        if productName == product['title']:
            
            myProduct = Product()
            myProduct.productURL = 'https://feature.com/products/' + product['handle']
            getOptions(myProduct)
            return myProduct
    
    return False






def getOptions(product):
    productJSON = product.productURL + '.json'
    r = requests.get(productJSON)
    options = json.loads((r.text))['product']['options']
    index = 0
    while product.sizeOptions == None or product.colorOptions == None:
        option = options[index]
        if option['name'] == 'Size':
            product.sizeOptions = option['values']
        elif option['name'] == 'Color':
            product.colorOptions = option['values']
            
        index += 1
        
    return product


    
    
    
    
def slowdown(xpath, text, driver, charSpeed):
    el = driver.find_element_by_xpath(xpath)
    for character in text:
        el.send_keys(character)
        time.sleep(charSpeed)





def buyProduct(product):
    #Start webdriver
    driver = webdriver.Chrome(executable_path = r'C:\webdrivers\chromedriver.exe')
    
    #Open product page
    driver.get(product.productURL)
    
    #Select size
    driver.find_element_by_xpath('//div[@data-value="' + product.sizeOptions[0] + '"]').click()
    
    #Select Color
    driver.find_element_by_xpath('//div[@data-value="' + product.sizeOptions[0] + '"]').click()
    #Add to cart
    time.sleep(0.5)
    driver.find_element_by_xpath('//button[@class="primary-btn add-to-cart"]').click()
    
    #Wait for cart to open
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/checkout"]'))).click()
    
    #Enter email
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys('example2@gmail.com')

    #Enter first name
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Michael')
    
    #Enter last name
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Barilla')
    
    #Enter address
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('Some address')
    
    #Enter city
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('Some city')
    
    #Enter Country
    time.sleep(0.5)
    driver.find_element_by_xpath('//option[@data-code="US"]').click()
    
    #Enter State
    time.sleep(0.5)
    driver.find_element_by_xpath('//option[@value="NJ"]').click()
    
    #Enter Zipcode
    time.sleep(0.5)
    driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys('08724')
    
    #Enter Phone Number
    slowdown('//input[@placeholder="Phone (We\'ll only contact you regarding your order)"]', '12345678901' + Keys.ENTER, driver, 0.05)
    
    #Continue to payment
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="step__footer__continue-btn btn"]'))).click()
    
    #Enter card number
    time.sleep(0.5)
    driver.find_element_by_xpath('//iframe[@title="Field container for: Card number"]').send_keys("1234567812345678")
    
    #Enter card name
    time.sleep(0.5)
    driver.find_element_by_xpath('//iframe[@title="Field container for: Name on card"]').send_keys("Michael Barilla")
    
    #Enter card EXP
    time.sleep(0.5)
    slowdown('//iframe[@title="Field container for: Expiration date (MM / YY)"]', "0817", driver, 0.05)
    
    #Enter card security code
    time.sleep(0.5)
    driver.find_element_by_xpath('//iframe[@title="Field container for: Security code"]').send_keys("123")






myProduct = availabilityCheck('New Balance 997 - Slate Green/Stone Blue/Linen Fog')
if myProduct == False:
    print("not available")
else:
    buyProduct(myProduct)
    print("Bought!")

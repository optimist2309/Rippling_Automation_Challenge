from selenium import webdriver
import requests
import re
import time

""""
So below code has written to assert the web-page for fun. 
It has written to sure that web-page is returning 200. 
"""
home_page_request = requests.get('https://vanilla-masker.github.io/vanilla-masker/demo.html')
status_code_for_request = home_page_request.status_code
if status_code_for_request == 200:
    print("Web page is working OK")

"""
VanillaMasker - It's a pure JavaScript mask input library.
VanillaMasker is used to mask the input elements.
So Only numbers text box will do ?
It will Convert any string to number.
Example has given below.
VMasker.toNumber("123ac34"); // -> 12334
VMasker.toNumber("-123ac34"); // -> -12334
So after playing with that text box below is test case to test this text box.
"""    
driver = webdriver.Chrome()
driver.get("https://vanilla-masker.github.io/vanilla-masker/demo.html")
time.sleep(10)

def for_only_numbers(input_value):
    inputElement = driver.find_element_by_id("numbers")
    inputElement.send_keys(input_value)
    text_box_value = inputElement.get_attribute('value')
    
    if "-" in input_value:
        removing_letter_special_ch_from_input = re.sub("\D", "", text_box_value)
        adding_negative_sign_if_removed_due_to_reg_ex = "-" + removing_letter_special_ch_from_input
        if(text_box_value == adding_negative_sign_if_removed_due_to_reg_ex):
            print("Assertion is passed")
        else:
            print("Assertion is failed")    
    else:
        removing_letter_special_ch_from_input = re.sub("\D", "", text_box_value)
        if (text_box_value == removing_letter_special_ch_from_input):
            print("Assertion is passed")
        else:
            print("Assertion is failed")
    inputElement.clear()
    
"""
This is the first case where input is alphanumeric. 
"""
for_only_numbers("123412340asdfghjk")

"""
This is the second test case where input is negative alphanumeric. 
"""

for_only_numbers("-123412340asdfghjk")

"""
This is the third case where input is like number,character,number. 
"""

for_only_numbers("123ac34")

"""
This is the fourth case where input is like number,character,number with negative sign. 
"""

for_only_numbers("-123ac34")

"""
This is the fifth case where input is special character. 
"""

for_only_numbers("@#!^!^!%^")

"""
This is the sixth case where input is negative number. 
"""

for_only_numbers("-142141212288")

"""
This is the seventh case where input is positive number. 
"""
for_only_numbers("142141212288")

"""
This is the seventh case where input is character. 
"""

for_only_numbers("abc")

for_only_numbers("i love you 3000") # Special Test case for Tony Stark.


def for_phone_number(input_value):
    inputElement = driver.find_element_by_id("phone")
    inputElement.send_keys(input_value)
    ph = inputElement.get_attribute('value')
    ph = ph.replace('(', '')
    ph = ph.replace(')', '')
    ph = ph.replace('-', '')
    ph = ph.replace(' ', '')
    if int(ph) == input_value:
        print("Assertion is passed")
    else:
        print("Assertion is failed")
    inputElement.clear()
    
"""
VanillaMasker - It's a pure JavaScript mask input library.
VanillaMasker is used to mask the input elements.
So Phone text box will do ?
It will convert any ten digit phone number into this format (12) 3456-7890.
So for phone there will be two test case phone number.
one is 10 digit phone number.
last is less than 10 digit number.
"""    
for_phone_number(1234567890) # Test case for 10 digit phone number.

for_phone_number(123456) # Test case for less that 10 digit phone number.

driver.quit()





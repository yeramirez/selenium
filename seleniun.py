from selenium import webdriver
import unittest
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time,json
import os

driver=webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe")

driver.get("https://simon.inder.gov.co/admin/login")
time.sleep(3)
# identify dropdown with Select class  //*[@id="tipo_documento"]
#s2id_autogen2//*[@id="select2-chosen-2"] /html/body/div[1]/div/div/section/div/section[1]/div/form/div[1]/div/a

select = driver.find_element_by_xpath("//*[@id='tipo_documento']")
opcion= select.find_elements_by_tag_name("option")
select_object = Select(opcion)
select_object.select_by_index(497)

#time.sleep(3)
#for option in opcion:
  #  print(option.get_attribute("value"))
    
    
 #   time.sleep(1)
#select_object = Select(driver.find_element_by_xpath("//*[@id='tipo_documento']"))
#select_object.select_by_value("CC")
driver.close

    


from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe")
driver.get("https://simon.inder.gov.co/admin/login")
time.sleep(2)
driver.find_element(By.ID,"s2id_tipo_documento").click()

##Nos logueamos en la pagina.
opcion=driver.find_element(By.CLASS_NAME,"select2-result-label")
opcion.click()
cc=driver.find_element(By.ID,'documento')
paswd=driver.find_element(By.ID,'password')
cc.send_keys("1047966575")
paswd.send_keys("Ramirez999")
driver.find_element(By.XPATH,"//*[@id='login']/div/form/div[4]/div[1]/button").click()

of=driver.find_elements(By.CLASS_NAME, "menu-simon")

for f in of:
    if f.text.find("Escenarios Deportivos") != -1:
        f.click()
        driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/div[4]/nav/div[2]/ul/ul/li[2]/ul/li[2]/a").click() 
        break
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/section/section/div[1]/nav/div/div/div[1]/ul/li/a").click()

###------Reserva-----------------
driver.find_element(By.ID,"select2-chosen-14").click()
br=driver.find_element(By.XPATH,"//*[@id='s2id_autogen14_search']")
br.send_keys("Manila")
br.send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='s2id_escenario_deportivo']").click()
ch=driver.find_element(By.XPATH,"//*[@id='s2id_autogen783_search']")
ch.send_keys("futbol")  
ch.send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='reserva_seleccion']/div[1]/ins").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='s2id_disciplina_escenario_deportivoreserva']").click()

ds=driver.find_element(By.XPATH,"//*[@id='s2id_autogen16_search']")
ds.send_keys("futbol")
ds.send_keys(Keys.RETURN)

driver.find_element(By.XPATH,"//*[@id='formulario_reserva_paso1']/div/div[2]/div[3]/div/div[1]/div[5]/div[3]/div[2]/div[1]").click()
fecha=driver.find_elements(By.XPATH,"/html/body/div[3]")

for dato in fecha:
    print(dato.text, end='')
    if "27" in dato.text:
        time.sleep(4)
        dato.click()
        time.sleep(4)
        
        break
    


#br=driver.find_elements(By.TAG_NAME,"select2-results")



#time.sleep(4)
#for bo in br:
 #   print(bo.text)
    
    
    #if bo.text.find("Manila - Poblado") != -1:
     #  print(bo.get_attribuete("value"))
      




driver.close
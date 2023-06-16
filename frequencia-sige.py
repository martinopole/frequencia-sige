from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

usuario = input("Qual o usuário do SIGE? ")
senha = input("Qual a senha? ")

driver = webdriver.Chrome()
#driver.switch_to.default_content()
driver.get("http://sige.seduc.ce.gov.br")
time.sleep(1)
iframe2 = driver.find_elements(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe2[1])
driver.execute_script("Acesso(1);")
time.sleep(1)
#driver.get("http://sige.seduc.ce.gov.br/login.asp")
#time.sleep(1)
#iframe2 = driver.find_elements(By.TAG_NAME, 'iframe')
#driver.switch_to.frame(iframe2[1])
nm_Codigo = driver.find_elements(By.NAME, 'nr_Codigo')
nm_Codigo[1].click()
nm_Login = driver.find_element(By.NAME, 'nm_Login')
nm_Senha = driver.find_element(By.NAME, 'nm_Senha')
nm_Login.send_keys(usuario)
nm_Senha.send_keys(senha)
nm_Senha.send_keys(Keys.ENTER)
time.sleep(1)
driver.get("http://sige.seduc.ce.gov.br/Academico/AlunoAvaliacao/Frequencia.asp?Inc_Alt=P")
time.sleep(5)
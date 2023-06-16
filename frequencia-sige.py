from selenium import webdriver

usuario = input("Qual o usuário do SIGE? ")
senha = input("Qual a senha? ")

driver = webdriver.Chrome()
driver.get("http://sige.seduc.ce.gov.br/")
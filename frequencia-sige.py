from selenium import webdriver

usuario = input("Qual o usuário do SIGE? ")
senha = input("Qual a senha? ")

driver = webdriver.Firefox()
driver.get("http://http://sige.seduc.ce.gov.br/")
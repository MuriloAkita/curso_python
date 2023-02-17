from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ChromeAuto:
    def __init__(self):
        self.service = Service('aula104/chromedriver')
        self.chrome = webdriver.Chrome(
            service=self.service
        )
        self.chrome.maximize_window()

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def login_click(self):
        try:
            login_button = self.chrome.find_element(By.ID, 'linkLoginHeader')
            login_button.click()
        except Exception as e:
            print(f'Erro na função login_click(): {e}')

    def login(self):
        try:
            input_username = self.chrome.find_element(
                By.CSS_SELECTOR, "input[type='text']")
            input_password = self.chrome.find_element(
                By.CSS_SELECTOR, "input[type='password']")
            
            input_username.send_keys('xxxxxx@gmail.com')
            input_password.send_keys('xxxxxx')
            
            login_button = self.chrome.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            sleep(5)
            popup = self.chrome.find_element(By.ID, 'buttonNaoTenhoInteresse')
            
            if popup:
                popup.click()
                
        except Exception as e:
            print(f'Erro na função login(): {e}')
        
    def logout(self):
        try:
            logout_button = self.chrome.find_element(By.ID, 'linkSairHeader')
            logout_button.click()
        except Exception as e:
            print(f'Erro na função logout(): {e}')


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://www.kabum.com.br/')
    chrome.login_click()
    chrome.login()
    sleep(1000)
    chrome.logout()
    sleep(10)
    chrome.sair()

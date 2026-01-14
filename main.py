import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

class MonkeyTypeBot:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.url = "https://monkeytype.com"

    def launch(self):
        self.driver.get(self.url)
        # 10 segundos para que aceptes cookies y elijas el modo de juego
        print("IMPORTANTE: Tienes 10 segundos para aceptar cookies y hacer clic en el área de letras")
        time.sleep(10)

    def start(self):
        self.launch()
        
        # Monkeytype usa un input oculto con el id 'wordsInput'
        try:
            input_field = self.driver.find_element(By.ID, "wordsInput")
        except:
            # Si no lo encuentra por ID, intentamos enviarlo al body
            input_field = self.driver.find_element(By.TAG_NAME, "body")

        print("Iniciando escritura...")
        
        while True:
            try:
                # Se localiza la palabra
                active_word = self.driver.find_element(By.CSS_SELECTOR, ".word.active")
                
                # Extraemos el texto de las letras
                letters = active_word.find_elements(By.TAG_NAME, "letter")
                word_text = "".join([l.text for l in letters])

                if word_text:
                    print(f"Escribiendo: {word_text}")
                    
                    for char in word_text:
                        input_field.send_keys(char)
                        time.sleep(random.uniform(0.04, 0.08))
                    
                    input_field.send_keys(Keys.SPACE)
                    time.sleep(0.02)

            except (StaleElementReferenceException, NoSuchElementException):
                continue
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    bot = MonkeyTypeBot()
    bot.start()
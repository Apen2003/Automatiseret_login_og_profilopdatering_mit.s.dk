from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

USERNAME = "dit_username_her"
PASSWORD = "Dit_password_her"



# Sti til din ChromeDriver
driver_path = r"C:\tools\Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Gå til login-siden
driver.get("https://mit.s.dk/studiebolig/login/?next=/studiebolig/home/")
time.sleep(0.25)
#klik cookie-knappen
wait = WebDriverWait(driver, 10)
# klik cookie-knappen
try:
    cookie_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cc-accept"))
    )
    cookie_btn.click()
    print("🍪 Cookie-popup accepteret.")
except:
    print("Ingen cookie-popup fundet.")



# Brug credentials
driver.find_element(By.ID, "id_username").send_keys(USERNAME)
driver.find_element(By.ID, "id_password").send_keys(PASSWORD + Keys.RETURN)


# Klik på "Min profil"
driver.find_element(By.XPATH, "//span[text()='Min profil']").click()
time.sleep(1.25)


# Vent på og klik "Forstået"-knappen i modal
try:
    forstaaet_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Forstået')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", forstaaet_btn)
    driver.execute_script("arguments[0].click();", forstaaet_btn)
    print("👉 Klikkede på 'Forstået'-knappen.")
except Exception as e:
    print("Kunne ikke klikke på 'Forstået'-knappen:", e)

time.sleep(1)

# Tjek boksen "confirm_information"
checkbox = driver.find_element(By.ID, "id_confirm_information")
if not checkbox.is_selected():
    checkbox.click()
time.sleep(0.5)
##hvis verdi er under 0.5 virker det ikke og der må ikke være et eksta enter



# Klik på knappen "Bekræft opskrivninger"
driver.find_element(By.ID, "renew-applications-btn").click()

time.sleep(3)

# Vent på og klik "Forstået"-knappen i modal
try:
    forstaaet_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Forstået')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", forstaaet_btn)
    driver.execute_script("arguments[0].click();", forstaaet_btn)
    print("👉 Klikkede på 'Forstået'-knappen.")
except Exception as e:
    print("Kunne ikke klikke på 'Forstået'-knappen:", e)

time.sleep(1.5)

# Tag et screenshot og gem det som PNG
screenshot = pyautogui.screenshot()
screenshot.save("screenshotchr.png")


# Lad browseren stå åben
print("✅ Scriptet er færdigt. Tryk Enter for at lukke browseren...")
input()  # venter på at du trykker Enter
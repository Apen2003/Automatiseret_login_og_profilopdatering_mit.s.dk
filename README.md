- Formål: hvad programmet gør.
- Forudsætninger: hvilke pakker, drivere og filer der skal være til stede.
- Brug: hvordan man kører det, og hvad brugeren skal gøre undervejs.
- Flow: trin for trin hvad scriptet udfører.
- Vedligeholdelse: hvor man kan ændre ting (fx login, driver‑sti, ventetider).


## Automatiseret login og profilopdatering på mit.s.dk med Selenium

Formål
Scriptet logger automatisk ind på studieboligportalen, accepterer cookie‑popup, åbner profilsiden, lukker introduktionsmodaler, markerer bekræftelsesfeltet og sender opskrivninger. Til sidst tages et skærmbillede som dokumentation.

Forudsætninger
- Python 3.11 eller nyere.
- Installerede pakker:

    ```bash
    pip install selenium pyautogui

- Chrome browser og matchende ChromeDriver placeret i C:\tools\Drivers\chromedriver-win64\chromedriver.exe.
- En credentials.py fil med


USERNAME = "dit_brugernavn"
PASSWORD = "dit_password"


Programflow
- Starter Chrome via Selenium.
- Går til login‑siden.
- Accepterer cookie‑popup hvis den vises.
- Logger ind med brugernavn og password fra credentials.py.
- Klikker på “Min profil”.
- Lukker modal med “Forstået”.
- Marker feltet “Bekræft oplysninger”.
- Klikker på “Bekræft opskrivninger”.
- Lukker modal med “Forstået” igen.
- Tager et screenshot og gemmer som screenshot.png.
- Lader browseren stå åben indtil brugeren trykker Enter.

Brugsanvisning
- Kør scriptet med:
    ```bash
    python web_alfa.py

- Følg output i terminalen.
- Når scriptet er færdigt, tryk Enter for at lukke browseren.


Vedligeholdelse
- Ventetider (time.sleep) kan justeres hvis siden loader langsomt.
- Driver‑sti skal pege på din ChromeDriver.
- Selectors (By.ID, By.XPATH) kan ændres hvis hjemmesiden ændrer struktur.
- Screenshot‑filnavn kan ændres i screenshot.save("...").

👉 Vil du have, at jeg laver en Markdown‑version af dokumentationen (så du kan gemme den som README.md), eller foretrækker du en kort docstring‑stil direkte i toppen af dit Python‑script?

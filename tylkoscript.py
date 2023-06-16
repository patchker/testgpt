import json
import pickle
import re
import sqlite3
import time
from datetime import datetime, timedelta

import numpy as np
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import app
import os
import pygame
from selenium.common.exceptions import NoSuchElementException

cookies = [
{'name' : 'remember_optout', 'value' : '0'},
{'name' : 'pl_auth', 'value' : 'a4194bdb3f70:21e4b391789d0cbc408cbc7f7d96055352862a68d633c67fb042fb0be8104d6e'},
{'name' : 'PHPSESSID', 'value' : 'n92foeajau1a52njm8ibgsaef0m1hqdp00099icmc4130dqv'},
{'name' : 'ref', 'value' : 'start'},
{'name' : 'cid', 'value' : '1486828514'}]
def scripto():
    def send_attack():
        try:
            id_record = row[0]
            parametr1 = row[1]
            parametr2 = row[2]
            attacktype = row[4]
            url = row[5]
            massorsingle = row[6]
            print("[LAUNCHING AN ATTACK]: ", row[0], row[1], row[2], row[4], row[5], row[6])
            data = date_str
            dt = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')

            options = Options()
            #options.add_argument('--user-data-dir=/path/to/user-data')
            #options.add_argument('--profile-directory=Default')
            options.add_argument("--start-minimized")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537")
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')


            driver = webdriver.Chrome(options=options)
            godzina = dt.hour
            minuta = dt.minute
            sekunda = dt.second
            ms = dt.microsecond / 1000
            ms2 = str(ms)
            godzina2 = str(godzina)
            minuta2 = str(minuta)

            if godzina < 10:
                godzina2 = str(0) + str(godzina)
            else:
                godzina2 = str(godzina)


            if sekunda < 10:
                sekunda2 = str(0) + str(sekunda)
            else:
                sekunda2 = str(sekunda)

            if minuta < 10:
                minuta2 = str(0) + str(minuta2)
            else:
                minuta2 = str(minuta)

            driver.implicitly_wait(1)  # sekundy
            if massorsingle == "1":
                driver.implicitly_wait(1)  # sekundy
                driver.get("https://plemiona.pl")

                driver.implicitly_wait(1)  # sekundy
                for cookie in cookies:
                    driver.add_cookie(cookie)
                    print(cookie)
                print("print przeszly cookie")
                driver.refresh()
                print("Po refreshu")
                time.sleep(1)
                print("Po refreshu2")
                driver.get(url)

                try:
                    challenge_container = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//span[text()='Świat 182']")))

                    challenge_container.click()
                    driver.get(url)

                except:
                    return False, "E.04 - Nie znaleziono swiata 182",0,"Brak"

                try:
                    challenge_container = driver.find_element(By.CLASS_NAME, "challenge-container")
                    return False, "E.01 - Znaleziono captcha",0,"Brak"
                except:
                    pass

                try:
                    iframe = driver.find_element(By.XPATH, "//iframe[@title='Main content of the hCaptcha challenge']")
                    return False, "E.02 - Znaleziono captcha",0,"Brak"
                except Exception as e:
                    pass


            else:
                driver.implicitly_wait(1)  # sekundy
                driver.get("https://plemiona.pl")

                driver.implicitly_wait(1)  # sekundy
                for cookie in cookies:
                    driver.add_cookie(cookie)
                    print(cookie)
                print("print przeszly cookie")
                driver.refresh()
                print("Po refreshu")
                time.sleep(1)
                print("Po refreshu2")


                try:
                    challenge_container = driver.find_element(By.CLASS_NAME, "challenge-container")
                    print("test1")

                    return False, "E.01 - Znaleziono captcha",0,"Brak"
                except:
                    print("test1")

                    pass

                try:
                    iframe = driver.find_element(By.XPATH, "//iframe[@title='Main content of the hCaptcha challenge']")
                    print("test2")
                    return False, "E.02 - Znaleziono captcha",0,"Brak"
                except Exception as e:
                    print("test2")

                    pass

                try:
                    logout_link = driver.find_element(By.XPATH, "//a[@href='/page/logout']")
                    print("test5")

                except:
                    print("test3")
                    return False, "E.03 - Wylogowano ze strony",0,"Brak"

                try:
                    print("test6")
                    time.sleep(1)
                    print("test7")
                    elements = driver.find_elements(By.CLASS_NAME, "world_button_active")
                    if elements:
                        first_element = elements[0]
                        print("test8")
                        first_element.click()
                    else:
                        print("Nie znaleziono elementu o podanej klasie.")
                    time.sleep(1)
                    print("test9")
                    print("Clicking 182")
                except Exception as e:
                    print(e)
                    print("test4")
                    return False, "E.04 - Nie znaleziono swiata 182",0,"Brak"

                try:
                    challenge_container = driver.find_element(By.CLASS_NAME, "popup_box_close")
                    challenge_container.click()
                except:
                    pass

                try:

                    element = driver.find_element(By.XPATH, '//a[contains(text(), "Kombinowany ")]')
                    element.click()
                    print("test1")
                    driver.implicitly_wait(1)  # sekundy

                except:
                    pass

                try:
                    element = driver.find_element(By.CLASS_NAME, "group-menu-item")
                    element.click()
                    driver.implicitly_wait(1)  # sekundy
                    print("test2")

                except:
                    pass

                current_url = driver.current_url

                response = requests.get(current_url)

                if response.status_code == 200:
                    html_content = response.text

                # Pobierz kod źródłowy strony
                html_content = driver.page_source

                # Przetwarzanie kodu HTML za pomocą BeautifulSoup
                soup = BeautifulSoup(html_content, "html.parser")
                try:
                    print("test3")

                    villages = soup.find_all("tr", class_="nowrap")
                    for village in villages:
                        # Pobieranie identyfikatora wioski
                        village_id = village.find("span", class_="quickedit-vn")["data-id"]

                        # Pobieranie koordynatów wioski
                        village_coordinates_raw = village.find("span", class_="quickedit-label").text
                        village_coordinates = village_coordinates_raw.split('(')[1].split(')')[0]

                        if village_coordinates == parametr1:
                            driver.get("https://pl182.plemiona.pl/game.php?village=" + village_id + "&screen=place")
                            break
                    else:
                        return False, "E.07 - Nie znaleziono wioski atakującego o podanych koordynatach",0,"Brak"
                except:
                    return False, "E.07 - Błąd pobierania id wiosek",0,"Brak"




            if attacktype == "OFF":
                try:
                    units = collect_and_assign_units(driver)
                except:
                    return False, "E.08 - Błąd pobierania aktualnych jednostek",0,"Brak"
                try:
                    attack_units = off_units(driver, units)
                    print("OFF UNITS: ", attack_units)
                except:
                    return False, "E.09 - Błąd podczas generowania offowych jednostek",0,"Brak"
                try:
                    enter_units(driver, attack_units)
                    size = calculate_total(attack_units)
                except:
                    return False, "E.09 - Błąd podczas wpisywania offowych jednostek",0,"Brak"
                driver.implicitly_wait(1)  # sekundy




            elif attacktype == "FAKE":
                try:
                    try:
                        driver.implicitly_wait(1)  # sekundy
                        challenge_container = driver.find_element(By.CLASS_NAME, "village-delete")
                    except NoSuchElementException:
                        # czynności do wykonania, gdy element nie zostanie znaleziony
                        driver.implicitly_wait(1)  # sekundy
                        challenge_container = driver.find_element(By.CLASS_NAME, "target-input-field")
                        challenge_container.clear()
                        slow_type(challenge_container, parametr2, delay=0.1)
                        driver.implicitly_wait(1)  # sekundy
                        print("test5")

                    units = collect_and_assign_units(driver)
                    if units['spear'] > 0:
                        pik = driver.find_element(By.ID, "unit_input_spear")
                        slow_type(pik, "1", delay=0.2)
                    elif units['axe'] > 0:
                        top = driver.find_element(By.ID, "unit_input_axe")
                        slow_type(top, "1", delay=0.2)
                    if units['ram'] < 1 and units['catapult'] < 1:
                        return False, "E.10a - Brak maszyn do wysłania fake", 0, "Brak"

                    #challenge_container = driver.find_element(By.CLASS_NAME, "target-input-field")
                    #challenge_container.clear()
                    #driver.implicitly_wait(1)  # sekundy
                    #slow_type(challenge_container, parametr2, delay=0.2)
                    #driver.implicitly_wait(1)  # sekundy
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "target_attack")))
                    driver.execute_script("arguments[0].click();", element)
                    text = driver.find_element(By.CLASS_NAME, "error_box").text
                    match = re.search(r'co najmniej (\d+) mieszka', text)
                    if match:
                        min_population = int(match.group(1))
                        print(f'Minimalna liczba mieszkańców: {min_population}')
                        capacity = min_population
                        print("Units",units)
                        time.sleep(1)
                        attack_units = fake_units(units, capacity)
                        print("FAKE UNITS: ", attack_units)
                        size = calculate_total(attack_units)
                        enter_units(driver, attack_units)
                except:
                    return False, "E.10b - Błąd podczas uzywania skryptu fake",0,"Brak"




            elif attacktype[:6] == "BURZAK":
                try:
                    parts = attacktype.split(' - ')
                    number = int(parts[1])
                    building = parts[2]
                    building = building.strip()
                    attack_units = burzak_units(driver, number)
                    print("BURZAK UNITS:", attack_units)
                    enter_units(driver, attack_units)
                    size = calculate_total(attack_units)
                except:
                    return False, "E.16 - Błąd podczas burzaka",0,"Brak"





            elif attacktype == "FAKE SZLACHCIC":
                try:
                    units = collect_and_assign_units(driver)
                    attack_units = fake_grubas_units(driver, units)
                    enter_units(driver, attack_units)
                    print("FAKE GRUBAS UNITS:", attack_units)
                    size = calculate_total(attack_units)
                except:
                    return False, "E.14 - Błąd podczas FAKE SZLACHCICA",0,"Brak"





            elif attacktype == "SZLACHCIC":
                try:
                    return False, "E.15 - SZLACHCIC",0,"Brak"
                except:
                    pass
            driver.implicitly_wait(1)  # sekundy



            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "target_attack")))
                driver.execute_script("arguments[0].click();", element)

            except:
                return False, "E.12 - Błąd jeszcze na placu",0,"Brak"

            try:
                challenge_container = driver.find_element(By.ID, "troop_confirm_submit")
            except:
                return False, "E.13 - Błędny cel lub jednostki",0,"Brak"

            try:
                challenge_container = driver.find_element(By.NAME, "building")
                select = Select(challenge_container)
                select.select_by_visible_text(building)
            except:
                pass

            driver.implicitly_wait(1)  # sekundy
            target_time = f"{godzina2}:{minuta2}:{sekunda2}"
            delayTime = 0  # Inicjalizacja delayTime na zero, jak w JavaScript

            try:
                while True:  # Pętla nieskończona, jak w setInterval w JavaScript
                    serverTime_element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.ID, "serverTime"))
                    )
                    serverTime = serverTime_element.text
                    if serverTime >= target_time:
                        print("Powinno sie wysylac")
                        # Rozpocznij odliczanie, a następnie kliknij przycisk, podobnie jak w JavaScript
                        time.sleep((delayTime + ms)/1000)  # delayTime + ms2, konwersja ms2 na sekundy
                        element = driver.find_element(By.ID, 'troop_confirm_submit')
                        driver.execute_script("arguments[0].click();", element)

                        break  # Przerwij pętlę po kliknięciu przycisku

                    time.sleep(1)  # Odczekaj 5 ms, podobnie jak w JavaScript
            except Exception as e:
                print(f"Exception occurred: {e}")
                return False,"GÓWNO",0,"Brak"

            driver.implicitly_wait(1)  # sekundy

            if sekunda < 55:
                sekunda += 5
            else:
                sekunda = (sekunda + 5) % 60
                if minuta < 59:
                    minuta += 1
                else:
                    minuta = 0
                    godzina = (godzina + 1) % 24

            wait_until(godzina, minuta, sekunda)

            try:
                challenge_container = driver.find_element(By.CLASS_NAME, "command-cancel")
                conn = sqlite3.connect('data.db')
                c = conn.cursor()
                c.execute("DELETE FROM data WHERE id = ?", (id_record,))
                conn.commit()

                driver.quit()
                return True, "Success", attack_units, size

            except:
                return False, "E.19 - Błąd skryptu wysyłającego atak",0,"Brak"


        except Exception as e:
            return False, str(e),0,"Brak"

    znaleziono_date = False
    while not znaleziono_date:

        if app.is_stopping:  # Jeśli skrypt jest wyłączony, zakończ
            print("[STOPPED]")
            app.script_enabled = False
            return False, "Skrypt zatrzymany"
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT * FROM data')
        rows = c.fetchall()

        for row in rows:
            date_str = row[3]  # Pobierz datę z kolumny parametr3
            date_obj = parse(date_str)  # Konwertuj ciąg znaków na obiekt datetime

            now = datetime.now()  # Pobierz aktualny czas
            time_diff = date_obj - now  # Oblicz różnicę czasu
            id_record = row[0]
            parametr1 = row[1]
            parametr2 = row[2]
            attacktype = row[4]
            url = row[5]
            massorsingle = row[6]

            data = date_str
            dt = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
            X = parametr1
            Y = parametr2
            godzina = dt.hour
            minuta = dt.minute
            sekunda = dt.second
            ms = dt.microsecond / 1000
            ms2 = str(ms)
            godzina2 = str(godzina)
            minuta2 = str(minuta)

            if sekunda < 10:
                sekunda2 = str(0) + str(sekunda)
            else:
                sekunda2 = str(sekunda)

            if minuta < 10:
                minuta2 = str(0) + str(minuta2)
            else:
                minuta2 = str(minuta)

            if timedelta(minutes=0) < time_diff <= timedelta(minutes=1):  # Sprawdź, czy do daty brakuje 2 minut
                if len(rows) == 1:
                    znaleziono_date = True

                is_successful, message, attack_units, size = send_attack()
                # Sprawdź wynik
                if is_successful:
                    print("Wysłano atak pomyślnie!")
                    # Dodaj informacje o ataku do tabeli 'wyslane'
                    conn = sqlite3.connect('data.db')
                    c = conn.cursor()
                    attack_units_json = json.dumps(attack_units)

                    c.execute(
                        "INSERT INTO wyslane(parametr1, parametr2, data, attacktype,size, units) VALUES (?, ?, ?, ?,?,?)",
                        (parametr1, parametr2, data, attacktype, size, attack_units_json))
                    conn.commit()
                else:
                    print("Nie udało się wysłać ataku. Powód:", message)
                    # Dodaj informacje o ataku do tabeli 'niewyslane'
                    conn = sqlite3.connect('data.db')
                    c = conn.cursor()
                    c.execute(
                        "INSERT INTO niewyslane(parametr1, parametr2, data, attacktype, reason, url, massorsingle) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (parametr1, parametr2, data, attacktype, message, url, massorsingle))
                    print("URL:", url)
                    c.execute("DELETE FROM data WHERE id = ?", (id_record,))
                    conn.commit()

        conn.close()
        if not znaleziono_date:
            time.sleep(10)  # Poczekaj 10s przed kolejnym sprawdzeniem

    return True, "Zakończono działanie programu."

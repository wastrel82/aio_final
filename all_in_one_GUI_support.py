import tkinter as tk
import tkinter.ttk as ttk
import csv
import os
import re
import time
import sys
import pandas as pd
import glob
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from pathlib import Path
import lxml
import openpyxl
import io
from contextlib import redirect_stdout
import requests
import webbrowser
import threading
import functools
import subprocess


py3 = True


def set_Tk_var():
    global input_i
    input_i = tk.StringVar()
    global replacements_price
    replacements_price = {"₽": "", ",": ".", " ": "", "о": "", "т": ""}
    global replacements
    replacements = {'"': "", "|": "", "₽": "", ",": "", "!": "", "@": "", "#": "", "$": "",
                    "%": "", "^": "", "&": "", "*": "", "(": "", ")": "", "_": " ", "?": ""}

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def work(i, work_dir):
    try:
        thr1=threading.Thread(target=autoeuro, args=(i, work_dir))
        thr1.start()
    except Exception:
        # print('Ошибка при работк с autoeuro.ru')
        pass
    try:
        thr2=threading.Thread(target=autopiter, args=(i, work_dir))
        thr2.start()
    except Exception:
        # print('Ошибка при работк с autopiter.ru')
        pass
    try:
        thr3=threading.Thread(target=autorus, args=(i, work_dir))
        thr3.start()
    except Exception:
        # print('Ошибка при работк с autorus.ru')
        pass
    try:
        thr4=threading.Thread(target=ixora_auto, args=(i, work_dir))
        thr4.start()
    except Exception:
        # print('Ошибка при работк с ixora_auto.ru')
        pass
    try:
        thr5=threading.Thread(target=pasker, args=(i, work_dir))
        thr5.start()
    except Exception:
        # print('Ошибка при работк с pasker.ru')
        pass
    try:
        thr6=threading.Thread(target=rossko, args=(i, work_dir))
        thr6.start()
    except Exception:
        # print('Ошибка при работк с rossko.ru')
        pass

    thr1.join()
    thr2.join()
    thr3.join()
    thr4.join()
    thr5.join()
    thr6.join()

def progress_bar():
    w.TProgressbar1 = ttk.Progressbar(root)
    w.TProgressbar1.place(relx=0.305, rely=0.06, relwidth=0.299, relheight=0.0, height=22)
    w.TProgressbar1.configure(length="334")
    w.TProgressbar1.configure(mode="indeterminate")
    w.TProgressbar1.configure(orient="horizontal")
    w.TProgressbar1.start()

def main():
    if hasattr(sys, "_MEIPASS"):
        work_dir = sys._MEIPASS
    else:
        work_dir = os.getcwd()
    i = input_i.get()
    
    start_time = time.time()
    w.Scrolledtreeview1.delete(*w.Scrolledtreeview1.get_children())
    csv_delete(work_dir)
    t2=threading.Thread(target=progress_bar)
    t2.start()
    t1=threading.Thread(target=work, args=(i, work_dir))
    t1.start()
    t1.join()
    print_csv(work_dir)

    finish_time = time.time() - start_time

    file = io.StringIO()
    with redirect_stdout(file):
        try:
            print(f"Время затраченное на autoeuro.ru : {autoeuro_finish}")
        except Exception:
            print('Ошибка при работе с autoeuro.ru')
            pass
        try:
            print(f"Время затраченное на autopiter.ru : {autopiter_finish}")
        except Exception:
            print('Ошибка при работе с autopiter.ru')
            pass
        try:
            print(f"Время затраченное на autorus.ru : {autorus_finish}")
        except Exception:
            print('Ошибка при работе с autorus.ru')
            pass
        try:
            print(f"Время затраченное на ixora_auto.ru : {ixora_auto_finish}")
        except Exception:
            print('Ошибка при работе с ixora_auto.ru')
            pass
        try:
            print(f"Время затраченное на pasker.ru : {pasker_finish}")
        except Exception:
            print('Ошибка при работе с pasker.ru')
            pass
        try:        
            print(f"Время затраченное на rossko.ru : {rossko_finish}")
        except Exception:
            print('Ошибка при работе с rossko.ru')
            pass
    output = file.getvalue()
    w.Label1 = tk.Label(root)
    w.Label1.place(relx=0.636, rely=0.015, height=100, width=384)
    # w.Label1.place(relx=0.502, rely=0.015, height=112, width=534)
    w.Label1.configure(activebackground="#f9f9f9")
    w.Label1.configure(activeforeground="black")
    w.Label1.configure(background="#d9d9d9")
    w.Label1.configure(disabledforeground="#a3a3a3")
    w.Label1.configure(foreground="#000000")
    w.Label1.configure(highlightbackground="#d9d9d9")
    w.Label1.configure(highlightcolor="black")
    w.Label1.configure(text=str(output))
    
    file = io.StringIO()
    with redirect_stdout(file):
        try:
            print(f"Всего времени прошло : {finish_time}")
        except Exception:
            pass
    output1 = file.getvalue()
    w.Label2 = tk.Label(root)
    w.Label2.place(relx=0.305, rely=0.0, height=31, width=333)
    w.Label2.configure(activebackground="#f9f9f9")
    w.Label2.configure(activeforeground="black")
    w.Label2.configure(background="#d9d9d9")
    w.Label2.configure(disabledforeground="#a3a3a3")
    w.Label2.configure(foreground="#000000")
    w.Label2.configure(highlightbackground="#d9d9d9")
    w.Label2.configure(highlightcolor="black")
    w.Label2.configure(text=str(output1))

    w.TProgressbar1.stop()
    sys.stdout.flush()

def csv_delete(work_dir):
    files_csv = glob.glob(os.path.normpath(
        os.path.join(work_dir, "geckodriver/*.csv")))
    for f in files_csv:
        os.remove(f)

def print_csv(work_dir):
    if len(os.listdir(os.path.normpath(os.path.join(work_dir, "geckodriver/")))) > 1:
        data_dir = Path(os.path.normpath(
            os.path.join(work_dir, "geckodriver")))

        df = pd.concat([pd.read_csv(f)
                        for f in data_dir.glob("*.csv")], ignore_index=True)
        df.to_csv(os.path.normpath(os.path.join(
            work_dir, "geckodriver/result.csv")), index=False)

        read_file = pd.read_csv(os.path.normpath(
            os.path.join(work_dir, "geckodriver/result.csv")))
        if getattr(sys, 'frozen', False):
            read_file.to_excel(os.path.normpath(os.path.join(
                os.path.dirname(sys.executable), "result.xlsx")), index=None, header=True)
        else:
            read_file.to_excel(os.path.normpath(os.path.join(
                work_dir, "result.xlsx")), index=None, header=True)

        with open(os.path.normpath(os.path.join(work_dir, "geckodriver/result.csv")), encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                link_xlsx = row['0']
                artikul = row['1']
                price = row['2']
                brend = row['3']
                nazvanie = row['4']
                w.Scrolledtreeview1.insert("", 0, values=(
                    link_xlsx, artikul, price, brend, nazvanie))

    else:
        pass

def autoeuro(i, work_dir):
    autoeuro_start = time.time()
    print_dic = []
    new_print_dic = []
    my_links = []
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }

    url = f"https://shop.autoeuro.ru/main/search?text={i}&whs=&crosses=0&crosses=1"

    req = requests.get(url, headers=headers)
    src = req.text

    with open(os.path.normpath(os.path.join(work_dir, "geckodriver/index.html")), "w") as file:
        file.write(src)

    with open(os.path.normpath(os.path.join(work_dir, "geckodriver/index.html")), "r") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    links = soup.find_all("span", class_="a_button go_search")
    for link in links:
        data = link.get("data-href")
        data = "https://shop.autoeuro.ru" + data
        my_links.append(data)
    for i in my_links:
        url = i

        req = requests.get(url=url, headers=headers)
        src = req.text

        with open(os.path.normpath(os.path.join(work_dir, "geckodriver/index.html")), "w") as file:
            file.write(src)

        with open(os.path.normpath(os.path.join(work_dir, "geckodriver/index.html"))) as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        links = soup.find_all(class_=re.compile(
            "search_maker_block proposals"))
        for item in links:
            try:
                price = item.find(id=re.compile(
                    'stat_best_')).text.replace(u"\xa0", u"").strip()
                price = "".join([replacements_price.get(c, c) for c in price])
                price = price.split(".")[0]
            except Exception:
                price = "нет в продаже"
                # continue
            try:
                brend = item.find(class_=re.compile(
                    'producer-info-link ajax-link')).text.strip()
                brend = "".join([replacements.get(c, c) for c in brend])
            except Exception:
                brend = "нет бренда"
            try:
                artikul = item.find("a", class_="code_link").text.strip()
                artikul = "".join([replacements.get(c, c) for c in artikul])
            except Exception:
                artikul = "нет артикула"
            try:
                link = url
                # link = "https://nov.rossko.ru" + item.get("href").strip()
            except Exception:
                link = "нет ссылки"
            try:
                nazvanie = item.find("h2").text.strip()
                nazvanie = "".join([replacements.get(c, c) for c in nazvanie])
            except Exception:
                nazvanie = "нет описания"
            try:
                link_xlsx = "autoeuro.ru"
                # link_xlsx = '<a href=' + '"' + link + '"' + '>' + link_xlsx + '</a>'
            except Exception:
                link_xlsx = "autoeuro.ru"

            new_print_dic.append(
                [link_xlsx, artikul, price, brend, nazvanie, link])
            for element in new_print_dic:
                if not element in print_dic:
                    print_dic.append(element)

    df = pd.DataFrame(print_dic)
    if df.empty == True:
        pass
    else:
        df.to_csv(os.path.normpath(os.path.join(
            work_dir, "geckodriver/autoeuro.csv")), index=False)

    files_html = glob.glob(os.path.normpath(
        os.path.join(work_dir, "geckodriver/*.html")))
    for f in files_html:
        os.remove(f)
    
    global autoeuro_finish
    autoeuro_finish = time.time() - autoeuro_start

def autopiter(i, work_dir):
    autopiter_start = time.time()
    
    flag = 0x08000000  # No-Window flag
    webdriver.common.service.subprocess.Popen = functools.partial(
        subprocess.Popen, creationflags=flag)    
    
    print_dic = []
    firefox_driver_path = os.path.normpath(
        os.path.join(work_dir, "geckodriver/geckodriver.exe"))

    service = FirefoxService(
        executable_path=firefox_driver_path, log_path=os.path.devnull)
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0")

    url = f"https://autopiter.ru/goods/{i}"

    driver = webdriver.Firefox(options=options, service=service)

    driver.get(url=url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "lxml")
    cards = soup.find_all(class_=re.compile(
        'IndividualTableRow__row___'))
    for item in cards:
        try:
            price = item.find(class_=re.compile(
                'IndividualTableRow__originalPriceWrapper___')).text.replace("от", "").replace(u"\xa0", u"").strip()
            price = "".join([replacements_price.get(c, c) for c in price])
            price = price.split(".")[0]
        except Exception:
            # price = "нет в продаже"
            continue
        try:
            brend = item.find(class_=re.compile(
                'IndividualTableRow__infoColumn___')).text.strip()
            brend = "".join([replacements.get(c, c) for c in brend])
        except Exception:
            brend = "нет бренда"
        try:
            artikul = item.find(class_=re.compile(
                'IndividualTableRow__numberLink___1-eq1 common__link___')).text.strip()
            artikul = "".join([replacements.get(c, c) for c in artikul])
        except Exception:
            artikul = "нет артикула"
        try:
            # link = "https://autopiter.ru/"
            link = "https://autopiter.ru" + item.find(class_=re.compile(
                'IndividualTableRow__numberLink___1-eq1 common__link___')).get("href").strip()
        except Exception:
            link = "нет ссылки"
        try:
            nazvanie = item.find(class_=re.compile(
                'IndividualTableRow__descriptionColumn___')).text.strip()
            nazvanie = "".join([replacements.get(c, c) for c in nazvanie])
        except Exception:
            nazvanie = "нет описания"
        link_xlsx = "autopiter.ru"
        # link_xlsx = '<a href=' + '"' + link + '"' + '>' + link_xlsx + '</a>'
        print_dic.append([link_xlsx, artikul, price, brend, nazvanie, link])

    driver.close()
    driver.quit()

    df = pd.DataFrame(print_dic)
    if df.empty == True:
        pass
    else:
        df.to_csv(os.path.normpath(os.path.join(
            work_dir, "geckodriver/autopiter.csv")), index=False)

    global autopiter_finish
    autopiter_finish = time.time() - autopiter_start

def autorus(i, work_dir):
    start_time = time.time()
    id = []
    print_dic = []
    url = "https://www.autorus.ru"
    response = requests.get(url)
    test = response.headers.get("Set-Cookie")
    id.append(response.headers.get("Set-Cookie"))
    cookies = test.split(";")[0]

    headers = {"Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Cookie": "sess-id=s%3AJxnqaPIecDkmcIE95_VFoanhqIqSMX4i.LDetic55ayovLpJ2VyRV%2Fv7RolrRv%2F3QkGZA62JbyHA; _userGUID=0:kw555gqe:G6dRLDBckmxjJG3QvQZl5FAwmpdig6MR; dSesn=18dceeca-11bf-af5b-ec07-d78d78e93a52; _dvs=0:kw6vivsd:Ro24_A~MQLjRgQ8hkYl4TZ7EvLyid~de",
            "DNT": "1", 
            "Host": "www.autorus.ru",
            "Referer": "https://www.autorus.ru/search?q=mts%200374",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "X-metaUrl": "/search?q=mts 0374",
            "X-Referer": "/search"}


    headers["Cookie"] = cookies
    ref = f"https://www.autorus.ru/search?q={i}"
    metaUrl = f"/search?q={i}"
    headers["Referer"] = ref
    headers["X-metaUrl"] = metaUrl

    try:
        new_url = f"https://www.autorus.ru/api/search_by_article?article={i}"
        response = requests.get(url=new_url, headers=headers)
        src = response.json()
        for i in src:
            for item in i.get('analog'):
                try:
                    price = str(item['minPrice'])
                    # price = price.split("\xa0")[0]
                    # price = re.sub("[о|т|А|₽|?], "", price)
                    price = "".join([replacements_price.get(c, c) for c in price])
                    price = price.split(".")[0]
                except Exception:
                    price = "нет в продаже"
                    # continue
                try:
                    brend = item['brand']
                    brend = "".join([replacements.get(c, c) for c in brend])
                except Exception:
                    brend = "нет бренда"
                try:
                    artikul = item['article']
                    artikul = "".join([replacements.get(c, c) for c in artikul])
                except Exception:
                    artikul = "нет артикула"
                try:
                    link = new_url
                    # link = "https://www.autorus.ru" + item.get("href").strip()
                except Exception:
                    link = "нет ссылки"
                try:
                    nazvanie = item['title']
                    nazvanie = "".join([replacements.get(c, c) for c in nazvanie])
                except Exception:
                    nazvanie = "нет описания"
                try:
                    link_xlsx = "autorus.ru"
                    # link_xlsx = '<a href=' + '"' + link + '"' + '>' + link_xlsx + '</a>'
                except Exception:
                    link_xlsx = "autorus.ru"

                print_dic.append([link_xlsx, artikul, price, brend, nazvanie, link])
            for item in i.get('sought'):
                try:
                    price = str(item['minPrice'])
                    # price = price.split("\xa0")[0]
                    # price = re.sub("[о|т|А|₽|?], "", price)
                    price = "".join([replacements_price.get(c, c) for c in price])
                    price = price.split(".")[0]
                except Exception:
                    price = "нет в продаже"
                    # continue
                try:
                    brend = item['brand']
                    brend = "".join([replacements.get(c, c) for c in brend])
                except Exception:
                    brend = "нет бренда"
                try:
                    artikul = item['article']
                    artikul = "".join([replacements.get(c, c) for c in artikul])
                except Exception:
                    artikul = "нет артикула"
                try:
                    link = new_url
                    # link = "https://www.autorus.ru" + item.get("href").strip()
                except Exception:
                    link = "нет ссылки"
                try:
                    nazvanie = item['title']
                    nazvanie = "".join([replacements.get(c, c) for c in nazvanie])
                except Exception:
                    nazvanie = "нет описания"
                try:
                    link_xlsx = "autorus.ru"
                    # link_xlsx = '<a href=' + '"' + link + '"' + '>' + link_xlsx + '</a>'
                except Exception:
                    link_xlsx = "autorus.ru"

                print_dic.append([link_xlsx, artikul, price, brend, nazvanie, link])
    except Exception:
        pass
    df = pd.DataFrame(print_dic)

    if df.empty == True:
        pass
    else:
        df.to_csv(os.path.normpath(os.path.join(
            work_dir, "geckodriver/autorus.csv")), index=False)

    global autorus_finish
    autorus_finish = time.time() - start_time

def ixora_auto(i, work_dir):
    start_time = time.time()

    flag = 0x08000000  # No-Window flag
    webdriver.common.service.subprocess.Popen = functools.partial(
        subprocess.Popen, creationflags=flag)
    
    print_dic = []

    firefox_driver_path = os.path.normpath(
        os.path.join(work_dir, "geckodriver/geckodriver.exe"))

    service = FirefoxService(
        executable_path=firefox_driver_path, log_path=os.path.devnull)
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0")

    url = f"https://ixora-auto.ru/catalog-article?article={i}"
    driver = webdriver.Firefox(options=options, service=service)

    driver.get(url=url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "lxml")
    cards = soup.find_all("div", class_='sku__content')
    for item in cards:
        try:
            price = item.find(
                "span", class_="sku__text sku__text--price").text.replace(u"\xa0", u"").replace('от', '').strip()
            # price = price.split("\xa0")[0]
            # price = re.sub("[о|т|А|₽|?], "", price)
            price = "".join([replacements_price.get(c, c) for c in price])
            price = price.split(".")[0]
        except Exception:
            price = "нет в продаже"
            # continue
        try:
            brend = item.find("span", class_="sku__title-brand").text.strip()
            brend = "".join([replacements.get(c, c) for c in brend])
        except Exception:
            brend = "нет бренда"
        try:
            artikul = item.find("h3", class_="sku__title").text.strip()
            artikul = "".join([replacements.get(c, c) for c in artikul])
            artikul = artikul.replace(" ", "")
            artikul = artikul.split('\n')
            artikul = " ".join(artikul)
            artikul = artikul.replace("  ", " ")
            artikul = artikul.replace(" ", ":")
            # GAZ\n\n4061006100\nНатяжительцепи
            artikul = artikul.split(":")[1]
            artikul = artikul.split(":")[0]
            # print(artikul)
            # artikul = "".join(artikul.split())
        except Exception:
            artikul = "нет артикула"
        try:
            link = url
            # link = "https://www.autorus.ru" + item.get("href").strip()
        except Exception:
            link = "нет ссылки"
        try:
            nazvanie = item.find(
                "span", class_="sku__detail-name").text.strip()
            nazvanie = "".join([replacements.get(c, c) for c in nazvanie])
        except Exception:
            nazvanie = "нет описания"
        try:
            link_xlsx = "ixora-auto.ru"
            # link_xlsx = '<a href=' + '"' + link + '"' + '>' + link_xlsx + '</a>'
        except Exception:
            link_xlsx = "ixora-auto.ru"

        print_dic.append([link_xlsx, artikul, price, brend, nazvanie, link])

    driver.close()
    driver.quit()

    df = pd.DataFrame(print_dic)
    if df.empty == True:
        pass
    else:
        df.to_csv(os.path.normpath(os.path.join(
            work_dir, "geckodriver/ixora_auto.csv")), index=False)

    global ixora_auto_finish
    ixora_auto_finish = time.time() - start_time

def pasker(i, work_dir):
    pasker_time = time.time()
    
    flag = 0x08000000  # No-Window flag
    webdriver.common.service.subprocess.Popen = functools.partial(
        subprocess.Popen, creationflags=flag)
    
    print_dic = []

    firefox_driver_path = os.path.normpath(
        os.path.join(work_dir, "geckodriver/geckodriver.exe"))

    service = FirefoxService(
        executable_path=firefox_driver_path, log_path=os.path.devnull)
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0")

    url = f"https://pasker.ru/search?x=0&y=0&filter={i}&cod="
    driver = webdriver.Firefox(options=options, service=service)

    driver.get(url=url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "lxml")
    cards = soup.find_all(class_=re.compile(
        'product-grid-item-wrap no-product-add-to-cart'))
    for item in cards:
        try:
            price = item.find("div", class_="markup").text.strip()
            # price = price.split("\xa0")[0]
            # price = re.sub("[о|т|А|₽|?], "", price)
            price = "".join([replacements_price.get(c, c) for c in price])
            price = price.split(".")[0]
        except Exception:
            price = "нет в продаже"
            # continue
        try:
            brend = item.find(
                "span", class_="field-content").find("a").text.strip()
            brend = "".join([replacements.get(c, c) for c in brend])
        except Exception:
            brend = "нет бренда"
        try:
            artikul = item.find("div", class_="article").find("a").text.strip()
            artikul = "".join([replacements.get(c, c) for c in artikul])
        except Exception:
            artikul = "нет артикула"
        try:
            link = url
            # link = "https://www.autorus.ru" + item.get("href").strip()
        except Exception:
            link = "нет ссылки"
        try:
            nazvanie = item.find(
                "div", class_="product-grid-title box").text.strip()
            nazvanie = "".join([replacements.get(c, c) for c in nazvanie])
        except Exception:
            nazvanie = "нет описания"
        try:
            link_xlsx = "pasker.ru"
            # link_xlsx = '<a href=' + '"' + link + '"' + '>' + link_xlsx + '</a>'
        except Exception:
            link_xlsx = "pasker.ru"

        print_dic.append([link_xlsx, artikul, price, brend, nazvanie, link])

    driver.close()
    driver.quit()

    df = pd.DataFrame(print_dic)
    if df.empty == True:
        pass
    else:
        df.to_csv(os.path.normpath(os.path.join(
            work_dir, "geckodriver/pasker.csv")), index=False)

    global pasker_finish
    pasker_finish = time.time() - pasker_time

def rossko(i, work_dir):
    start_time = time.time()
    
    flag = 0x08000000  # No-Window flag
    webdriver.common.service.subprocess.Popen = functools.partial(
        subprocess.Popen, creationflags=flag)
    
    print_dic = []
    firefox_driver_path = os.path.normpath(
        os.path.join(work_dir, "geckodriver/geckodriver.exe"))

    service = FirefoxService(
        executable_path=firefox_driver_path, log_path=os.path.devnull)
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0")

    url = f"https://nov.rossko.ru/search?sid=undefined&q={i}&text={i}&type=all"
    driver = webdriver.Firefox(options=options, service=service)

    driver.get(url=url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "lxml")
    cards = soup.find_all(class_=re.compile(
        'src-features-search-components-result-item-___index__link___'))
    for item in cards:
        try:
            price = item.find(class_=re.compile(
                'src-features-search-components-deliver-___index__price___')).text.replace(u"\xa0", u"").strip()
            price = "".join([replacements_price.get(c, c) for c in price])
            price = price.split(".")[0]
        except Exception:
            # price = "нет в продаже"
            continue
        try:
            brend = item.find(class_=re.compile(
                'src-features-search-components-result-item-___index__brand___')).find("span").text.strip()
            brend = "".join([replacements.get(c, c) for c in brend])
        except Exception:
            brend = "нет бренда"
        try:
            artikul = item.find(class_=re.compile(
                'src-features-search-components-result-item-___index__articleNumbers___')).text.strip()
            artikul = "".join([replacements.get(c, c) for c in artikul])
        except Exception:
            artikul = "нет артикула"
        try:
            # link = "https://nov.rossko.ru/"
            link = "https://nov.rossko.ru" + item.get("href").strip()
        except Exception:
            link = "нет ссылки"
        try:
            nazvanie = item.find(class_=re.compile(
                'src-features-search-components-result-item-___index__article___')).text.strip()
            nazvanie = "".join([replacements.get(c, c) for c in nazvanie])
        except Exception:
            nazvanie = "нет описания"
        try:
            link_xlsx = "rossko.ru"
            # link_xlsx = '<a href=' + '"' + link + '"' + '>' + link_xlsx + '</a>'
        except Exception:
            link_xlsx = "rossko.ru"

        print_dic.append([link_xlsx, artikul, price, brend, nazvanie, link])

    driver.close()
    driver.quit()

    df = pd.DataFrame(print_dic)
    if df.empty == True:
        pass
    else:
        df.to_csv(os.path.normpath(os.path.join(
            work_dir, "geckodriver/rossko.csv")), index=False)

    global rossko_finish
    rossko_finish = time.time() - start_time

def autoeuro_link():
    i = input_i.get()
    webbrowser.open_new(
        f"https://shop.autoeuro.ru/main/search?text={i}&whs=&crosses=0&crosses=1")

def autopiter_link():
    i = input_i.get()
    webbrowser.open_new(f"https://autopiter.ru/goods/{i}")

def autorus_link():
    i = input_i.get()
    webbrowser.open_new(f"https://www.autorus.ru/search?q={i}")

def ixora_auto_link():
    i = input_i.get()
    webbrowser.open_new(f"https://ixora-auto.ru/catalog-article?article={i}")

def pasker_link():
    i = input_i.get()
    webbrowser.open_new(f"https://pasker.ru/search?x=0&y=0&filter={i}&cod=")

def rossko_link():
    i = input_i.get()
    webbrowser.open_new(
        f"https://nov.rossko.ru/search?sid=undefined&q={i}&text={i}&type=all")


if __name__ == '__main__':
    import all_in_one_GUI
    all_in_one_GUI.vp_start_gui()

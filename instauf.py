import json
import os
import sys
import time
from selenium import webdriver
import warnings


class InstagramUnfollower:
    def __init__(self,
                 email: str = None,
                 password: str = None,
                 profile_link: str = None,
                 executable_path: str = None
                 ):

        self._email = None
        self._password = None
        self._profile_link = None
        self._executable_path = None
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        if os.name == 'nt':
            self._pip = "pip"
            self._python, = "python"
            self._clear = "cls"
        else:
            self._pip = "pip3"
            self._python = "python3"
            self._cleartxt = "clear"

    def setEmail(self, email: str = None):
        if email is None:
            self._email = input("[?] Email/Username: ")
        else:
            self._email = email

    def setPassword(self, password: str = None):
        if password is None:
            self._password = input("[?] Password: ")
        else:
            self._password = password

    def setProfileLink(self, profile_link: str = None):
        if profile_link is None:
            self._profile_link = input("[?] Profile Link: ")
        else:
            self._profile_link = profile_link

    def setWebDriver(self, web_driver_path: str = None):
        self._executable_path = web_driver_path

    def pip_install(self, name: str, additional_options: str = "-U"):
        os.system(self._pip + " install " + additional_options + name)

    def clear(self):
        os.system(self._cleartxt)

    def sleep(self, t):
        if isinstance(t, str):
            t = float(t)
        time.sleep(t)

    def loadDict(self, email: str, password: str, profile_link: str):
        self._email = email
        self._password = password
        self._profile_link = profile_link

    def checkFile(self, filename: str = "login.txt"):
        if filename in os.listdir(os.getcwd()):
            return os.path.join(os.getcwd(), filename)
        else:
            return None

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

    def unFollowInstagram(self):
        if self._executable_path is None:
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome(
                executable_path=self._executable_path)

        driver.get("https://www.instagram.com/")

        print("[+] Waiting 5 seconds until instagram home page loads")
        time.sleep(5)

        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self._email)
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self._password)
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()

        print("[+] Waiting 4 seconds until login completes")
        time.sleep(4)

        driver.get(self._profile_link)

        print("[+] Waiting 5 seconds until profile opens")
        time.sleep(5)

        following = driver.find_element_by_partial_link_text("following")
        following.click()

        print("[+] Waiting 5 seconds until 'Following' opens")
        time.sleep(3)

        temp = driver.find_elements_by_tag_name('button')
        print("\n\n")
        count = 1
        for i in temp:
            if str(i.text).strip() == "Following":
                i.click()

                time.sleep(1)

                secondbtn = driver.find_element_by_xpath(
                    '//button[text()="Unfollow"]')
                secondbtn.click()

                print("[" + str(count) + "]" + " : Unfollowed")
                time.sleep(1.5)

            count += 1

    def startUnfollowing(self):
        self.clear()
        filename = self.checkFile()
        if not(filename is None):
            logininfo = self.loadFile()
        else:
            logininfo = None

        if logininfo is None:
            self.setEmail()
            self.setPassword()
            self.setProfileLink()
        else:
            self.loadDict(email=logininfo["email"],
                          password=logininfo["password"],
                          profile_link=logininfo["profile_link"])

        self.unFollowInstagram()


if __name__ == "__main__":
    x = InstagramUnfollower()
    x.startUnfollowing()

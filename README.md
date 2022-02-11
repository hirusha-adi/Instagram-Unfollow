# Instagram-Unfollow

Unfollow the people you follow easily with python and selenium

# Usage

Make sure to have the `webdriver` added to path or copy the `webdriver.exe` to the current folder (current working directory)

For Login Info

1. You can make a text file named `login.txt` and include the email address in the first line, password in the second line and the profile link in the third line

```
youemail@address.com
yourpassword123
https://instagram.com/@yourusername
```

2. You can make a `json` file named `login.json` with a the key names `"email"`, `"password"`, `"profile_link"`

```json
{
  "email": "youemail@address.com",
  "password": "yourpassword123",
  "profile_link": "https://instagram.com/@yourusername"
}
```

## For Users

- Start the script with

```
python instauf.py
```

## For Developers

### Easy Mode

1. Copy the `instauf.py` to the current working directory

```python
from instauf import InstagramUnfollower # 2. Importing the class from `instauf.py`
obj = InstagramUnfollower() # 3. Initializing the imported class
obj.startUnfollowing() # 4. Running a function
```

### Hard Mode

1. Copy the `instauf.py` to the current working directory

```python
# import
from instauf import InstagramUnfollower

obj = InstagramUnfollower()

# Setters for required values
# if no value is passed to these functions,
#   they will ask the user for the value from an `input("...")`
obj.setEmail("value@passed.com")
obj.setPassword()
obj.setProfileLink()

# Start to unfollow
obj.unFollowInstagram()
```

### Extreme Mode

1. Copy the `instauf.py` to the current working directory

```python
from instauf import InstagramUnfollower

obj = InstagramUnfollower()

obj.clear()
filename = obj.checkFile()
if not(filename is None):
    logininfo = obj.loadFile()
else:
    logininfo = None
if logininfo is None:
    obj.setEmail()
    obj.setPassword()
    obj.setProfileLink()
else:
    obj.loadDict(email=logininfo["email"],
                  password=logininfo["password"],
                  profile_link=logininfo["profile_link"])

obj.unFollowInstagram()
```

- or use sys.argv or argparse to even create a nice CLI application

# Installing and Running

## Arch Linux

run the commands below, line by line

```bash
sudo pacman -Syyuu --noconfirm
sudo pacman -S git python python-pip --noconfirm
cd ~
git clone https://github.com/hirusha-adi/Instagram-Unfollow.git
cd Instagram-Unfollow
pip3 install -r requirements.txt
python3 instauf.py
```

## Ubuntu/Debian

run the commands below, line by line

```bash
sudo apt install && sudo apt upgrade -y
sudo apt install git python3 python3-pip -y
cd ~
git clone https://github.com/hirusha-adi/Instagram-Unfollow.git
cd Instagram-Unfollow
pip3 install -r requirements.txt
python3 instauf.py
```

## Windows

1. Download and install Python3. Make sure to 'Add to PATH' when install python3

![image1](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

2. Download the code as a .zip file from [this Github Reposotory](https://github.com/hirusha-adi/Instagram-Unfollow)

![image2](https://cdn.discordapp.com/attachments/935515175073763398/937186561299197952/unknown.png)

(this above image might not be the same)

3. Extract the downloaded `.zip` file
4. open `cmd` in that folder
5. run `pip install -r requirements.txt`
6. run `python instauf.py` to start the program

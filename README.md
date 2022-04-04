PAGE-BRUTE is a python3 brute force tool that is used to brute force most websites

 [x]-> v1.0.5<br>
 [x]-> coded by KTSociety<br>
 [x]-> brute-force-tool for Python 3<br>
 [x]-> code based on the "Hatch" script from METACHAR<br>
 
## Installation Instructions
```
git clone https://github.com/KTSociety/page-brute
```

## Requirements
```
pip3 install selenium
pip3 install requests
```
The chromedriver for Linux and Windows are already included, but if you need an other version of chromedriver you can download it at https://chromedriver.chromium.org/downloads<br> 

## How to use the script with interactive wizard
1). Start the script in terminal with<br>
```
python3 pb-v105.py
```
2). Enter the target website login page url like: https://targetpage.com/login<br>
3). In your Chrome browser inspect the username element to find the CSS-Selector of the Username-Field & copy it into terminal<br>
4). Do the same for the CSS-Selector of the Password-Field<br>
5). And again for the CSS-Selector of the Login-Button<br>
6). When asked put in the targets username you want to brute-force<br>
7). Enter the PATH/NAME of your passwords.txt<br>
8). Watch the magic happen<br>

## Terminal Start-Code to use the script without wizard
```
python3 pb-v105.py --username 'TARGET-USERNAME-HERE' --usernamesel 'USERNAME-CSS-SELECTOR-HERE' --passsel 'PASSWORD-CSS-SELECTOR-HERE' --loginsel 'LOGINBUTTON-CSS-SELECTOR-HERE' --passlist 'passwords.txt' --website 'TARGETPAGE-URL-HERE'
```

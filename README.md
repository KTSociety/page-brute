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
1). Start the script in terminal with: python3 pb-v105.py<br>
2). Enter the target website login page url like: https://yourtargetpage.com/login<br>
3). In your Chrome-Browser inspect the username element to find the CSS-Selector of the username form and enter it in your terminal as asked<br>
4). Do the same for the CSS-Selector of the password field<br>
5). And again for the CSS-Selector of the Login-Button<br>
6). When Asked put in the targets username you wanna brute-force<br>
7). Enter the PATH/NAME of your passwordlist .txt<br>
8). Watch the magic happen<br>

## Terminal Start-Code example
```
python3 pb-v105.py --username 'FILL-IN-TARGET-USERNAME-HERE' --usernamesel 'USER-CSS-SELECTOR-HERE' --passsel 'PASS-CSS-SELECTOR-HERE' --loginsel 'LOGIN-BUTTON-CSS-SELECTOR-HERE' --passlist 'YOUR-PASSLIST-TXT-HERE' --website 'TARGET-PAGE-URL-HERE'
```

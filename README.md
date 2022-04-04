## Installation Instructions
```
git clone https://github.com/ktsociety/page-brute/
```

## Requirements
```
pip3 install selenium
pip3 install requests
```
chrome driver and chrome are also required!
link to chrome driver: http://chromedriver.chromium.org/downloads
copy it to bin!
<br>
## How to use (text)
1). Find a website with a login page<br>
2). Inspect element to find the Selector of the username form<br>
3). Do the same for the password field<br>
4). The the login form <br>
5). When Asked put in the username to brute force<br>
6). Watch it go!

## Startcode example
```
python3 pb-v105.py --username 'FILL-IN-TARGET-USERNAME-HERE' --usernamesel 'USER-CSS-SELECTOR-HERE' --passsel 'PASS-CSS-SELECTOR-HERE' --loginsel 'LOGIN-BUTTON-CSS-SELECTOR-HERE' --passlist 'YOUR-PASSLIST-TXT-HERE' --website 'TARGET-PAGE-URL-HERE'
```

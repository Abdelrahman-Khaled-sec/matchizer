# matchizer
Taken urls and match words => return urls which true or false matched

## why i want matchizer
some times you want gather all [ login pages , admin pages , CMS , password input , any thing in response body ] <br>
matchizer can do this ..

## Installation
```bash
git clone https://github.com/Abdelrahman-Khaled-sec/matchizer.git
pip3 install -r requirements.txt
```

## Examples usage
python3 matchizer.py -urls file_urls.txt -match "login" -include -o results.txt

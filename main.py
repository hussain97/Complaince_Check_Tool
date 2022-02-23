import requests
from bs4 import BeautifulSoup

payload = {'company': 'MICROSOFT CORP'}
r = requests.get('https://www.sec.gov/cgi-bin/cik_lookup', params=payload)
r_Contents = r.text
# Making a request to the SEC gov website to retrieve the CIK codes for the searched company

soup = BeautifulSoup(r_Contents, 'lxml')
Company_CIK_Code_HTML = soup.find('a')
Company_CIK_Code = Company_CIK_Code_HTML.text
print(Company_CIK_Code)
# Extracting the first CIK code from the HTML file

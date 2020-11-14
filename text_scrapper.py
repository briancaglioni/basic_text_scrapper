import httplib2
from bs4 import BeautifulSoup

# asks for a link
link = input()

# retreives the page
http = httplib2.Http()
status, response = http.request(link)

# gets the texts
soup = BeautifulSoup(response,"html.parser" )
text1 = soup.get_text(strip=True)
texts = [text for text in soup.stripped_strings]

# writes to file
f = open("text.txt", "w")
for t in texts:
    f.write(t + '\n')
f.close()
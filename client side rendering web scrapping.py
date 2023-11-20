from requests_html import HTMLSession

url = "https://www.oehv.at/mitglieder/hotelverzeichnis/?filter.sortOrder=ASC&page=1"

s = HTMLSession()
r = s.get(url)
r.html.render(sleep = 90)

# Print the status code and confirmation
print("Status Code:", r.status_code)
print(r.html.html)

with open("scraped_content.txt", "w", encoding="utf-8") as file:
    file.write(r.html.html)
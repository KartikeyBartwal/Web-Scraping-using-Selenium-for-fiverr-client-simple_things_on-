import requests
from bs4 import BeautifulSoup

url = "https://www.oehv.at/mitglieder/hotelverzeichnis/?filter.sortOrder=ASC&page=1"  # Replace with the URL of the webpage containing the hotel information
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Use CSS selectors to find the elements containing hotel information
    hotel_names = soup.select('.hotel-name-class')  # Replace 'hotel-name-class' with the actual class of the hotel name element
    addresses = soup.select('.hotel-address-class')  # Replace 'hotel-address-class' with the actual class of the address element
    emails = soup.select('.hotel-email-class')  # Replace 'hotel-email-class' with the actual class of the email element
    
    # Extract text from the found elements
    hotel_names_text = [name.get_text() for name in hotel_names]
    addresses_text = [address.get_text() for address in addresses]
    emails_text = [email.get_text() for email in emails]
    
    # Print or process the extracted data
    for name, address, email in zip(hotel_names_text, addresses_text, emails_text):
        print(f"Hotel Name: {name}\nAddress: {address}\nEmail: {email}\n")
else:
    print("Failed to retrieve the webpage.")

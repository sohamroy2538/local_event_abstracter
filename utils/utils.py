from bs4 import BeautifulSoup
import requests
import datetime
from langchain_community.document_loaders import WebBaseLoader



def scrape_and_clean(url):
    # Fetch the content of the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the text from the parsed HTML
        text = soup.get_text()
        
        # Optionally, clean up the text further (e.g., remove extra whitespace)
        cleaned_text = ' '.join(text.split())
        
        return cleaned_text
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"
    



def extract_event_info(link : str):
        loader = WebBaseLoader(link)
        scrap_data = scrape_and_clean(loader)

        #scrap_data = loader.load()
        #scrap_data = (scrap_data[0].page_content)

        return scrap_data



def get_days_dates():
    today = datetime.date.today()
    formatted_today = today.strftime("%B %d, %Y")
    day_today = today.strftime("%A")

    tomorrow = today + datetime.timedelta(days=1)
    formatted_tomorrow = tomorrow.strftime("%B %d, %Y")
    day_tomorrow = tomorrow.strftime("%A")

    day_after = today + datetime.timedelta(days=2)
    formatted_dayafter = day_after.strftime("%B %d, %Y")
    day_dayafter = day_after.strftime("%A")

    return formatted_today, day_today , formatted_tomorrow, day_tomorrow , formatted_dayafter ,day_dayafter

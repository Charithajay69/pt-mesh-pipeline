import requests
from bs4 import BeautifulSoup

class TenderScraper:
    def __init__(self, url):
        self.url = url

    def get_tender_details(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")
        tender_details = []

        # Scraping logic specific to each source
        if "ieg.worldbankgroup.org" in self.url:
            tender_elements = soup.find_all("div", class_="tender-details")
            for tender in tender_elements:
                title = tender.find("h2").text
                description = tender.find("p").text
                tender_details.append({"Title": title, "Description": description})

        elif "chinabidding.com" in self.url or "ggzy.gov.cn" in self.url or "mofcom.gov.cn" in self.url:
            tender_elements = soup.find_all("div", class_="tender-details")
            for tender in tender_elements:
                title = tender.find("h2").text
                description = tender.find("p").text
                tender_details.append({"Title": title, "Description": description})

        elif "cpppc.org" in self.url:
            tender_elements = soup.find_all("div", class_="tender-details")
            for tender in tender_elements:
                title = tender.find("h2").text
                description = tender.find("p").text
                tender_details.append({"Title": title, "Description": description})

        elif "etenders.gov.in" in self.url:
            tender_elements = soup.find_all("div", class_="tender-details")
            for tender in tender_elements:
                title = tender.find("h2").text
                description = tender.find("p").text
                tender_details.append({"Title": title, "Description": description})

        return tender_details

if __name__ == "__main__":
    urls = [
        "https://ieg.worldbankgroup.org/data",
        "https://www.chinabidding.com/en",
        "http://www.ggzy.gov.cn/",
        "http://en.chinabidding.mofcom.gov.cn/",
        "https://www.cpppc.org/en/PPPyd.jhtml",
        "https://www.cpppc.org:8082/inforpublic/homepage.html#/searchresult",
        "https://etenders.gov.in/eprocure/app"
    ]

    for url in urls:
        scraper = TenderScraper(url)
        tenders = scraper.get_tender_details()
        print("Tenders from", url)
        for tender in tenders:
            print("Title:", tender["Title"])
            print("Description:", tender["Description"])
            print("=" * 40)

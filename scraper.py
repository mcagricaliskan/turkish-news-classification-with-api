import time
import json
import urllib3
import requests
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
from threading import Thread
from multiprocessing.pool import ThreadPool


urllib3.disable_warnings()


class NewsScraper:
    def __init__(self) -> None:
        # News Categories and their links
        self.WEB_SITE_LINK = "https://www.ensonhaber.com"
        self.NEWS_CATEGORY_LINKS = {
            'Sport': 'https://www.ensonhaber.com/kralspor?infinity=1&sayfa=', # spor is different from others?
            'Daily': 'https://www.ensonhaber.com/gundem?infinity=1&sayfa=',
            'Economy': 'https://www.ensonhaber.com/ekonomi?infinity=1&sayfa=',
            'Magazine': 'https://www.ensonhaber.com/magazin?infinity=1&sayfa=',
            'Automobile': 'https://www.ensonhaber.com/otomobil?infinity=1&sayfa=',
            'Technology': 'https://www.ensonhaber.com/teknoloji?infinity=1&sayfa=',
            'Health': 'https://www.ensonhaber.com/saglik?infinity=1&sayfa=',
            'Living': 'https://www.ensonhaber.com/yasam?infinity=1&sayfa='
        }

        self.links_of_news = []
        self.dataset = []
        self.errors = []
        # pattern = {
        #     "Source": "",
        #     "Category": "",
        #     "Link": "",
        #     "Title": "",
        #     "Date": "",
        #     "Summary": "",
        #     "Context": ""
        # }
        # i decide to get 300 pages news for balanced dataset
        self.max_page_num = 301
        self.start_date = datetime.now()

    def get_news_links_from_category(self, category_name, category_link):
        start_time = time.time()

        for page_num in range(1, self.max_page_num):
            response = requests.get(f"{category_link}{page_num}")
            soup = BeautifulSoup(response.content, "html.parser")

            for link in soup.find_all("a"):
                if "href" in link:
                    print("okkk")
                link_of_news = link["href"]
                # sometimes youtube or another video source links can comes with a tag
                # for that reason i create a if control is this a news link (all news link has "/" in first char)
                if link_of_news[0] == "/":
                    self.links_of_news.append({"Category": category_name, "Link": link_of_news})
            print(f"Category: {category_name}, Page Number: {page_num}")
        print(f"{category_name} ended at {page_num}, scraping took: {time.time() - start_time} seconds!")

    def get_news_data_from_news_link(self, news_data):

        print(f"""{self.WEB_SITE_LINK}{news_data["Link"]}""")
        response = requests.get(f"""{self.WEB_SITE_LINK}{news_data["Link"]}""", verify=False)
        soup = BeautifulSoup(response.content, "html.parser")
        date = None
        try:
            for li in soup.find("div", {"class": "c-date"}).find_all("li"):
                if "Güncelleme" not in li.text and li.text[0].isdigit():
                    date = datetime.strptime(li.text, "%d.%m.%Y - %H:%M").strftime("%Y/%m/%d")
                    break
        except AttributeError:
            print("c-date Not Found, News is deleted: ", f"""{self.WEB_SITE_LINK}{news_data["Link"]}""")
            self.errors.append(news_data)
            return

        data = {
            "Source": "Ensonhaber",
            "Category": news_data["Category"],
            "Link": f"""{self.WEB_SITE_LINK}{news_data["Link"]}""",
            "Title": (soup.find("h1", {"class": "c-title"}).text).strip(),
            "Summary": (soup.find("div", {"class": "c-desc"}).text).strip(),
            "Context": (soup.find("article", {"class": "body"}).text).strip(),
            "Date": date

        }
        self.dataset.append(data)

    def create_excel(self):
        df = pd.DataFrame(data=self.dataset, columns=["Source", "Category", "Link", "Title", "Summary", "Context", "Date"])
        df.to_excel("Dataset/dataset_20_02_2022.xlsx", index=False)

    def main(self):
        # Getting news links
        # Using threads because i can :p so i dont wait that much!
        thread_list_for_cateogries = []
        for category_name, category_link in self.NEWS_CATEGORY_LINKS.items():
            thread_list_for_cateogries.append(Thread(target=self.get_news_links_from_category, args=[category_name, category_link]))
        for t in thread_list_for_cateogries:
            t.start()
        for t in thread_list_for_cateogries:
            t.join()

        # saving link if any error happens (happend :p)
        json.dump(self.links_of_news, open("Dataset/link_list.json", "w"))
        # self.links_of_news = json.load(open("Dataset/link_list.json", "r"))

        # 16 threads at same time (scraping 16 news data same time)
        start_time = time.time()
        print(f"Start to scraping news data {datetime.now()}")
        pool = ThreadPool(processes=16)
        pool.map(self.get_news_data_from_news_link, self.links_of_news)
        pool.close()
        pool.join()
        print(f"Scraping End. It took {time.time() - start_time} seconds.")
        # Scraping End. It took 3148.4161405563354 seconds.
        self.create_excel()
        print(f"DONE!!")
        # saving news which giving error 
        json.dump(self.errors, open("Dataset/errors.json", "w"))
        print("Creating Excel File")


if __name__ == "__main__":
    ns = NewsScraper()
    ns.main()

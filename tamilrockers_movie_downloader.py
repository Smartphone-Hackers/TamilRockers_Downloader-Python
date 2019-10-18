import requests
from bs4 import BeautifulSoup
import os
import re

class TamilRockers:

    request_url = "https://eu1.proxysite.com/includes/process.php?action=update"

    def domain(self):
        form_data = {
                    "server-option":"eu1",
                    "d":"tamilrockers.com",
                    "allowCookies":"on"
                    }
        r = requests.post(url=self.request_url, data=form_data).text
        self.domain_name = re.findall('http://tamil[a-z]+\.[a-z]{2,3}', r)[0]
        return self.domain_name

class MovieLinks(TamilRockers):

    def movie_url_scraper(self):
        print("Movie Link Scraping. Please Wait..")
        f = open("movie_links.txt", "w")
        for i in range(1, 11):
            form_data = {
                        "d":"{}/index.php/forum/115-tamil-new-dvdrips-hdrips-bdrips-movies/page-{}".format(self.domain(),i),
                        "allowCookies":"on"
                        }

            r = requests.post(url=self.request_url, data=form_data).text
            soup = BeautifulSoup(r, "lxml")

            for a in soup.find_all("td", {"class":"col_f_content "}):
                for i in a.find_all("a",{"class":"topic_title"}):
                    title_id = i.get("id").split("-")[-1]
                    title1 = i.get("title").split("[")[0].replace("(","").replace(")","").strip().replace(" ","-").lower()
                    title2 = "".join(i.get("title").split("]")[0].split('[')[-1].split("-")).replace(" ","-").replace("--", "-").lower()
                    full_title = "http://tamilrockers.ws/index.php/topic/" + title_id + "-" + title1 + title2
                    if "---started" in full_title:
                        f.write("\n" + full_title.split("---started")[0])
                    else:
                        f.write("\n" + full_title)

class MovieDownloader(MovieLinks):

    def movie_downloader(self):
        url = input("Enter Movie URL : ")
        proxy = {"http": "http://52.157.177.105:80"}
        magnetic_link = ""
        print("Searching Magnetic Link.")
        for i in range(50):
            try:
                r = requests.get(url, proxies=proxy).text
                soup = BeautifulSoup(r, "lxml")
                for i in soup.find_all("a", {"class":"bbc_url"}):
                    if i.text == "Magnet Link":
                        magnetic_link = i.get("href")
                        break
                break
            except:
                pass

        os.chdir(r"C:\Users\Anandh\AppData\Roaming\Microsoft\Windows\Start Menu")
        if magnetic_link != "":
            torrent = "µTorrent.lnk \"{}\"".format(magnetic_link)
            os.system(torrent)
        else:
            print("Link Corrupted!.")

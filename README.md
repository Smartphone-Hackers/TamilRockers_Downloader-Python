# TamilRockers_Downloader-Python

step : 1
  - pip install -r requirements.txt

step : 2
  - git clone https://github.com/Smartphone-Hackers/TamilRockers_Downloader-Python/blob/master/tamilrockers_movie_downloader.py

step : 3
  - create object for MovieDownloader class.
  - call method => movie_url_scraper => this method is used to scrap all movie links
      - MovieDownloader.movie_url_scraper()
  - call method => movie_downloader => this method used to download movie to given link.
      - MovieDownloader.movie_downloader()

step : 4 
  - python tamilrockers_movie_downloader.py

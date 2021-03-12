# YTS Torrent File Downloader
## Download any movie's torrent file via python script. (scraping from yts.mx)
Scraping from yts.mx based on command line argument like year of the movie and genre of the movie.

## Usage
```
-mt   movie title   (title of the movie like "ride along")
-mq   movie quality (720p|1080p|2160p|3D)
-mg   movie genre   (run "yts.py -showGenre to view all genre")
-mr   movie rating  (1 to 9)
-o    order by      (run "yts.py -showOrders to view orders")
-my   movie year    (year of the movie like 2021)
-l    language      (run "yts.py -showLanguages to view all languages)"
-show showing number of movies
```
### Examples
Getting 10 horror movies released on 2021.
```python yts.py -my 2021 -mg horror -show 10```
This command will save 10 horror movie's details into json file which are relesed on 2021.
#### List available devices:


## Used modules

- itertools
- threading
- time
- requests
- BeautifulSoup
- sys
- json

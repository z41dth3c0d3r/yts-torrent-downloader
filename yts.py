import itertools
import threading
import time
import requests
from bs4 import BeautifulSoup
import sys
import json

# output file name based on args

fileName = ""
done = False
start_time = 0
# here is the animation
def animate():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        sys.stdout.write("\rScrapping " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush()
    totalTimeTaken = time.time() - start_time
    sys.stdout.write("\rDone!     ")
    print("\nTotal Time Taken : " + str(round(totalTimeTaken, 2)) + " Seconds")
    print("Data Written to " + str(fileName))


if (
    len(sys.argv) == 1
    or sys.argv[1] == "-h"
    or sys.argv[1] == "-help"
    or sys.argv[1] == "--help"
):
    usage = """Usage:
    -mt movie title   (title of the movie like "ride along")
    -mq movie quality (720p|1080p|2160p|3D)
    -mg movie genre   (run "main.py -showGenre to view all genre")
    -mr movie rating  (1 to 9)
    -o  order by      (run "main.py -showOrders to view orders")
    -my movie year    (year of the movie like 2021)
    -l  language      run "main.py -showLanguages to view all languages"

    -show showing number of movies
    
    for example: getting 10 horror movies released on 2021

        python yts.py -my 2021 -mg horror -show 10"""

    # url structure
    # https://yts.mx/browse-movies/hack/720p/action/4/oldest/2019/foreign
    #                              0    1    2     3  4       5    6
    # 0 - movie title (default is 0)
    # 1 - movie quality (default is all)
    # 2 - movie genre (default is all)
    # 3 - movie rating (default is 0)
    # 4 - order by (default is latest)
    # 5 - movie year (default is 0)
    # 6 - language (default is all)

    print(usage)

elif (len(sys.argv) == 2) and (
    sys.argv[1] == "-showGenre"
    or sys.argv[1] == "-showOrders"
    or sys.argv[1] == "-showLanguages"
):
    if sys.argv[1] == "-showGenre":
        print(
            """
        Genres

            all
            action
            adventure
            animation
            biography
            comedy
            crime
            documentary
            drama
            family
            fantasy
            film-noir
            game-show
            history
            horror
            music
            musical
            mystery
            news
            reality-tv
            romance
            sci-fi
            sport
            talk-show
            thriller
            war
            western"""
        )
    elif sys.argv[1] == "-showOrders":
        print(
            """
        Orders

            latest
            oldest
            featured
            seeds
            peers
            year
            rating
            likes
            alphabetical
            downloads"""
        )
    elif sys.argv[1] == "-showLanguages":
        print(
            """
        Languages

            all - All language
            en - English
            ja - Japanese
            fr - French
            it - Italian
            es - Spanish
            de - German
            zh - Chinese
            ko - Korean
            hi - Hindi
            cn - Cantonese
            ru - Russian
            sv - Swedish
            pt - Portuguese
            pl - Polish
            da - Danish
            no - Norwegian
            th - Thai
            nl - Dutch
            te - Telugu
            fi - Finnish
            cs - Czech
            ta - Tamil
            vi - Vietnamese
            tr - Turkish
            id - Indonesian
            fa - Persian
            el - Greek
            ar - Arabic
            tl - Tagalog
            he - Hebrew
            ur - Urdu
            hu - Hungarian
            ms - Malay
            bn - Bangla
            ro - Romanian
            is - Icelandic
            ml - Malayalam
            et - Estonian
            ca - Catalan
            pa - Punjabi
            uk - Ukrainian
            sr - Serbian
            xx - xx
            af - Afrikaans
            mr - Marathi
            kn - Kannada
            eu - Basque
            sk - Slovak
            ak - Akan
            am - Amharic
            gl - Galician
            bs - Bosnian
            ka - Georgian
            bo - Tibetan
            la - Latin
            lv - Latvian
            mn - Mongolian
            nb - Norwegian Bokmål
            wo - Wolof
            az - Azerbaijani
            so - Somali
            ab - Abkhazian
            iu - Inuktitut
            ht - Haitian Creole
            sh - Serbo-Croatian
            st - Southern Sotho
            lg - Ganda
            ky - Kyrgyz
            ps - Pashto
            lb - Luxembourgish
            mi - Maori
            aa - Afar
            yi - Yiddish
            ga - Irish
            km - Khmer
            mk - Macedonian
            os - Ossetic
            sw - Swahili"""
        )

elif len(sys.argv) >= 2:

    # concatanating command line args to url for get request

    baseURL = "https://yts.mx/browse-movies"

    if "-mt" in sys.argv:
        baseURL += "/" + sys.argv[sys.argv.index("-mt") + 1]
        fileName += sys.argv[sys.argv.index("-mt") + 1] + "_"
    else:
        baseURL += "/" + str(0)
        fileName += "movies" + "_"
    if "-mq" in sys.argv:
        baseURL += "/" + sys.argv[sys.argv.index("-mq") + 1]
        fileName += sys.argv[sys.argv.index("-mq") + 1] + "_"
    else:
        baseURL += "/" + "all"
        fileName += "allQuality" + "_"
    if "-mg" in sys.argv:
        baseURL += "/" + sys.argv[sys.argv.index("-mg") + 1]
        fileName += sys.argv[sys.argv.index("-mg") + 1] + "_"
    else:
        baseURL += "/" + "all"
        fileName += "allGenre" + "_"
    if "-mr" in sys.argv:
        baseURL += "/" + sys.argv[sys.argv.index("-mr") + 1]
        fileName += sys.argv[sys.argv.index("-mr") + 1] + "_"
    else:
        baseURL += "/" + str(0)
        fileName += "allRating" + "_"
    if "-o" in sys.argv:
        baseURL += "/" + sys.argv[sys.argv.index("-o") + 1]
        fileName += sys.argv[sys.argv.index("-o") + 1] + "_"
    else:
        baseURL += "/" + "latest"
        fileName += "OrderdBylatest" + "_"
    if "-my" in sys.argv:
        baseURL += "/" + sys.argv[sys.argv.index("-my") + 1]
        fileName += sys.argv[sys.argv.index("-my") + 1] + "_"
    else:
        baseURL += "/" + str(0)
        fileName += "allYear" + "_"
    if "-l" in sys.argv:
        baseURL += "/" + sys.argv[sys.argv.index("-l") + 1]
        fileName += sys.argv[sys.argv.index("-l") + 1] + "_"
    else:
        baseURL += "/" + "all"
        fileName += "allLanguages" + "_"
    if "-show" in sys.argv:
        show = sys.argv[sys.argv.index("-show") + 1]
    else:
        show = 5
        fileName += "5_Movies"

    firstPage = requests.get(baseURL)

    start_time = time.time()

    t = threading.Thread(target=animate)
    t.start()

    firstPageContent = BeautifulSoup(firstPage.content, "html.parser")

    # getting total number of movies in get request

    totalMovies = (
        firstPageContent.find(class_="browse-content")
        .find(class_="container")
        .find("h2")
        .find("b")
        .get_text()
    )

    moviesWithDetails = {}

    moviesWithDetails["totalMovies"] = totalMovies

    # loop through pages wchich is given via -show arg other wise 10 movies
    # determining how many pages based on show args
    if int(totalMovies.replace(",", "")) < int(show):
        show = totalMovies

    fileName += str(show) + "_Movies.json"

    # calculating total pages to scrap

    total_pages = int(int(show) / 20)

    if total_pages <= 0 or int(show) % 20 > 0:
        total_pages += 1

    totalMoviesEncoutered = 0

    # loop through calculated pages

    for i in range(1, total_pages + 1):
        if i == 1:
            dynamiURL = baseURL
        else:
            dynamiURL = baseURL + "?page=" + str(i)
        paginationPages = requests.get(dynamiURL)
        pageContent = BeautifulSoup(paginationPages.content, "html.parser")

        # movie variable storing all movie details in a single page

        movies = (
            pageContent.find(class_="browse-content")
            .find(class_="container")
            .find(class_="row")
            .find_all(class_="browse-movie-wrap")
        )
        Genres = []
        for movie in movies:

            if totalMoviesEncoutered == int(show):
                break

            # getting title of the movie

            title = (
                movie.find(class_="browse-movie-bottom")
                .find(class_="browse-movie-title")
                .get_text()
            )

            # holding download links

            linkToMovie = movie.find(class_="browse-movie-bottom").find(
                class_="browse-movie-title"
            )["href"]

            # getting download link of torrent file

            downloadPage = requests.get(linkToMovie)
            downloadPageContent = BeautifulSoup(downloadPage.content, "html.parser")
            realDownloadLinks = dict()
            if downloadPageContent.find(id="movie-info") != None:
                downloadLinks = (
                    downloadPageContent.find(id="movie-info")
                    .find(class_="hidden-md hidden-lg")
                    .find_all("a")
                )
                for downloadLink in downloadLinks:
                    if downloadLink.get_text() != "Download Subtitles":
                        realDownloadLinks[downloadLink.get_text()] = downloadLink[
                            "href"
                        ]

            # getting year of the movie

            year = (
                movie.find(class_="browse-movie-bottom")
                .find(class_="browse-movie-year")
                .get_text()
            )

            # getting rating of the movie

            rating = movie.find(class_="browse-movie-link").find(class_="rating")
            if rating != None:
                rating = rating.get_text()

            # gettig genre of the movie
            genres = movie.find(class_="browse-movie-link").find_all("h4")
            for genre in genres:
                Genres.append(genre.get_text())
            Genres.pop(0)

            moviesWithDetails[title] = {
                "title": title,
                "year": year,
                "ratings": rating,
                "genres": Genres,
                "download links": realDownloadLinks,
            }
            Genres = []
            realDownloadLinks = {}
            totalMoviesEncoutered = totalMoviesEncoutered + 1

    outputFile = open(fileName, "w")
    outputFile.write(json.dumps(moviesWithDetails))
    outputFile.close()
    done = True
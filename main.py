import requests
from bs4 import BeautifulSoup
import sys

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
    -l  language      run "main.py -showLanguages to view all languages" """
    print(usage)

elif len(sys.argv) == 2:
    if sys.argv[1] == "-showGenre":
        print(
            """all
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
            """latest
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
            """all - All language
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

else:

    # base url
    yts_serach = requests.get("https://yts.mx/browse-movies")

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

    pageContent = BeautifulSoup(yts_serach.content, "html.parser")

    totalMovies = (
        pageContent.find(class_="browse-content")
        .find(class_="container")
        .find("h2")
        .find("b")
        .get_text()
    )

    print(totalMovies)
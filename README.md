# Lottopal
Simple Lotto drawing application taking into account the history of drawn numbers

#Features
The application will generate 6 random numbers in the range from 1 to 49. The number of draws can be chosen freely, standard
will be one draw.

Each single draw will be stored in a list, sorted and written as csv-string to a draw list. The draw list will be written
to a file (or database?).

For the German Lotto 6aus49 it is possible to check against a list of the most drawn numbers of the Wednesday and Saturday
session. The lists will be automatically scraped from the website www.lottozahlenonline.de/statistik.

Last but not least an UI will be added usinng TKinter.    
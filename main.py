# -*- coding: utf-8 -*-
 

MyFavoriteSong = {'Artist': "Oxxxymiron", 'Genre': "Rap or Hip Hop", 'Song': "Город под подошвой", 
                  'DurationInSeconds': str(4*60+7) + " seconds", 'Year': 2015, 'ViewsOnYoutube': 47000000, 
                  'PublicationDate': "21.09.2015", 'MyPersonalScore': str(4.5) + " out of " + str(5)}

def dict_printer():
    for key, value in MyFavoriteSong.items():
        print(key, ":", value)


def guesser(key, value):
    if key in MyFavoriteSong and str(value) == str(MyFavoriteSong[key]):
        return True
    else:
        return False


def main():
    key = input("guess key: ")
    value = input("guess value: ")
    if guesser(key, value) is True:
        print(key, ":", value, "guessed right\n")
    else:
        print(key, ":", value, "guessed wrong\n")


main()
dict_printer() 


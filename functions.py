# function for artist
def artistFunc():
    Name = "Oxxxymiron"
    return Name



print(artistFunc())


# function for Gengre
def genreFunc():
    Name = "Rap or Hip-Hop"
    return Name


print(genreFunc())


# function for Year
def yearFunc():
    Name = 2015
    return Name


print(yearFunc())
TooLow = 50000
TooHigh = 50000000


# True/False function
def viewsFunc(number):

    if number < 47000000:
        return True
    else:
        return False


A = viewsFunc(TooHigh)
B = viewsFunc(TooLow)
print(A)
print(B)

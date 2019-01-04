myUniqueList = []
myLeftLovers = []
print("My unique list before = " + str(myUniqueList))
print("Left Lovers list before = " + str(myLeftLovers))


def addToListIfNotExist(toAdd):
    if toAdd not in myUniqueList:
        myUniqueList.append(toAdd)
        return True
    else:
        return False


def main(listMember):
    wasAdded = addToListIfNotExist(listMember)
    if wasAdded is False:
        myLeftLovers.append(listMember)


main(5)
main(6)
main(7)
main(5)
main(8)
main(6)
main('a')
main('6')

print("My unique list after = " + str(myUniqueList))
print("Left Lovers list after = " + str(myLeftLovers))

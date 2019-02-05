def main():
    with open('atata.txt', 'w') as f:
        for i in range(10):
            f.write("This is line %d\r\n" % (i+1))

if __name__ == '__main__':
    main()

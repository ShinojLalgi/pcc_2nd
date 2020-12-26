def make_album():
    """ Prints a dictionary containing information about a album """

    while True:
        title = input("Enter album title: ")
        if title == 'q':
            break

        artist = input("Enter artist name: ")
        if artist == 'q':
            break

        album = {
            'title'  : title.title(),
            'artist' : artist.title() 
        }

        print()
        print(album)
        print()

make_album()


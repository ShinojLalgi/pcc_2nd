def make_album(title, artist, number_of_songs = None):
    """ Returns a dictionary containing information about a album """

    album = {
        'title'  : title.title(),
        'artist' : artist.title() 
    }

    if number_of_songs:
        album['number of songs'] = number_of_songs

    return album


print(make_album('654', 'bieber'))
print(make_album('love', 'mj'))
print(make_album('dan', 'dua', 654))
# Helen Chau
# chauh4@uci.edu
# 84334175

def read():
    ''' Created read function to open file and read its contents
    and then split it to different lists for data to send '''
    # Opens file
    open_f = open("datafile.txt")
    # Read lines of file
    read_f = open_f.readlines()
    # Created lists to collect data
    data = []
    songs = []
    popularity = []
    # Removed name of artist to save for graph title
    artist = read_f.pop(0)
    # Iterates through file contents
    for i in read_f:
        # Splitting to get sound track popularity data
        data.append(i.split("//popularity//"))
    # Iterates through data
    for s in data:
        # Replaces new line symbol with nothing
        s[1] = s[1].replace("\n", "")
    # Iterates in data again with no new lines
    for m in data:
        # Appends song title to song list
        songs.append(m[0])
        # Appends popularity rating to popularity list
        popularity.append(int(m[1]))
    # Returns songs and popularity
    return songs, popularity

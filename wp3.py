# Helen Chau
# chauh4@uci.edu
# 84334175

import data_table as dt
import spotify_data as sd
import reading_file as rf


def main():
    ''' Created main function to run main code'''
    # Printing out welcome message with brief description of its function
    print("Welcome to Spotify Top Tracks visualizer!")
    print("This data visualizer generates a bar graph", end=' ')
    print("of your chosen artist and their top", end=' ')
    print("song tracks with their popularity score!")

    # Asking user for input for their desired artist
    artist = input("Enter an artist: ")

    # Checking if artist exists
    if sd.spotify_data(artist) is True:
        # Reads file that spotify_data writes to
        split = rf.read()
        # Sending data to plot_data function
        dt.plot_data(split[0], split[1], artist)
        # Printing out confirmation message
        print("Success! Bar Graph has been made!")
        print("Check your files for the newly created png!")
    else:
        # If artist doesn't exist, then printing out an Error message
        print("Unsuccessful...enter a valid artist!")


if __name__ == "__main__":
    main()

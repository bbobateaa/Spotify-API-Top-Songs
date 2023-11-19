# Helen Chau
# chauh4@uci.edu
# 84334175

import matplotlib.pyplot as plot


def plot_data(x_data: list, y_data: list, artist) -> None:
    ''' Created function to take in data parameters to generate a bar graph'''
    fig, ax = plot.subplots(figsize=(30, 10))
    # Sending data to bar graph function
    ax.barh(x_data, y_data, color="green")
    # Naming x-axis and y-axis and title of graph
    ax.set_xlabel("Popularity Rank")
    ax.set_ylabel("Tracks")
    ax.invert_yaxis()
    ax.set_title(f"Top Tracks with Popularity Rank of {artist}")
    # Replacing spaces with "_" for saving image file
    artist = artist.replace(" ", "_")
    # saves data to an image file
    plot.savefig(f'{artist}_Top_Tracks.png')

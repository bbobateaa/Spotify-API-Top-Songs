# Spotify-API-Top-Songs
This project uses the Spotify API to output ten top songs from any given artist and their popularity rate and display the data as a bar graph.

My program uses the matplotlib module to take the available data and generate a bar graph as a png image. 

Starting off in the program, the user is prompted to enter an existing artist, if they enter an artist that cannot be found or does not exist, it will output an error message asking them to try again. 

If the user does enter an existing artist, then the program calls my Spotify module which is responsible for extracting data needed from Spotify and uses the Spotify API to do so. After it receives the data needed, the module writes the data in a text file which is then used by the reading module. 

My reading module takes the file and opens and reads its content, it then splits the data to get the song track name and its popularity rate. The reading module function returns a tuple of two lists containing the song tracks and the popularity rate. The program then inputs that return value into the data_table module, which uses the matplotlib functions to generate a table. 

It also names the png file as the artist's name so the user can easily find their data table. 
Finally, the program has finished and generates a confirmation message to the screen to let the user know that their bar graph has been made.

# python-filemagic
This command line program sorts files according to its format.
You input files as command-line arguments, separting each file with a single space. 
The program will create a folder called "sorted" in the current working directory.
Then, the program will create a folder for each unique format for the inputs inside the "sorted" folder.

# How to
1. Download the python script
1. Place it in a directory
1. Launch terminal or the command-line
1. Write "python filemagic.py" followed by the files you want to sort
1. Press "enter" and the program will do its job

**Example command line code**
> python filemagic.py image1.png image2.png image3.jpg image4.tiff

# Supported file formats
* JPEG
* PNG
* TIFF
* GIF

# imports os for finding and moving files
import os
# imports sys for command line arguments
import sys

def filemagic(file):
    '''
    Creates a folder 'sorted' and a subfolder with the file's format as name.
    INPUT: Filepath
    '''
    # A dictionary containing magic byte signatures of the formats
    file_bytes = {
        'JPEG':'FFD8FFE0',
        'PNG':'89504E470D0A1A0A',
        'TIFF':'49492A00',
        'GIF89a':'474946383961'
    }
    # reads the file if it exists
    if os.path.isfile(file):
        with open(file, mode="rb") as f:
            # assigns a uppercase hex representation of the 8 first bytes
            # we will use this to find the matching file in our dictionary
            data = f.read(8).hex().upper()
            # creates a folder "sorted" if it's not created already
            try:
                os.mkdir('sorted')
            except:
                pass
            # compares the dictionaries values with our file's first bytes
            for key, value in file_bytes.items():
                if data.startswith(value):
                    # creates a directory for that file inside 'sorted'
                    try:
                        os.chdir('sorted')
                        os.mkdir(key)
                        os.chdir('..')
                    except:
                        os.chdir('..')
                    finally:
                        # creates the path we want to move the file to
                        # uses os.path.join to create a path that works on mac/windows/linux
                        move_path = os.path.join('sorted',key, file)
                        os.rename(file, move_path)
                    return f"The file {file} is of type {key} and has been moved to sorted/{key}"
                else:
                    pass
    else:
        return f"{file} was not found!"

if __name__ == "__main__":
    # takes arguments from index 1. Index 0 is the .py-filename
    for file in sys.argv[1:]:
        print(filemagic(file))

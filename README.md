# Onge-Sprite-Tools-v2

This script allows you to create sprite sheets from a directory of images, with more options than the original version. You can also use the [web version](https://ongezell.com/project/ongespritetools.html) of this tool if you prefer not to use the command line.

### Usage

To use the script, you need to provide the directory containing the input image files as a positional argument. You can also specify the following optional arguments:

- `--columns`: The number of columns in the sprite sheet. The default value is 1.
- `--direction`: The direction of the columns. You can choose between `horizontal` and `vertical`. The default value is `horizontal`.
- `--output`: The output file for the sprite sheet. The default value is `sprite_sheet.png`.

For example, to create a sprite sheet with 2 vertical columns and the output file named `mysprite.png`, you can use the following command:

`python onge-sprite-tools-v2.py my_image_directory --columns 2 --direction vertical --output mysprite.png`

## Requirements

To use this script, you will need to have the following software installed and available on your system:

- [Python](https://www.python.org/): The script is written in Python, so you will need to have a Python interpreter installed on your system in order to run it.
- [Pillow](https://pillow.readthedocs.io/en/stable/): The script uses the Pillow library to create and manipulate image files. You can install Pillow using the following 

I hope you find this script hella useful!



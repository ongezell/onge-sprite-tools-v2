# onge-sprite-tools-v2

This script allows you to create sprite sheets from a directory of images, with more options than the original version. You can also use the [web version](https://ongezell.com/project/ongespritetools.html) of this tool if you prefer not to use the command line.

### Usage

To use the script, you need to provide the directory containing the input image files as a positional argument. You can also specify the following optional arguments:

- `--columns`: The number of columns in the sprite sheet. The default value is 1.
- `--direction`: The direction of the columns. You can choose between `horizontal` and `vertical`. The default value is `horizontal`.
- `--output`: The output file for the sprite sheet. The default value is `sprite_sheet.png`.

For example, to create a sprite sheet with 2 vertical columns and the output file named `mysprite.png`, you can use the following command:

`python script.py my_image_directory --columns 2 --direction vertical --output mysprite.png`

I hope you find this script hella useful!



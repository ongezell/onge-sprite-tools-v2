# Developed by Ongezell at Ongezell.com
# Web version available at https://ongezell.com/project/ongespritetools.html

import argparse
import os
import re

from PIL import Image

def create_sprite_sheet(images, columns, direction, output_file):
    
    if direction == 'horizontal':
        rows = (len(images) + columns - 1) // columns
    elif direction == 'vertical':
        rows = columns
        columns = (len(images) + rows - 1) // rows
    else:
        raise ValueError('Invalid direction')

   
    cell_width = images[0].width
    cell_height = images[0].height
    sprite_width = cell_width * columns
    sprite_height = cell_height * rows

   
    sprite_sheet = Image.new('RGBA', (sprite_width, sprite_height))

   
    if direction == 'horizontal':
        for row in range(rows):
            for column in range(columns):
                
                index = row * columns + column
                if index >= len(images):
                   
                    break
                
                sprite_sheet.paste(images[index], (column * cell_width, row * cell_height))
    elif direction == 'vertical':
        for column in range(columns):
            for row in range(rows):
               
                index = column * rows + row
                if index >= len(images):
                    
                    break
                
                sprite_sheet.paste(images[index], (column * cell_width, row * cell_height))

    
    sprite_sheet.save(output_file)

def extract_number_from_filename(filename):
    
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return 0

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='the directory containing the input image files')
    parser.add_argument('--columns', type=int, default=1, help='the number of columns in the sprite sheet')
    parser.add_argument('--direction', default= 'horizontal', choices=['horizontal', 'vertical'], help='the direction of the columns')
    parser.add_argument('--output', default='sprite_sheet.png', help='the output file')
    args = parser.parse_args()

    
    images = []
    for file in sorted(os.listdir(args.directory), key=extract_number_from_filename):
        if file.endswith('.png') or file.endswith('.jpg'):
            images.append(Image.open(os.path.join(args.directory, file)))

    
    create_sprite_sheet(images, args.columns, args.direction, args.output)


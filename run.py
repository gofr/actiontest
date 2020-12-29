#!/usr/bin/env python3

from PIL import Image


if __name__ == '__main__':
    img = Image.new('RGB', (32, 32))
    name = 'icon.png'
    img.save(name)
    print(f'Image "{name}" created successfully.')

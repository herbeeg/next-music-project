import sys

class ImageGen:
    """
    Handles the construction of the ASCII art
    rectangles that represent what software,
    styles and influences should be used
    for the next project.
    """
    def __init__(self, typeface='#'):
        self.typeface = typeface

    def software(self, ident=''):
        images = {
            'bambootracker': [],
            'famitracker': [
                [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
                [(2, 2)],
                [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12)],
                [(4, 2), (4, 10)],
                [(5, 2), (5, 10)]
            ],
            'lmms': [],
            'sunvox': []
        }

        image_data = []

        try:
            image_data = images[ident]
        except IndexError as ex:
            sys.stdout.write('Invalid software type passed to image generator.\n')
            sys.exit()

        return image_data

    def getBase(self):
        return [
            ['@', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '@'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['@', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '@']
        ]

    def getTypeface(self):
        return self.typeface
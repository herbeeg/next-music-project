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
            'bambootracker': [
                [(1, 2), (1, 3), (1, 4)],
                [(2, 2), (2, 5)],
                [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12)],
                [(4, 2), (4, 6), (4, 10)],
                [(5, 2), (5, 3), (5, 4), (5, 5), (5, 10)]
            ],
            'famitracker': [
                [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
                [(2, 2)],
                [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12)],
                [(4, 2), (4, 10)],
                [(5, 2), (5, 10)]
            ],
            'lmms': [
                [(1, 2)],
                [(2, 2)],
                [(3, 2), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12)],
                [(4, 2), (4, 8), (4, 10), (4, 12)],
                [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 8), (5, 12)]
            ],
            'sunvox': [
                [(1, 3), (1, 4), (1, 5), (1, 6)],
                [(2, 2)],
                [(3, 3), (3, 4), (3, 5), (3, 8), (3, 12)],
                [(4, 6), (4, 9), (4, 11)],
                [(5, 2), (5, 3), (5, 4), (5, 5), (5, 10)]
            ]
        }

        image_data = []

        try:
            image_data = images[ident]
        except IndexError as ex:
            sys.stdout.write('Invalid software type passed to image generator.\n')
            sys.exit()

        return image_data

    def extension(self, ident=''):
        images = {
            '2a03': [
                [(1, 3), (1, 4), (1, 5)],
                [(2, 2), (2, 6)],
                [(3, 5), (3, 8), (3, 10)],
                [(4, 3), (4, 9), (4, 10), (4, 11)],
                [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 8), (5, 12)]
            ],
            'fds': [],
            'vrc6': [],
            'vrc7': [],
            'n163': []
        }

        image_data = []

        try:
            image_data = images[ident]
        except IndexError as ex:
            sys.stdout.write('Invalid FamiTracker extension type passed to image generator.\n')
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
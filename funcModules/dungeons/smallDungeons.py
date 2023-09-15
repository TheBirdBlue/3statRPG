'''
Dungeon Name = {

    'room0': {  # Room ID
        'x': 0,  # X position (Up and Down)
        'y': 0,  # Y position (Left and Right)
        'direction': (N, E, S, W),  # 0 or 1 for movement; North, East, South, West
        'room': ('N', 'E', 'S', 'W'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },
}

'''

TJunction_01 = {

    'room0': {  # Room ID
        'x': 1,  # X position
        'y': 0,  # Y position
        'direction': (0, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room1', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 1,  # X position
        'y': 1,  # Y position
        'direction': (1, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('exit', 'room2', 'none', 'room0'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room2': {  # Room ID
        'x': 1,  # X position
        'y': 2,  # Y position
        'direction': (0, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'none', 'room1'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 0,  # X position
        'y': 1,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room1', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }
}

LShape_02 = {

    'room0': {  # Room ID
        'x': 0,  # X position
        'y': 0,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room1', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 1,  # X position
        'y': 0,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room0', 'none', 'room2', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room2': {  # Room ID
        'x': 2,  # X position
        'y': 0,  # Y position
        'direction': (1, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room1', 'room3', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room3': {  # Room ID
        'x': 2,  # X position
        'y': 1,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'exit', 'none', 'room2'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 2,  # X position
        'y': 2,  # Y position
        'direction': (0, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'none', 'room3'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }

}

LongLShape_03 = {

    'room0': {  # Room ID
        'x': 0,  # X position
        'y': 0,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room1', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 1,  # X position
        'y': 0,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room0', 'none', 'room2', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room2': {  # Room ID
        'x': 2,  # X position
        'y': 0,  # Y position
        'direction': (1, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room1', 'room3', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room3': {  # Room ID
        'x': 2,  # X position
        'y': 1,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room4', 'none', 'room2'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room4': {  # Room ID
        'x': 2,  # X position
        'y': 2,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room5', 'none', 'room3'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room5': {  # Room ID
        'x': 2,  # X position
        'y': 3,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'exit', 'none', 'room4'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 2,  # X position
        'y': 4,  # Y position
        'direction': (0, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('o', 'o', 'o', 'room5'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }
}

FourWaySouth_04 = {

    'room0': {  # Room ID
        'x': 2,  # X position
        'y': 2,  # Y position
        'direction': (1, 1, 1, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('room1', 'room6', 'room5', 'room3'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 2,  # X position
        'y': 1,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room2', 'none', 'room0', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room2': {  # Room ID
        'x': 2,  # X position
        'y': 0,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room1', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room3': {  # Room ID
        'x': 1,  # X position
        'y': 2,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room0', 'none', 'room4'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room4': {  # Room ID
        'x': 0,  # X position
        'y': 2,  # Y position
        'direction': (0, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room3', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room5': {  # Room ID
        'x': 2,  # X position
        'y': 3,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room0', 'none', 'exit', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 2,  # X position
        'y': 4,  # Y position
        'direction': (1, 0, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room5', 'none', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room7': {  # Room ID
        'x': 3,  # X position
        'y': 2,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room8', 'none', 'room0'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room8': {  # Room ID
        'x': 4,  # X position
        'y': 2,  # Y position
        'direction': (0, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'none', 'room7'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }
}

FourWayNorth_05 = {

    'room0': {  # Room ID
        'x': 2,  # X position
        'y': 2,  # Y position
        'direction': (1, 1, 1, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('room1', 'room7', 'room5', 'room3'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 1,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('exit', 'none', 'room0', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 0,  # X position
        'y': 2,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room1', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room3': {  # Room ID
        'x': 2,  # X position
        'y': 1,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room0', 'none', 'room4'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room4': {  # Room ID
        'x': 2,  # X position
        'y': 0,  # Y position
        'direction': (0, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room3', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room5': {  # Room ID
        'x': 3,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room0', 'none', 'room6', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room6': {  # Room ID
        'x': 4,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room5', 'none', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room7': {  # Room ID
        'x': 2,  # X position
        'y': 3,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room8', 'none', 'room0'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room8': {  # Room ID
        'x': 2,  # X position
        'y': 4,  # Y position
        'direction': (0, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'none', 'room7'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }
}

FourWayEast_06 = {

    'room0': {  # Room ID
        'x': 2,  # X position
        'y': 2,  # Y position
        'direction': (1, 1, 1, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('room1', 'room7', 'room5', 'room3'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 1,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room2', 'none', 'room0', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room2': {  # Room ID
        'x': 0,  # X position
        'y': 2,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room1', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room3': {  # Room ID
        'x': 2,  # X position
        'y': 1,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room0', 'none', 'room4'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room4': {  # Room ID
        'x': 2,  # X position
        'y': 0,  # Y position
        'direction': (0, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room3', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room5': {  # Room ID
        'x': 3,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room0', 'none', 'room6', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room6': {  # Room ID
        'x': 4,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room5', 'none', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room7': {  # Room ID
        'x': 2,  # X position
        'y': 3,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'exit', 'none', 'room0'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 2,  # X position
        'y': 4,  # Y position
        'direction': (0, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'none', 'room7'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }
}

FourWayWest_07 = {

    'room0': {  # Room ID
        'x': 2,  # X position
        'y': 2,  # Y position
        'direction': (1, 1, 1, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('room1', 'room7', 'room5', 'room3'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 1,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room2', 'none', 'room0', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room2': {  # Room ID
        'x': 0,  # X position
        'y': 2,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room1', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room3': {  # Room ID
        'x': 2,  # X position
        'y': 1,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room0', 'none', 'exit'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 2,  # X position
        'y': 0,  # Y position
        'direction': (0, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room3', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room5': {  # Room ID
        'x': 3,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room0', 'none', 'room6', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room6': {  # Room ID
        'x': 4,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room5', 'none', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room7': {  # Room ID
        'x': 2,  # X position
        'y': 3,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room8', 'none', 'room0'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room8': {  # Room ID
        'x': 2,  # X position
        'y': 4,  # Y position
        'direction': (0, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'none', 'room7'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }
}

Eight_08 = {

    'room0': {  # Room ID
        'x': 1,  # X position
        'y': 1,  # Y position
        'direction': (1, 0, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room1', 'none', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room1': {  # Room ID
        'x': 0,  # X position
        'y': 1,  # Y position
        'direction': (0, 1, 1, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room6', 'room0', 'room2'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room2': {  # Room ID
        'x': 0,  # X position
        'y': 0,  # Y position
        'direction': (0, 1, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room1', 'room3', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room3': {  # Room ID
        'x': 1,  # X position
        'y': 0,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room2', 'none', 'room4', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room4': {  # Room ID
        'x': 2,  # X position
        'y': 0,  # Y position
        'direction': (1, 1, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room3', 'room5', 'room9', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room5': {  # Room ID
        'x': 2,  # X position
        'y': 1,  # Y position
        'direction': (0, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'room8', 'none', 'room4'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room6': {  # Room ID
        'x': 0,  # X position
        'y': 2,  # Y position
        'direction': (0, 0, 1, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room7', 'room1'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room7': {  # Room ID
        'x': 1,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room6', 'none', 'room8', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room8': {  # Room ID
        'x': 2,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('room7', 'none', 'room11', 'room5'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room9': {  # Room ID
        'x': 3,  # X position
        'y': 0,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room4', 'none', 'room10', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room10': {  # Room ID
        'x': 4,  # X position
        'y': 0,  # Y position
        'direction': (1, 1, 0, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room9', 'room13', 'none', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room11': {  # Room ID
        'x': 3,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('room8', 'none', 'room12', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room12': {  # Room ID
        'x': 4,  # X position
        'y': 2,  # Y position
        'direction': (1, 0, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('room11', 'none', 'none', 'room13'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'room13': {  # Room ID
        'x': 4,  # X position
        'y': 1,  # Y position
        'direction': (1, 1, 0, 1),  # 0 or 1 for movement; North, East, South, West
        'room': ('exit', 'room12', 'none', 'room10'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    },

    'exit': {  # Room ID
        'x': 3,  # X position
        'y': 1,  # Y position
        'direction': (0, 0, 1, 0),  # 0 or 1 for movement; North, East, South, West
        'room': ('none', 'none', 'room13', 'none'),  # Room ID to move to; North, East, South, West
        'action': []  # List of actions taken in that room
    }
}

list = (TJunction_01, LShape_02, LongLShape_03, FourWaySouth_04, FourWayNorth_05, FourWayEast_06, FourWayWest_07,
        Eight_08)


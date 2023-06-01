import os
from enum import Enum
from typing import Dict, Tuple

from enum import Enum

class PieceName(Enum):
    GAP_LEVEL_1 = "gap_level_1"
    GAP_DOWN_1 = "gap_down_1"
    FLAT_ROAD_1 = "flat_road_1"
    START_WITH_ICON_1 = "start_with_icon_1"
    FINISH_WITH_ICON_1 = "finish_with_icon_1"
    BOOSTER_1 = "booster_1"
    ROAD_CURVE_LEFT_1 = "road_curve_left_1"
    ROAD_CURVE_RIGHT_1 = "road_curve_right_1"
    ROAD_CURVE_LEFT_2 = "road_curve_left_2"
    ROAD_CURVE_RIGHT_2 = "road_curve_right_2"
    ROAD_STEP_UP_2 = "road_step_up_2"
    ROAD_STEP_UP_3 = "road_step_up_3"
    ROAD_STEP_UP_1 = "road_step_up_1"
    ROAD_STEP_DOWN_2 = "road_step_down_2"
    ROAD_STEP_DOWN_3 = "road_step_down_3"
    ROAD_STEP_DOWN_1 = "road_step_down_1"
    ROAD_SLOPE_UP_TOP_2 = "road_slope_up_top_2"
    ROAD_SLOPE_DOWN_TOP_2 = "road_slope_down_top_2"
    ROAD_SLOPE_DOWN_BOTTOM_2 = "road_slope_down_bottom_2"
    ROAD_SLOPE_UP_BOTTOM_2 = "road_slope_up_bottom_2"
    ROAD_SLOPE_UP_FLAT_1 = "road_slope_up_flat_1"
    ROAD_SLOPE_DOWN_FLAT_1 = "road_slope_down_flat"
    ROAD_SLOPE_UP_TOP_1 = "road_slope_up_top_1"
    ROAD_SLOPE_DOWN_TOP_1 = "road_slope_down_top_1"
    ROAD_SLOPE_UP_BOTTOM_1 = "road_slope_up_bottom_1"
    ROAD_SLOPE_DOWN_BOTTOM_1 = "road_slope_down_bottom_1"
    ROAD_CURVE_LEFT_3 = "road_curve_left_3"
    ROAD_CURVE_RIGHT_3 = "road_curve_right_3"
    ROAD_CURVE_LEFT_4 = "road_curve_left_4"
    ROAD_CURVE_RIGHT_4 = "road_curve_right_4"
    ROAD_CHECKPOINT_WITH_ICON_1 = "road_checkpoint_with_icon_1"
    ROAD_SHALLOW_SLOPE_BOTTOM_2 = "road_shallow_slope_bottom_2"
    ROAD_SHALLOW_SLOPE_TOP_2 = "road_shallow_slope_top_2"
    ROAD_SHALLOW_SLOPE_UP_FLAT_1 = "road_shallow_slope_up_flat_1"
    ROAD_SHALLOW_SLOPE_DOWN_FLAT_1 = "road_shallow_slope_down_flat_1"

class Piece:
    def __init__(self, name: PieceName, overrides: dict):
        default_config = {
            "size": [1,1,0],
            "curve": 0,
            "slope": 0,
            "checkpoint": False,
            "finish": False,
            "booster_force": None,
            "booster_speed": None,
            "offset": [0,0,0],
            "default_rotation_y": 0,
            "default_incline": 0,
            "origin_at_end": False
        }

        self.configurations = {
            PieceName.GAP_LEVEL_1: {**default_config, "id": -1, "offset": [0,0,-.05]},
            PieceName.GAP_DOWN_1: {**default_config, "id": -1, "slope":-1},
            PieceName.FLAT_ROAD_1: {**default_config, "id": 0},
            PieceName.START_WITH_ICON_1: {**default_config, "id": 1, "finish": True},
            PieceName.FINISH_WITH_ICON_1: {**default_config, "id": 2, "finish": True},
            PieceName.BOOSTER_1: {**default_config, "id": 69, "checkpoint": True, "booster_force": 1, "booster_speed": 120},
            PieceName.ROAD_CURVE_LEFT_1: {**default_config, "id": 3, "curve": 1},
            PieceName.ROAD_CURVE_RIGHT_1: {**default_config, "id": 3, "curve": 2, "default_rotation_y": 270},
            PieceName.ROAD_CURVE_LEFT_2: {**default_config, "id": 4, "size": [2,2,0], "curve": 1},
            PieceName.ROAD_CURVE_RIGHT_2: {**default_config, "id": 4, "size": [2,2,0], "curve": 2, "offset": [1,1,0], "default_rotation_y": 270, "origin_at_end": True},
            PieceName.ROAD_STEP_UP_2: {**default_config, "id": 5, "size": [1,2,0], "slope": 1},
            PieceName.ROAD_STEP_UP_3: {**default_config, "id": 6, "size": [1,3,0], "slope": 1},
            PieceName.ROAD_STEP_UP_1: {**default_config, "id": 7, "slope": 1},
            PieceName.ROAD_STEP_DOWN_2: {**default_config, "id": 5, "size": [1,2,0], "offset": [0,1,-.5], "default_rotation_y": 180, "origin_at_end": True},
            PieceName.ROAD_STEP_DOWN_3: {**default_config, "id": 6, "size": [1,3,0], "offset": [0,2,-0.5], "default_rotation_y": 180, "origin_at_end": True},
            PieceName.ROAD_STEP_DOWN_1: {**default_config, "id": 7, "offset": [0,0,-0.5], "default_rotation_y": 180},
            PieceName.ROAD_SLOPE_UP_TOP_2: {**default_config, "id": 8, "size": [1,2,0], "slope": 2},
            PieceName.ROAD_SLOPE_DOWN_TOP_2: {**default_config, "id": 8, "size": [1,2,0], "offset": [0,1,-1], "default_rotation_y": 180, "origin_at_end": True},
            PieceName.ROAD_SLOPE_DOWN_BOTTOM_2: {**default_config, "id": 9, "size": [1,2,0], "offset": [0,1,-1], "default_rotation_y": 180, "origin_at_end": True},
            PieceName.ROAD_SLOPE_UP_BOTTOM_2: {**default_config, "id": 9, "size": [1,2,0], "slope": 2},
            PieceName.ROAD_SLOPE_UP_FLAT_1: {**default_config, "id": 10, "slope": 2},
            PieceName.ROAD_SLOPE_DOWN_FLAT_1: {**default_config, "id": 10, "offset": [0,0,-1], "default_rotation_y": 180},
            PieceName.ROAD_SLOPE_UP_TOP_1: {**default_config, "id": 12, "slope": 1},
            PieceName.ROAD_SLOPE_DOWN_TOP_1: {**default_config, "id": 12, "offset": [0,0,-.5], "default_rotation_y": 180},
            PieceName.ROAD_SLOPE_UP_BOTTOM_1: {**default_config, "id": 13, "slope": 1},
            PieceName.ROAD_SLOPE_DOWN_BOTTOM_1: {**default_config, "id": 13, "offset": [0,0,-.5], "default_rotation_y": 180},
            PieceName.ROAD_CURVE_LEFT_3: {**default_config, "id": 14, "size": [3,3,0], "curve": 1},
            PieceName.ROAD_CURVE_RIGHT_3: {**default_config, "id": 14, "size": [3,3,0], "curve": 2, "offset": [2,2,0], "default_rotation_y": 270, "origin_at_end": True},
            PieceName.ROAD_CURVE_LEFT_4: {**default_config, "id": 15, "size": [4,4,0], "curve": 1},
            PieceName.ROAD_CURVE_RIGHT_4: {**default_config, "id": 15, "size": [4,4,0], "curve": 2, "offset": [3,3,0], "default_rotation_y": 270, "origin_at_end": True},
            PieceName.ROAD_CHECKPOINT_WITH_ICON_1: {**default_config, "id": 22, "checkpoint": True},
            PieceName.ROAD_SHALLOW_SLOPE_BOTTOM_2: {**default_config, "id": 25, "size": [1,2,0], "offset": [0,1,-0.5], "default_rotation_y": 180, "origin_at_end": True},
            PieceName.ROAD_SHALLOW_SLOPE_TOP_2: {**default_config, "id": 26, "size": [1,2,0], "slope": 1},
            PieceName.ROAD_SHALLOW_SLOPE_UP_FLAT_1: {**default_config, "id": 27, "slope": 1},
            PieceName.ROAD_SHALLOW_SLOPE_DOWN_FLAT_1: {**default_config, "id": 27, "offset": [0,0,-0.5], "default_rotation_y": 180},
        }

        self.config = self.configurations[name]
        self.config.update(overrides)

# Rails 1 or no Rails 0
rails = 0

# TRACK SEQUENCE GOES HERE
track_sequence = [
    ("start_with_icon_1", {}),  # start
    ("booster_1", {"booster_force": 3, "booster_speed": 120}),  # initial booster
    ("flat_road_1", {}),
    ("finish_with_icon_1", {}),  # finish line
]

def calculate_new_position(x: float, y: float, z: float, rotation_y: float, piece: Piece) -> Tuple[float, float, float]:
    # logic omitted for brevity
    return x, y, z

def generate_and_place_track_piece(x: float, y: float, z: float, rotation_y: float, piece: Piece) -> Tuple[str, float, float, float, float]:
    # logic omitted for brevity
    return piece, x, y, z, rotation_y

def write_to_file(track_pieces: list):
    folder_path = os.getenv('APPDATA') + '/Zeepkist/Levels/aichatlevel/'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Output the track pieces
    with open(folder_path + 'aichatlevel.zeeplevel', 'w+') as file:
        print("LevelEditor2,,\n"
            "6,310,-18,359.3311,347.007,0,-12.99295,0.6689512\n"
            "invalid track,8.656,9.443,10.623,0,90", file=file)
        for piece in track_pieces:
            print(piece, file=file)
            print(piece)

def generate_track_piece(piece: Piece, x, y, z, rotation_x, rotation_y, rotation_z, scale_x, scale_y, scale_z,
                         material_numbers, piece_settings):
    return f"{piece.config['id']},{x},{y},{z},{rotation_x},{rotation_y},{rotation_z},{scale_x},{scale_y},{scale_z}," + \
           ",".join(str(x) for x in material_numbers) + "," + ",".join(str(x) for x in piece_settings)

def calculate_new_position(x: float, y: float, z: float, rotation_y: float, piece: Piece) -> Tuple[float, float, float]:
    y += piece.config['slope'] * 8

    if piece.config['origin_at_end']:
        piece.config['size'][0] = piece.config['size'][1] = 1

    if rotation_y == 0:
        z += piece.config['size'][1] * 16
        x += (piece.config['size'][0]-1) *16
    elif rotation_y == 90:
        x += piece.config['size'][1] * 16
        z -= (piece.config['size'][0]-1) *16
    elif rotation_y == 180:
        z -= piece.config['size'][1] * 16
        x -= (piece.config['size'][0]-1) *16
    elif rotation_y == 270:
        x -= piece.config['size'][1] * 16
        z += (piece.config['size'][0]-1) *16

    return x, y, z

def generate_and_place_track_piece(x: float, y: float, z: float, rotation_y: float, piece: Piece) -> Tuple[str, float, float, float, float]:
    rotation_x = rotation_z = 0

    y += piece.config['offset'][2] * 16

    if rotation_y == 0:
        z += piece.config['offset'][1] * 16
        x += piece.config['offset'][0] * 16
    elif rotation_y == 90:
        x += piece.config['offset'][1] * 16
        z -= piece.config['offset'][0] * 16
    elif rotation_y == 180:
        z -= piece.config['offset'][1] * 16
        x -= piece.config['offset'][0] * 16
    elif rotation_y == 270:
        x -= piece.config['offset'][1] * 16
        z += piece.config['offset'][0] * 16

    rotation_y += piece.config['default_rotation_y']
    rotation_y %= 360

    piece_string = generate_track_piece(piece, x, y, z, rotation_x, rotation_y, rotation_z, 1, 1, 1,
                                        [0, 5, 10, 24, 30, 24, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        ([1, rails, rails, 0, 0 ,0 ,0 , piece.config['booster_force'], 0, piece.config['booster_speed'], 0] if piece.config['id'] == 69 else [1, rails, rails, 0, 0 ,0 ,0 , 0, 0, 0, 0]))
    
    if piece.config['curve'] == 1:
        rotation_y -= 90
    if piece.config['curve'] == 2:
        rotation_y -= 180
    if piece.config['curve'] == 0:
        rotation_y -= piece.config['default_rotation_y']

    rotation_y %= 360

    x, y, z = calculate_new_position(x, y, z, rotation_y, piece)
    
    if piece.config['id'] == -1:
        piece_string = "skip"

    return piece_string, x, y, z, rotation_y

def get_piece_name_enum(piece_name_str: str):
    for piece_name in PieceName:
        if piece_name.value == piece_name_str:
            return piece_name
    raise ValueError(f"No PieceName found for '{piece_name_str}'")

# Generate the track pieces
track_pieces = []
x, y, z = 0, 300, 0
rotation_y = 0

for piece_name, overrides in track_sequence:
    piece = Piece(get_piece_name_enum(piece_name), overrides)
    piece_string, x, y, z, rotation_y = generate_and_place_track_piece(x, y, z, rotation_y, piece)
    if piece != "skip":
        track_pieces.append(piece_string)

write_to_file(track_pieces)

for x in PieceName:
    print(x.value)
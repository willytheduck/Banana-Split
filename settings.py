WIDTH, HEIGHT = 1280, 720
FPS = 60

BG = (255, 240, 245)
DIV = (60, 40, 50)
PANEL_LEFT = (255, 228, 238)
PANEL_RIGHT = (228, 240, 255)

SPRITE = 32
SCALE = 2
BANANA_W = SPRITE * SCALE
BANANA_H = SPRITE * SCALE
BANAN_SPEED = 500  # px/sec
P1_COLOR = (255, 214, 64)
P2_COLOR = (255, 170, 64)

DIFF = "normal"
DIFFS = {
    "easy": {"speed": 160, "interval": 1.1, "gross": 0.0, "target": 45, "lives": 5},
    "normal": {"speed": 220, "interval": 0.8, "gross": 0.01, "target": 105, "lives":4},
    "hard": {"speed": 320, "interval": 0.55, "gross":0.10, "target": 210, "lives": 3},
}

FONT_FILE=None

DEBUG = True  # for the red catch box so i can tune
CATCH_INSET = 0.15  # fraction trimmed off each side
CATCH_HEIGHT = 0.5  # catch box height as a fraction of the catch

CATCHER_FILE = "assets/catcher.png"
FLAVOUR_FILES = {
    "orange": "assets/scoop_orange.png",
    "saffron": "assets/scoop_saffron.png",
    "caramel": "assets/scoop_caramel.png",
    "gross": "assets/scoop_gross.png"
}
NORMAL_FLAVOURS = ["orange", "saffron", "caramel"]

TXT_COLOR = (40, 30, 40)

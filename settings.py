WIDTH, HEIGHT = 1280, 720
FPS = 60

BG = (255, 240, 245)
DIV = (60, 40, 50)
PANEL_LEFT = (255, 228, 238)
PANEL_RIGHT = (228, 240, 255)

SPRITE = 32
SCALE = 3
BANANA_W = SPRITE * SCALE
BANANA_H = SPRITE * SCALE
BANANA_SPEED = 500  # px/sec
P1_COLOR = (255, 214, 64)
P2_COLOR = (255, 170, 64)

DIFF = "hard"
DIFFS = {
    "easy": {"speed": 140, "interval": 1.2, "gross": 0.0, "target": 28, "lives": 5},
    "normal": {"speed": 200, "interval": 0.9, "gross": 0.01, "target": 55, "lives":4},
    "hard": {"speed": 260, "interval": 0.75, "gross":0.10, "target": 105, "lives": 3},
}

FONT_FILE=None

DEBUG = False  # for the red catch box so i can tune
CATCH_INSET = 0.05  # fraction trimmed off each side
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

VS_BOT = True
BOT = {
    "easy": {"reaction": 0.5, "error": 64, "speed": 0.75, "avoid_gross": False},
    "normal": {"reaction": 0.2, "error": 18, "speed": 0.90, "avoid_gross": False},
    "hard": {"reaction": 0.10, "error": 12, "speed": 1.0, "avoid_gross": True}
}
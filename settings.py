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

SCOOP_SPEED = 220  # px/sec
SPWN_INTER = 0.9  # secs between scoops

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

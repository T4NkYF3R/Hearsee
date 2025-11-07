from pathlib import Path


# ========== CONFIG ==========
NB_SESSION = 2
NB_IMAGE_SESSION = 5
CSV_FILE = "reponses.csv"


# ========== FILES ==========
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ASSETS = ROOT / "assets"
IMAGE = ASSETS / "image"
MUSIC = ASSETS / "music"
CSV_PATH = DATA / CSV_FILE


# ========== COLORS ==========
BACKGROUND_COLOR = "#F4EDDE"
RESPONSE_BUTTON_COLOR = ["#FF0000", "#FF3300", "#FF6600", "#FF9900", "#FFCC00", "#FFFF00", "#CCFF00", "#99FF00", "#66FF00", "#33FF00", "#00FF00"]
ACTIVE_BG_BUT_COLOR = "black"
ACTIVE_FG_BUT_COLOR = "white"


# ========== FONT ==========
FONT = ("Arial", 20, "bold")


# ========== SIZES ==========
PADX = 5
PADY = 20

MAX_WIDTH_IMAGE = 500
MAX_HEIGHT_IMAGE = 500


# ========== TIMES ==========
NB_SECONDS = 1
NB_MS = 100
SECOND_TO_MS = 1000
AFTER_TIME = NB_SECONDS * SECOND_TO_MS
SLEEP_TIME = NB_MS * 1 / SECOND_TO_MS
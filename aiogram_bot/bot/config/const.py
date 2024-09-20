import zoneinfo
from pathlib import Path

TIME_ZONE = zoneinfo.ZoneInfo("America/Adak")


BASE_DIR = Path(__file__).parent.parent
LOG_DIR = BASE_DIR / "logs"
LOCALES_DIR = BASE_DIR / "locales"
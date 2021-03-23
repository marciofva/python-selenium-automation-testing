import enum
import os


class Path(enum.Enum):
   ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

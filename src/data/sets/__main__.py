from .load import load
from .paths import file_paths as paths

keys = list(paths.keys())
data = load(keys, info=True)

from pathlib import Path

file_name = 'description.txt'

home_path = Path(__file__).parent.resolve()
file_path = home_path / file_name

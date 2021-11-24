from pathlib import Path

data_file = 'data.txt'
data_read_params = dict(encoding='utf-8')

data_file_path = Path(__file__).parent.resolve() / data_file


def main():
    print(
        data_file_path,
        data_file_path.read_text(**data_read_params),
        sep='\n'
    )

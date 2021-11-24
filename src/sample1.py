"""Sample module to use in packaging setup."""

from pathlib import Path

module_file_path = Path(__file__).parent.resolve() / __file__


def main():
    print(module_file_path)


if __name__ == '__main__':
    main()

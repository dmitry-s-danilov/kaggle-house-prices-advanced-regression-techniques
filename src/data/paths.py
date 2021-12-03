from pathlib import Path

file_names = dict(
    train='train.csv',
    test='test.csv',
    submission='sample_submission.csv',
)

home_path = Path(__file__).parent.resolve()
file_paths = {
    file_key: home_path / file_name
    for file_key, file_name in file_names.items()
}

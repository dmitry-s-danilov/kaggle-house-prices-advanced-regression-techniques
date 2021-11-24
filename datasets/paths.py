from pathlib import Path

data_files = dict(
    train='train.csv',
    test='test.csv',
    # submission='sample_submission.csv',
)

data_home_path = Path(__file__).parent.resolve()
data_file_paths = {
    data_key: data_home_path / data_file
    for data_key, data_file in data_files.items()
}

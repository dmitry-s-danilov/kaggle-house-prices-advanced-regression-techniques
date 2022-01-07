from setuptools import setup, find_packages
from pathlib import Path

main_package_name = 'contest'
main_package_dir = 'src'

setup(
    name=main_package_name,
    version='0.0.1',

    description='A house price prediction contest solution',
    long_description=(Path(__file__).parent.resolve() / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',

    url='https://github.com/dmitry-s-danilov/kaggle-house-prices-advanced-regression-techniques',
    project_urls={
        'Contest': 'https://kaggle.com/c/house-prices-advanced-regression-techniques',
        'Source': 'https://github.com/dmitry-s-danilov/kaggle-house-prices-advanced-regression-techniques',
        'Tracker': 'https://github.com/dmitry-s-danilov/kaggle-house-prices-advanced-regression-techniques/issues',
    },

    author='Dmitry S. Danilov',
    author_email='dmitry.s.danilov@gmail.com',

    license='MIT',
    license_files=['LICENSE.txt'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: DataScientists',
        'Topic :: Machine Learning :: Regression Contest',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    keywords='machine-learning, regression-contest, kaggle, python',

    python_requires='>=3.9',
    install_requires=['pandas'],
    extras_require={'exploration': ['matplotlib']},

    package_dir={main_package_name: main_package_dir},
    packages=[
        main_package_name + '.' + sub_package_name
        for sub_package_name in find_packages(where=main_package_dir)
    ],
    package_data={
        main_package_name + '.data.load': [
            'train.csv',
            'test.csv',
            'sample_submission.csv',
        ],
    },
)

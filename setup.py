from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='contest',  # required
    version='0.0.1',  # required

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
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='machine-learning, regression-contest, kaggle, python',

    python_requires='>=3.9',
    install_requires=[
        'pandas',
        'matplotlib',
        # 'scikit-learn',
    ],
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    py_modules=['sample1'],
    packages=(
        find_packages(
            where='src',
            include=['sample2'],
        ) +
        find_packages(
            # where='.',
            include=[
                'sample3',
                # 'datasets',
            ],
        )
    ),  # required
    package_dir={
        '': 'src',
        'sample3': 'sample3',
        # 'datasets': 'datasets',
    },
    package_data={
        'sample2': ['data.txt'],
        'sample3': ['data.txt'],
        # 'datasets': [
        #     'train.csv',
        #     'test.csv',
        #     # 'sample_submission.csv'
        # ],
    },

    data_files=[('sample4_data', ['sample4/data.txt'])],

    entry_points={
        'console_scripts': [
            'sample1=sample1:main',
            'sample2=sample2:main',
            'sample3=sample3:main',
            # 'datasets=datasets:main',
        ],
    },
)

## Python files

### scraper.py
IO scraping helper function and setup
 - imported by: 01_webscraping.ipynb
 - on import:
    - launches a chromedriver
    - prepares for scraping
 - intended exports:
    - `get_results_from_driver()`

### fis_parser.py
Pure functions for parsing a BeautifulSoup()
 - imported by: scraper.py
 - intended exports:
    - `get_FIS_Results( soup )`

### fis_cleaning_functions.py
Pure functions used in cleaning dataframe, prior to EDA
 - imported by: 02_Cleaning_and_EDA.ipynb
 - intended exports: *

## Jupyter Notebooks

### 01_webscraping.ipynb
requires manual interaction (scrolling) with chromedriver
 - saves:
    - (various scraping backups)
    - fis_dataframe.pkl

### 02_cleaning_and_eda.ipynb
 - loads:
    - fis_dataframe.pkl
 - saves:
    - train_df_TIMESTAMP.pkl
    - test_df_TIMESTAMP.pkl

### 03_modelling.ipynb
 - loads:
    - train_df_20180425-1926.pkl
    - test_df_20180425-1926.pkl

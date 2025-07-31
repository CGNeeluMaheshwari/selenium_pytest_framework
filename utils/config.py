# class Config:
#     # URLs
#     BASE_URL = "https://www.saucedemo.com/"
#
#     # Credentials
#     USERNAME = "standard_user"
#     PASSWORD = "secret_sauce"
#
#     # Default Browser Setting
#     BROWSER = "chrome"
#
#     # Default wait time for explicit waits
#     WAIT_TIME = 10


import pandas as pd


class Config:
    BASE_URL = "https://www.saucedemo.com/"
    # Load the Excel file
    df = pd.read_excel("data/users.xlsx", engine='openpyxl')

    BROWSER = "chrome"
    WAIT_TIME = 10

    # Access usernames and passwords
    for index, row in df.iterrows():
        USERNAME = df.loc[0, 'USERNAME']
        PASSWORD = df.loc[0, 'PASSWORD']

        print(f"Username: {USERNAME}, Password: {PASSWORD}")


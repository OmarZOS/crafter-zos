

import pandas as pd

from lib.constants import DATA_INPUT_FILE



def input_data():
    df = pd.read_excel(DATA_INPUT_FILE, engine='openpyxl',header=None)
    return df


import os
from dotenv import load_dotenv

# loading .env variables..
load_dotenv()

DATA_INPUT_FILE = str(os.environ.get("DATA_INPUT_FILE","input.xlsx"))
TARGET_WORD_TEMPLATE = str(os.environ.get("TARGET_WORD_TEMPLATE","Template.docx"))
DESTINATION_SAVE = str(os.environ.get("DESTINATION_SAVE","Destination"))
FILENAME_PATTERN = str(os.environ.get("FILENAME_PATTERN","Product_"))
PATTERNS_TO_CHANGE = (os.environ.get("PATTERNS_TO_CHANGE","1,2")).split(",")




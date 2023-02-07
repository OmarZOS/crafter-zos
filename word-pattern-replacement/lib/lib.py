from lib.constants import *
from lib.input import input_data
from lib.word_Parser import *
import os
import copy

def load_files_through_template():
    
    if not os.path.exists(DESTINATION_SAVE):
        os.makedirs(DESTINATION_SAVE)    
    
    
    # loading excel values
    input = input_data()
    
    # loading word template
    template = load_document(TARGET_WORD_TEMPLATE)
    
    for item in input.iterrows():
        doc = copy.deepcopy(template)
        data = {}
        filename = DESTINATION_SAVE + "/"+FILENAME_PATTERN + str(item[0])+".docx"
        # loading fields for a single file
        for index in item[1].index:
            
            # building the data dictionary
            data[str(PATTERNS_TO_CHANGE[index])]= str(item[1][index])
            
            # avoiding segmentation faults
            if len(PATTERNS_TO_CHANGE) <= index+1:
                break
        
        update_file_through_template(data,doc,filename)


def update_file_through_template(data,doc,filename):
    for key in data:
        doc = replace_in_file(doc,key,data[key])
    save_document(doc,filename)













import pandas as pd

from lib import search_and_replace


df_samples = pd.read_excel(r'Form.docx.xlsx', engine='openpyxl',header=None)


# data = {
#     "2221":"Etwas das du kannst nicht kennen",
#     "2222":"Etwas das du kannst nicht kennen",
#     "2223":"Etwas das du kannst nicht kennen",
#     "2224":"Etwas das du kannst nicht kennen",
#     "2225":"Etwas das du kannst nicht kennen",
#     "2226":"Etwas das du kannst nicht kennen",
#     "2227":"Etwas das du kannst nicht kennen",
#     "2228":"Etwas das du kannst nicht kennen",
#     "2229":"Etwas das du kannst nicht kennen"
# }


for item in df_samples.iterrows():
    

    data = {
        "2221":str( "" if not item[1][0] else item[1][0] ),
        "2222":str( "" if not item[1][1] else item[1][1] ),
        "2223":str( "" if not item[1][2] else item[1][2] ),
        "2224":str( "" if not item[1][3] else item[1][3] ),
        "2225":str( "" if not item[1][4] else item[1][4] ),
        "2226":str( "" if not item[1][5] else item[1][5] ),
        "2227":str( "" if not item[1][6] else item[1][6] ),
        "2228":str( "" if not item[1][7] else item[1][7] ),
        "2229":str( "" if not item[1][8] else item[1][8] ),
        } 

    search_and_replace(data,"template.pptx",str(data["2221"]+" "+data["2222"])+".pptx")

    # print (data)


















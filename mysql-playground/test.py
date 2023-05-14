import os
import mysql.connector



TABLE_NAME = "Documents"
TABLE_FIELDS = "Doc_ID,Doc_Label,Doc_size,Doc_number_of_chunks"




def insert_in_chunks(file_object,doc_id,session, chunk_size=1048576): # 1MB
    counter = 1
    _uuid = str(doc_id)
    print("Inserting chunks...")
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        print(f"Inserting chunk number {counter}...")
        session.execute(_uuid,counter,data)
        counter += 1
        yield data

def insert_doc(_uuid,item,session):
    with open(f"docs/{item}", "rb") as file1:
        # read_content = file1.read()
        
        print(f"{item} ---------------------------------------------------")
        # insert_in_chunks(file1,counter,session,chunk_size=1048576)
        chunk_size=1048576
        counter = 1
        
        print("Inserting chunks...")
        while True:
            data = file1.read(chunk_size)
            if not data:
                break
            print(f"Inserting chunk number {counter}...")
            session.execute(_uuid,counter,data)
            # query = f"INSERT INTO {TABLE_NAME} ({TABLE_FIELDS}) VALUES ( {_uuid}, {counter},{data} )"
            # print(query)
            # session.execute(query)
            
            counter += 1
                # yield data
        file1.close()
        print("Done ---------------------------------------------------")
        
        # print(read_content)
    # print(file.read)
    # print(item)



mydb = mysql.connector.connect(
  host="localhost",
  user="dev_user",
  password="dev_password",
  database= "Archive"
)

session = mydb.cursor()

doc_id = 0

statement = "INSERT INTO "+TABLE_NAME+" ("+TABLE_FIELDS+") VALUES "

# print(f"INSERT INTO {TABLE_NAME} ({TABLE_FIELDS}) VALUES (?, ?)")
for item in os.listdir("docs"):
    doc_id+=1
    values = f"({doc_id},\"{str(item)}\",{100},{1});"
    print(statement+values)
    session.execute(statement+values)
    # for result in session:
    #     print(result)
    mydb.commit()
    # insert_doc(doc_id,item,session)

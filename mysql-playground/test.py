import time
from cassandra.cluster import Cluster
import os
import uuid;



def insert_in_chunks(file_object,doc_id,session, chunk_size=1048576): # 1MB
    counter = 1
    _uuid = str(uuid.uuid4(doc_id))
    print("Inserting chunks...")
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        print(f"Inserting chunk number {counter}...")
        session.execute(_uuid,counter,data)
        counter += 1
        yield data



        
SCYLLA_NODES = ['172.20.0.3',
                '172.20.0.2',
                '172.20.0.4']

SCYLLA_KEYSPACE = "archive"
TABLE_NAME = "DOCUMENTS"
TABLE_FIELDS = "doc_id,chunk_id,document_content"



cluster = Cluster(SCYLLA_NODES)

session = cluster.connect(SCYLLA_KEYSPACE)

doc_id = 0

statement = "INSERT INTO "+TABLE_NAME+" ("+TABLE_FIELDS+") VALUES ( ?, ?, ?)"

session.prepare(statement)
# print(f"INSERT INTO {TABLE_NAME} ({TABLE_FIELDS}) VALUES (?, ?)")
for item in os.listdir("docs"):
    doc_id+=1
    
    with open(f"docs/{item}", "rb") as file1:
        # read_content = file1.read()
        
        print(f"{item} ---------------------------------------------------")
        # insert_in_chunks(file1,counter,session,chunk_size=1048576)
        chunk_size=1048576
        counter = 1
        _uuid = uuid.uuid1(doc_id)
        print(_uuid)
        
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




def write_to_text_file(**kwargs):
    with open('EventRecords.txt','a') as f:
        for key, value in kwargs.items():
            print(key ,":",value)
            f.write(key + ": "+ value+"\n")
        f.write("\n")

            

def get_ids():
    pass 










# format rtmp://127.0.0.1/enclosure/live 

# import pandas as pd
# import numpy as np
# import h5py

def write_to_text_file(**kwargs):
    with open('EventRecords.txt','a') as f:
        for key, value in kwargs.items():
            print(key ,":",value)
            f.write(key + ": "+ value+"\n")
        f.write("\n")

            
# def get_animal_ids_from_file():
#     filename = "1625134431020_000000_R62G35wcage1_0000000000000.hdf5"
#     df = pd.DataFrame(np.array(h5py.File(filename)['subjects']))
#     df.columns = ['animal_ids']


#     return df['animal_ids'].values.tolist()


# import h5py
  












# format rtmp://127.0.0.1/enclosure/live 

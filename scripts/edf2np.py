import pandas as pd
import numpy as np 
import mne 

PATH = '/home/pib3/Projetos/tuh_eeg_epilepsy/'
csv = pd.read_csv(PATH + 'codes/docs/data1_1.csv')
edf_with = csv[csv['epilepsy']==0]
edf_no = csv[csv['epilepsy']==1]
print(edf_no.iloc[0,2])
#raw = mne.io.read_raw_edf(PATH + 'epilepsy'+ edf_no.loc[0,'path'][1:], preload=True,verbose=False)

# shapes1 = []
# for i in range(len(edf_with)):
#     raw = mne.io.read_raw_edf(PATH + 'epilepsy'+ edf_with.loc[i,'path'][1:], preload=True,verbose=False)
#     data = raw.to_data_frame().T
#     print(data.shape[1])
#     shapes1.append(data.shape[1])

shapes2 = []
for i in range(len(edf_no)):
    raw = mne.io.read_raw_edf(PATH + 'epilepsy'+ edf_no.iloc[i,3][1:], preload=True,verbose=False)
    data = raw.to_data_frame().T
    print(data.shape[1])
    shapes2.append(data.shape[1])

# print(shapes1)
# print(shapes2)
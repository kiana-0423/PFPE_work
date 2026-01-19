#Using dpdata for reading CP2K output files;including .ener/.out(or log files,need the printing level Medium or above)/~frc.xyz/~pos.xyz

import dpdata
from ase.io import write

#reading the cp2k output data files
data=dpdata.LabeledSystem('../d4oh_water_sio_o/',cp2k_output_name='packed_water_base_o.out',fmt='cp2kdata/md')

'''
print(data)

#converting to npy data files for deepmd
data.to_deepmd_npy('./02_dp/aimd_single/',fmt='deepmd-npy',set_size=20)
'''



ase_list = data.to_ase_structure() 
write("allegro_dataset.extxyz", ase_list)

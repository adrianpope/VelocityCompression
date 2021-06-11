import sys

import numpy as np
import pandas as pd

def df_add_keys(df):
    ax = df['fof_halo_angmom_x']
    ay = df['fof_halo_angmom_y']
    az = df['fof_halo_angmom_z']
    mag = np.sqrt(ax**2 + ay**2 + az**2)
    dx = ax/mag
    dy = ay/mag
    dz = az/mag
    df['fof_halo_angmom_mag'] = mag
    df['fof_halo_angmom_dx'] = dx
    df['fof_halo_angmom_dy'] = dy
    df['fof_halo_angmom_dz'] = dz
    return df

def df_merge(df1, df1_suffix, df2, df2_suffix):
    merged = pd.DataFrame()
    kl = df1.keys()
    for i in range(len(kl)):
        k = kl[i]
        k1 = k + '_' + df1_suffix
        k2 = k + '_' + df2_suffix
        merged[k1] = df1[k]
        merged[k2] = df2[k]
    return merged

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 7:
        print('USAGE: %s <in1_name> <in1_suffix> <in2_name> <in2_suffix> <out_name> <add_keys>'%argv[0])
        sys.exit(-1)
    in1_name = argv[1]
    in1_suffix = argv[2]
    in2_name = argv[3]
    in2_suffix = argv[4]
    out_name = argv[5]
    add_keys = int(argv[6])
    
    in1 = pd.read_csv(in1_name)
    in2 = pd.read_csv(in2_name)

    if add_keys:
        df_add_keys(in1)
        df_add_keys(in2)

    merged = df_merge(in1, in1_suffix, in2, in2_suffix)
    merged.to_csv(out_name)

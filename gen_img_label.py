import os
from utils.read_from_agrl import read_from_agrl
from utils.split_dataset import split_dataset

casia_base_dir = "./raw/casia"

if __name__ == '__main__':

    # generate label and image from raw agrl dir
    read_from_agrl(os.path.join(casia_base_dir, 'raw_data'))

    # split into train test valid in cv1 folder
    split_dataset(os.path.join(casia_base_dir, "label.txt"))

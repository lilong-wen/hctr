import os
from utils.read_from_agrl import read_from_agrl
from utils.split_dataset import split_dataset
from src.data.reader import Dataset
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, default='casia', required=False)
    args = parser.parse_args()

    raw_path = os.path.join("..", "raw", args.source)

    casia_label_path = os.path.join(raw_path, "label.txt")

    if args.source == 'casia' and not os.path.exists(casia_label_path):

        # generate label and image from raw agrl dir
        read_from_agrl(os.path.join(raw_path, 'raw_data'))
        # split into train test valid in cv1 folder
        split_dataset(os.path.join(raw_path, "label.txt"))

    else:
        pass

    assert os.path.exists(raw_path)
    print(f"##### {args.source} dataset #####")

    ds = Dataset(source = raw_path, name = args.source)
    ds.read_partitions()

    print("Partitions will be preprocessed...")
    ds.preprocess_partitions(input_size=input_size)

    print("Partitions will be saved...")
    os.makedirs(os.path.dirname(source_path), exist_ok=True)

    for i in ds.partitions:
        with h5py.File(source_path, "a") as hf:
            hf.create_dataset(f"{i}/dt", data=ds.dataset[i]['dt'], compression="gzip", compression_opts=9)
            hf.create_dataset(f"{i}/gt", data=ds.dataset[i]['gt'], compression="gzip", compression_opts=9)
            print(f"[OK] {i} partition.")

    print(f"Transformation finished.")

import pandas as pd
import numpy as np
import os

from tsml.datasets import load_from_ts_file

def load_dataset(name, path="./assets/datasets"):
    X_train, y_train = load_from_ts_file(f"{path}/{name}/{name}_TRAIN.ts")
    X_test, y_test = load_from_ts_file(f"{path}/{name}/{name}_TEST.ts")
    y_train = y_train.astype(float)
    y_test = y_test.astype(float)

    X = np.concatenate([X_train, X_test], axis=0)
    y = np.concatenate([y_train, y_test])

    return X, y

def list_datasets(path="./assets/datasets"):
    datasets = os.listdir(path)
    return datasets
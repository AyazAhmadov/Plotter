import numpy as np
import csv

def csv_to_array(filename) -> np.ndarray:
    with open(filename, 'r') as f:
        reader = csv.reader(f)

        vals = []
        for row in reader:
            try:
                vals.append([float(val) for val in row])
            except ValueError:
                continue

    return np.array(vals)
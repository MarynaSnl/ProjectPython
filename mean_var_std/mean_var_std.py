import numpy as np

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.") 
    else:
        tmp_array = np.array(list).reshape(3,3)
        calculations = {'mean': [np.mean(tmp_array, axis = 0).tolist(), np.mean(tmp_array, axis = 1).tolist(), np.mean(tmp_array)],
              'variance': [np.var(tmp_array, axis = 0).tolist(), np.var(tmp_array, axis = 1).tolist(), np.var(tmp_array)],
              'standard deviation': [np.std(tmp_array, axis = 0).tolist(), np.std(tmp_array, axis = 1).tolist(), np.std(tmp_array)],
              'max': [np.max(tmp_array, axis = 0).tolist(), np.max(tmp_array, axis = 1).tolist(), np.max(tmp_array)],
              'min': [np.min(tmp_array, axis = 0).tolist(), np.min(tmp_array, axis = 1).tolist(), np.min(tmp_array)],
              'sum': [np.sum(tmp_array, axis = 0).tolist(), np.sum(tmp_array, axis = 1).tolist(), np.sum(tmp_array)]}

        return calculations
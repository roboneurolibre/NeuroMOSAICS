# +
import scipy.io
import numpy as np
import csv
import pandas as pd

# import data from OSF
from osfclient.api import OSF
import os
from tempfile import NamedTemporaryFile
from scipy.io import loadmat
import numpy as np

def get_data(is_mat, is_macaque, mat, name):
    """
    Processes .mat data based on the input flags and data.

    Args:
        is_mat (bool): Flag indicating if the data is in .mat format.
        is_macaque (bool): Flag indicating if the data corresponds to rats.
        lData (list): List containing loaded .mat data.
        lNames (list): List of names corresponding to the data.

    Returns:
        dict: A dictionary containing all the processed variables.
    """
    if is_mat:

        if is_macaque:
            correspondance = {
                'emgs': 0, 'emgsabr': 1, 'nChan': 2, 'stimProfile': 3, 'stim_channel': 4, 
                'evoked_emg': 5, 'response': 6, 'isvalid': 7, 'sorted_isvalid': 8, 'sorted_resp': 9, 
                'sorted_evoked': 10, 'sampFreqEMG': 11, 'resp_region': 12, 'map': 13, 'ch2xy': 14, 
                'sorted_respMean': 15, 'sorted_respSD': 16
            }
        else:
            correspondance = {
                'emgs': 0, 'emgsabr': 1, 'nChan': 2, 'stimProfile': 3, 'stim_channel': 4, 
                'evoked_emg': 5, 'response': 6, 'isvalid': 7, 'sorted_isvalid': 8, 'sorted_resp': 9, 
                'sorted_respMean': 10, 'sorted_respSD': 11, 'sorted_evoked': 12, 'sampFreqEMG': 13, 
                'resp_region': 14, 'map': 15, 'ch2xy': 16
            }

        data = mat[name][0][0]

        rM = data[correspondance['sorted_resp']]
        nChan = data[correspondance['nChan']][0][0]
        i1, i2, i3 = rM.shape[0], rM.shape[1], rM[0][0].shape[0]
        evoked_emg = np.stack(data[correspondance['evoked_emg']][0], axis=0)
        sorted_resp = np.stack([np.squeeze(rM[i, j]) for i in range(i1) for j in range(i2)], axis=0)
        sorted_resp = sorted_resp.reshape(i1, i2, i3)

        rN = data[correspondance['sorted_isvalid']]
        j1, j2, j3 = rN.shape[0], rN.shape[1], rN[0][0].shape[0]
        sorted_isvalid = np.stack([np.squeeze(rN[i, j]) for i in range(j1) for j in range(j2)], axis=0)
        sorted_isvalid = sorted_isvalid.reshape(j1, j2, j3)

        sorted_respMean = data[correspondance['sorted_respMean']]
        emgs = {
            'emgs': [name[0] for name in data[correspondance['emgs']][0]],
            'emgsabr': [name[0] for name in data[correspondance['emgsabr']][0]]
        }

        ch2xy = data[correspondance['ch2xy']] - 1
        se = data[correspondance['sorted_evoked']]
        i1, i2, i3, i4 = se.shape[0], se.shape[1], se[0][0].shape[0], se[0][0].shape[1]
        sorted_evoked = np.stack([np.squeeze(se[i, j]) for i in range(i1) for j in range(i2)], axis=0)
        sorted_evoked = sorted_evoked.reshape(i1, i2, i3, i4)
        sorted_filtered = sorted_evoked

        stim_channel = data[correspondance['stim_channel']]
        if stim_channel.shape[0] == 1:
            stim_channel = stim_channel[0]

        fs = data[correspondance['sampFreqEMG']][0][0]
        parameters = {'c': nChan, 'j': stim_channel.shape[0]}
        n_muscles = data[correspondance['emgs']].shape[1]
        maps = data[correspondance['map']]
        resp_region = data[correspondance['resp_region']][0]

        stimProfile = data[correspondance['stimProfile']][0]

        return {
        'correspondance': correspondance,
        'rM': rM, 'nChan': nChan, 'evoked_emg': evoked_emg, 'sorted_resp': sorted_resp,
        'rN': rN, 'sorted_isvalid': sorted_isvalid, 'sorted_respMean': sorted_respMean,
        'emgs': emgs, 'ch2xy': ch2xy, 'sorted_evoked': sorted_evoked,
        'sorted_filtered': sorted_filtered, 'stim_channel': stim_channel, 'fs': fs,
        'parameters': parameters, 'n_muscles': n_muscles, 'maps': maps,
        'resp_region': resp_region, 'stimProfile': stimProfile
        }

    ch2xy = mat['ch2xy']
    emgs = mat['emgs'] 
    evoked_emg = mat['evoked_emg'] 
    filtered_emg = mat['filtered_emg'] 
    isvalid =  mat['isvalid']
    maps =  mat['map']
    parameters = mat['parameters']
    resp_region = mat['resp_region']
    response = mat['response']
    fs = mat['sampFreqEMG']
    sorted_evoked = mat['sorted_evoked']
    sorted_filtered = mat['sorted_filtered']
    sorted_resp = mat['sorted_resp']
    sorted_isvalid = mat['sorted_isvalid']
    sorted_respMean = mat['sorted_respMean']
    sorted_respSD = mat['sorted_respSD']
    stim_channel = mat['stim_channel']
    stimProfile = mat['stimProfile'] 
    n_muscles = emgs.shape[0]
    additional_info = mat['additional_info'] 

    return {
        'evoked_emg': evoked_emg, 'filtered_emg':filtered_emg, 'sorted_resp': sorted_resp,
        'sorted_isvalid': sorted_isvalid, 'sorted_respMean': sorted_respMean, 'sorted_respSD': sorted_respSD,
        'emgs': emgs, 'ch2xy': ch2xy, 'sorted_evoked': sorted_evoked,
        'sorted_filtered': sorted_filtered, 'stim_channel': stim_channel, 'fs': fs,
        'parameters': parameters, 'n_muscles': n_muscles, 'maps': maps, 'isvalid':isvalid,
        'resp_region': resp_region, 'stimProfile': stimProfile, 'additional_info':additional_info
    }
# -



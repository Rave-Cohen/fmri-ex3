import os
import numpy as np
import matplotlib.pyplot as plt
import pydicom
import cv2
from scipy.stats import zscore
from scipy.stats import pearsonr
from skimage import exposure

# Define parameters
dicom_fp = ''  # TODO - add file path to DICOM images

nSliceRows = 5
nSliceCols = 6

clim = [200, 1100]
movieFps = 20
plotTrialNo = # choose trial number
axialPlotSliceNo = # an array of [axial slice, saggital slice, coronal slice]
sagittalPlotSliceNo = # choose the correct saggital slice number
coronalPlotSliceNo = # choose the correct coronal slice number
plotSliceCoord = [[70, 45], [70, 37], [62, 54]]

tau = 0.5
n = 3 # choose 3 or 4
hemDelay =  # Hemodynamic delay [sec]
startLen = # rest length
stimLen = # length of each trial
stimOnLen =  # [sec]
expOrder = [1, 3, 1, 2, 3, 2, 1, 1, 1, 3, 2, 1, 3, 3, 1, 2, 1, 2, 3, 2, 2, 3, 3, 2]

corrThresh = 0.3

# 1. DICOM data

# Load DICOM files
filenames = [f for f in os.listdir(dicom_fp) if f.endswith('.dcm')]
dicom_info = pydicom.dcmread(os.path.join(dicom_fp, filenames[0])) # metadata

# Repetition time in seconds
TR =  # in sec

# --- Read all the 180 images into a 3D matrix ---
# Your code goes here

# --- Plot five random images in gray scale ---
# Your code goes here


# --- Set image dimensions ---
# Your code goes here

# --- Convert to 4D ---
# Your code goes here


# --- Plot axial slice movie ---

# Your code goes here



# --- Plot sagittal and coronal cuts ---
# Your code goes here


# 2. Correlation with the stimuli


# --- Create binary stimuli ---
# Your code goes here



# --- Perform correlation analysis for each experimental condition ---
# Your code goes here


# --- Define Hemodynamic Response Function (HRF) ---
# Your code goes here
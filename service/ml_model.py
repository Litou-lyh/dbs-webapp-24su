"""
Global Configuration for ML model
"""

import pickle

############################################################
# Initialize ML Model. Retrieve model and parameters
############################################################
CHECKPOINT_PATH = "checkpoints/insurance_xgb_model.pkl"
with open(CHECKPOINT_PATH, 'rb') as f:
    states = pickle.load(f)
    xgb = states["xgb"]
    scaler = states["scaler"]

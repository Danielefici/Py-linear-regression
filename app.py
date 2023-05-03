import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

import warnings
warnings.filterwarnings('ignore')

def main():
    st.title("Prova")
    load_model=joblib.load('prova_test.pkl')


if __name__=="__main__":
    main()   

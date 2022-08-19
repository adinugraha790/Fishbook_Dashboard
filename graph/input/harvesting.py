from datetime import datetime as dt
import pandas as pd
from flask import request

def read_dataset(dataset, sheet):
    df = pd.read_excel(dataset, sheet)
    return df

def panen_ikan():
    kolam = read_dataset('data/Dummy Dataset Kolam.xlsx', 'Dataset_Kolam_1')

    parsial = int(request.form['parsial'])
    Panen_Date = request.form['panen-date']
    tgl = dt.strptime(Panen_Date, '%Y-%m-%d')
    Pan_Date = dt.date(tgl) # input ke tabel
    ABW = int(request.form['abw'])
    Populasi = int(request.form['populasi'])
    Perc_pop = Populasi / kolam.iloc[0,2]
    
    hasil_panen = [
        parsial, Panen_Date, tgl, Pan_Date,
        ABW, Populasi, Perc_pop
    ]
    return hasil_panen
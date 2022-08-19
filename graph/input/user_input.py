from datetime import datetime as dt
import pandas as pd
from flask import request

def read_dataset(dataset, sheet):
    df = pd.read_excel(dataset, sheet)
    return df

def input_form():
    kolam = read_dataset('data/Dummy Dataset Kolam.xlsx', 'Dataset_Kolam_1')

    inp_Date = request.form['tanggal']
    inp_Datetm = dt.strptime(inp_Date, '%Y-%m-%d')
    inp_Date_ = dt.date(inp_Datetm)
    date_bfr = dt.date(kolam.iloc[-1,0])

    delta = inp_Date_ - date_bfr
    ddays = delta.days # Ini untuk Hari Kultur

    wt = float(request.form['berat-ikan'])
    ct = float(request.form['jumlah-ikan'])
    ABW = wt / ct # input tabel
    ADG = (ABW - kolam.iloc[-1,4]) # input tabel
    mortal = float(request.form['ikan-yang-mati'])
    survived = kolam.iloc[-1,2] - mortal # input tabel
    fd_rate = float(request.form['feeding-rate'])
    pakan = survived * fd_rate * ABW # input tabel
    pH_pagi = float(request.form['ph-pagi'])
    pH_sore = float(request.form['ph-sore'])
    range_pH = pH_sore - pH_pagi
    Nitrit = float(request.form['nitrit'])
    DO_pagi = float(request.form['do-pagi'])
    DO_sore = float(request.form['do-sore'])
    Salin = float(request.form['salinitas'])
    Suhu_pagi = float(request.form['suhu-pagi'])
    Suhu_sore = float(request.form['suhu-sore'])
    Amon = float(request.form['kadar-amonia'])
    Alkali = float(request.form['alkalinitas'])
    Kadar_Mg = float(request.form['kadar-mg'])
    Kadar_Ca = float(request.form['kadar-ca'])
    
    data_awal = [
        inp_Date, inp_Datetm, inp_Date_, date_bfr, # 0, 1, 2, 3
        delta, ddays, wt, ct, # 4, 5, 6, 7
        ABW, ADG, mortal, survived, # 8, 9, 10, 11
        fd_rate, pakan, pH_pagi, pH_sore, # 12, 13, 14, 15
        range_pH, Nitrit, DO_pagi, DO_sore, # 16, 17, 18, 19
        Salin, Suhu_pagi, Suhu_sore, Amon, # 20, 21, 22, 23
        Alkali, Kadar_Mg, Kadar_Ca, # 24, 25, 26
    ]

    inp = {'Hari Kalendar':[inp_Datetm], 'Hari Kalender':[ddays], 'Populasi':[survived], 'Kematian':[mortal], 'ABW (g)':[ABW], 
       'ADG (g)':[ADG], 'Feeding Rate':[fd_rate], 'Pakan':[survived * fd_rate * ABW], 'pH Pagi':[pH_pagi],
       'pH Sore':[pH_sore], 'range pH':[range_pH], 'Nitrit': [Nitrit], 'D.O. pagi':[DO_pagi], 'D.O. sore':[DO_sore], 
       'Salinitas':[Salin], 'Suhu pagi':[Suhu_pagi], 'Suhu sore':[Suhu_sore],
       'Amonia':[Amon], 'Alkalinitas':[Alkali], 'Kadar Mg':[Kadar_Mg], 'Kadar Ca':[Kadar_Ca] }
    inp = pd.DataFrame(inp)
    kolam = kolam.append(inp, ignore_index=True)

    return data_awal

'''
def input_harian():
    kolam = read_dataset('data/Dummy Dataset Kolam.xlsx', 'Dataset_Kolam_1')

    inp_Date = request.form['tanggal']
    inp_Datetm = dt.strptime(inp_Date, '%Y-%m-%d')
    inp_Date_ = dt.date(inp_Datetm)
    date_bfr = dt.date(kolam.iloc[-1,0])

    delta = inp_Date_ - date_bfr
    ddays = delta.days # Ini untuk Hari Kultur

    wt = float(request.form['berat-ikan'])
    ct = float(request.form['jumlah-ikan'])
    ABW = wt / ct # input tabel
    ADG = (ABW - kolam.iloc[-1,4]) # input tabel
    mortal = float(request.form['ikan-yang-mati'])
    survived = kolam.iloc[-1,2] - mortal # input tabel
    fd_rate = float(request.form['feeding-rate'])
    pakan = survived * fd_rate * ABW # input tabel
    pH_pagi = float(request.form['ph-pagi'])
    pH_sore = float(request.form['ph-sore'])
    range_pH = pH_sore - pH_pagi
    Nitrit = float(request.form['nitrit'])
    DO_pagi = float(request.form['do-pagi'])
    DO_sore = float(request.form['do-sore'])
    Salin = float(request.form['salinitas'])
    Suhu_pagi = float(request.form['suhu-pagi'])
    Suhu_sore = float(request.form['suhu-sore'])
    Amon = float(request.form['kadar-amonia'])
    Alkali = float(request.form['alkalinitas'])
    Kadar_Mg = float(request.form['kadar-mg'])
    Kadar_Ca = float(request.form['kadar-ca'])
    
    data_harian = [
        inp_Date, inp_Datetm, inp_Date_, date_bfr, # 0, 1, 2, 3
        delta, ddays, wt, ct, # 4, 5, 6, 7
        ABW, ADG, mortal, survived, # 8, 9, 10, 11
        fd_rate, pakan, pH_pagi, pH_sore, # 12, 13, 14, 15
        range_pH, Nitrit, DO_pagi, DO_sore, # 16, 17, 18, 19
        Salin, Suhu_pagi, Suhu_sore, Amon, # 20, 21, 22, 23
        Alkali, Kadar_Mg, Kadar_Ca, # 24, 25, 26
    ]

    inp = {'Hari Kalendar':[inp_Datetm], 'Hari Kalender':[ddays], 'Populasi':[survived], 'Kematian':[mortal], 'ABW (g)':[ABW], 
       'ADG (g)':[ADG], 'Feeding Rate':[fd_rate], 'Pakan':[survived * fd_rate * ABW], 'pH Pagi':[pH_pagi],
       'pH Sore':[pH_sore], 'range pH':[range_pH], 'Nitrit': [Nitrit], 'D.O. pagi':[DO_pagi], 'D.O. sore':[DO_sore], 
       'Salinitas':[Salin], 'Suhu pagi':[Suhu_pagi], 'Suhu sore':[Suhu_sore],
       'Amonia':[Amon], 'Alkalinitas':[Alkali], 'Kadar Mg':[Kadar_Mg], 'Kadar Ca':[Kadar_Ca] }
    inp = pd.DataFrame(inp)
    kolam = kolam.append(inp, ignore_index=True)

    return data_harian
'''
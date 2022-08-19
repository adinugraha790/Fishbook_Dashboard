import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

def read_dataset(dataset, sheet):
    df = pd.read_excel(dataset, sheet)
    return df

def data_metrics():
    kolam = read_dataset('data/fishbook_dataset.xlsx', 'Dataset_Kolam_1')

    # Metrics FCR
    metrics_fcr = go.Figure(
        go.Indicator(
            mode = "number+delta", # valuenya SUM dari pakan dibagi 10, terus berat akhir dikurangi berat awal dikali populasi awal
            value = round((list(kolam['Pakan'].cumsum())[-1] / 10) / ((kolam.iloc[-1,4] - kolam.iloc[0,4]) * 1000),2),
            # title = {"text": "FCR<br><span style='font-size:25em;color:gray'>"},
            domain = {'x': [0, 1], 'y': [0, 1]}
        )
    )

    layout_metrics_fcr = metrics_fcr.update_layout(
        width=465.5,
        height=450,
        # margin=dict(l=2, r=2, t=2, b=2),
    )

    # Metrics Total Pakan
    a = (list(kolam['Pakan'].cumsum())[-1] - kolam.iloc[-1,7]) / 1000

    metrics_total_pakan = go.Figure(
        go.Indicator(
            mode = "number+delta", # valuenya SUM dari pakan dibagi 10, terus berat akhir dikurangi berat awal dikali populasi awal
            value = round((list(kolam['Pakan'].cumsum())[-1] / 1000),2),
            # title = {"text": "Total Pakan (kg)<br><span style='font-size:25em;color:gray'>"},
            domain = {'x': [0, 1], 'y': [0, 1]},
            delta = {'reference': a, 'relative': True}
        )
    )

    layout_total_pakan = metrics_total_pakan.update_layout(
        width=465.5,
        height=450,
        # margin=dict(l=2, r=2, t=2, b=2),
    )

    return metrics_fcr, layout_metrics_fcr, metrics_total_pakan, layout_total_pakan

def data_pie():
    kolam = read_dataset('data/fishbook_dataset.xlsx', 'Dataset_Kolam_1')

    # Pie Chart Survival Rate
    svr = {'ket': ['Mati', 'Hidup'], 'pop': [kolam.iloc[0,2] - kolam.iloc[-1, 2], kolam.iloc[-1,2]]}
    svr = pd.DataFrame(svr)

    pie_svr = go.Figure(
        data=[go.Pie(labels=svr['ket'], values=svr['pop'], hole=.5)]
    )
    
    layout_pie_svr = pie_svr.update_layout(
        title = "Tingkat Kelangsungan Hidup (%)",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=str(round((kolam.iloc[-1,2]/kolam.iloc[0,2])*100, 2))+'%', x=0.5, y=0.5, font_size=40, showarrow=False)])

    return pie_svr, layout_pie_svr

def grafik():
    kolam = read_dataset('data/fishbook_dataset.xlsx', 'Dataset_Kolam_1')
    metrics = data_metrics()
    pie = data_pie()

    # Grafik pertumbuhan ABW
    grafik_abw = []

    def pred_abw(n):
        y = 0.0016 * (n ** 2) + 0.0261 * (n) - 0.1265
        return y
    
    pred_x = [kolam.iloc[-1,1]+1, kolam.iloc[-1,1]+2, kolam.iloc[-1,1]+2]
    pred_y = []

    for i in pred_x:
        y = pred_abw(i)
        pred_y.append(y)

    grafik_abw.append(
        go.Scatter(
            x=kolam['Hari Kalender'], y=kolam['ABW (g)'],
            mode='lines+markers',
            name='Rataan Berat (gram)',
        )
    )

    grafik_abw.append(
        go.Scatter(
            x=pred_x, y=pred_y,
            mode='markers',
            name='Prediksi',
        )
    )

    layout_abw = dict(
        # title = 'Rataan Berat Harian dan Prediksinya (gram)',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Berat (gr)'),
    )

    # Grafik ADG
    grafik_adg = []

    grafik_adg.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="ADG (g)", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[adg for adg in kolam['ADG (g)']],
            mode = 'lines',
            name = 'Rataan Pertumbuhan Harian (gr)'
        )
    )

    layout_adg = dict(
        title = 'Rataan Pertumbuhan Harian (gr)',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Pertumbuhan (g)'),
    )

    # Grafik Pakan Kumulatif
    grafik_pakan_kumulatif = []

    grafik_pakan_kumulatif.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y=kolam["Pakan"].cumsum(), width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[pakan for pakan in kolam['Pakan'].cumsum()],
            mode = 'lines',
            name = 'Pakan Kumulatif'
        )
    )

    layout_pakan_kumulatif = dict(
        title = 'Pakan Kumulatif',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Pakan Kumulatif (gr)'),
    )

    # Grafik Pakan Harian
    grafik_pakan_harian = []

    grafik_pakan_harian.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Pakan", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[pakan for pakan in kolam['Pakan']],
            mode = 'lines',
            name = 'Pakan Harian'
        )
    )

    layout_pakan_harian = dict(
        title = 'Pakan Harian',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Pakan Harian (gr)'),
    )

    # Grafik pH Pagi
    grafik_ph_pagi = []

    grafik_ph_pagi.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="pH Pagi", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[ph for ph in kolam['pH Pagi']],
            mode = 'lines',
            name = 'pH Pagi'
        )
    )

    layout_ph_pagi = dict(
        title = 'pH Pagi',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='pH Pagi'),
    )

    # Grafik pH Sore
    grafik_ph_sore = []

    grafik_ph_sore.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="pH Sore", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[ph for ph in kolam['pH Sore']],
            mode = 'lines',
            name = 'pH Sore'
        )
    )

    layout_ph_sore = dict(
        title = 'pH Sore',   
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='pH Sore'),
    )

    # Grafik Nitrit
    grafik_nitrit = []

    grafik_nitrit.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Nitrit", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[nitrit for nitrit in kolam['Nitrit']],
            mode = 'lines',
            name = 'Kadar Nitrit'
        )
    )

    layout_nitrit = dict(
        title = 'Kadar Nitrit',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Nitrit (ppm)'),
    )
    
    # Grafik D.O. Pagi
    grafik_do_pagi = []

    grafik_do_pagi.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="D.O. pagi", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[do for do in kolam['D.O. pagi']],
            mode = 'lines',
            name = 'Oksigen Terlarut (DO) Pagi'
        )
    )

    layout_do_pagi = dict(
        title = 'Oksigen Terlarut (DO) Pagi',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='DO pagi (ppm)'),
    )
    
    # Grafik D.O. Sore
    grafik_do_sore = []

    grafik_do_sore.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="D.O. sore", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[do for do in kolam['D.O. sore']],
            mode = 'lines',
            name = 'Oksigen Terlarut (DO) Sore'
        )
    )

    layout_do_sore = dict(
        title = 'Oksigen Terlarut (DO) Sore',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='DO Sore (ppm)'),
    )
    
    # Grafik Salinitas
    grafik_salinitas = []

    grafik_salinitas.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Salinitas", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[salinitas for salinitas in kolam['Salinitas']],
            mode = 'lines',
            name = 'Salinitas'
        )
    )

    layout_salinitas = dict(
        title = 'Salinitas',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Salinitas (ppm)'),
    )
    
    # Grafik Suhu Pagi
    grafik_suhu_pagi = []

    grafik_suhu_pagi.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Suhu pagi", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[suhu for suhu in kolam['Suhu pagi']],
            mode = 'lines',
            name = 'Suhu Pagi'
        )
    )

    layout_suhu_pagi = dict(
        title = 'Suhu Pagi',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Suhu Pagi (C)'),
    )

    # Grafik Suhu Sore
    grafik_suhu_sore = []

    grafik_suhu_sore.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Suhu sore", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[suhu for suhu in kolam['Suhu sore']],
            mode = 'lines',
            name = 'Suhu Sore'
        )
    )

    layout_suhu_sore = dict(
        title = 'Suhu Sore',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Suhu Sore (C)'),
    )
    
    # Grafik Amonia
    grafik_amonia = []

    grafik_amonia.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Amonia", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[amonia for amonia in kolam['Amonia']],
            mode = 'lines',
            name = 'Kadar Amonia'
        )
    )

    layout_amonia = dict(
        title = 'Amonia',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Amonia (ppm)'),
    )

    # Grafik Alkalinitas
    grafik_alkalinitas = []

    grafik_alkalinitas.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Alkalinitas", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[alkalinitas for alkalinitas in kolam['Alkalinitas']],
            mode = 'lines',
            name = 'Alkalinitas'
        )
    )

    layout_alkalinitas = dict(
        title = 'Alkalinitas',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Alkalinitas (ppm)'),
    )
    
    # Grafik Kadar Mg
    grafik_kadar_mg = []

    grafik_kadar_mg.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Kadar Mg", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[kadar for kadar in kolam['Kadar Mg']],
            mode = 'lines',
            name = 'Kadar Magnesium'
        )
    )

    layout_kadar_mg = dict(
        title = 'Kadar Magnesium',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Magnesium (ppm)'),
    )

    # Grafik Kadar Ca
    grafik_kadar_ca = []

    grafik_kadar_ca.append(
        go.Scatter(
            # px.line(kolam, x="Hari Kalender", y="Kadar Ca", width=500, height=400)
            x=[hari for hari in kolam['Hari Kalender']],
            y=[kadar for kadar in kolam['Kadar Ca']],
            mode = 'lines',
            name = 'Kadar Kalsium'
        )
    )

    layout_kadar_ca = dict(
        title = 'Kadar Kalsium',
        xaxis = dict(title='Hari Kultur'),
        yaxis = dict(title='Kalsium (ppm)'),
    )

    grafik = []

    grafik.append(dict(data=metrics[0], layout=metrics[1]))
    grafik.append(dict(data=metrics[2], layout=metrics[3]))
    grafik.append(dict(data=pie[0], layout=pie[1]))
    grafik.append(dict(data=grafik_abw, layout=layout_abw))
    grafik.append(dict(data=grafik_adg, layout=layout_adg))
    grafik.append(dict(data=grafik_pakan_kumulatif, layout=layout_pakan_kumulatif))
    grafik.append(dict(data=grafik_pakan_harian, layout=layout_pakan_harian))
    grafik.append(dict(data=grafik_ph_pagi, layout=layout_ph_pagi))
    grafik.append(dict(data=grafik_ph_sore, layout=layout_ph_sore))
    grafik.append(dict(data=grafik_nitrit, layout=layout_nitrit))
    grafik.append(dict(data=grafik_do_pagi, layout=layout_do_pagi))
    grafik.append(dict(data=grafik_do_sore, layout=layout_do_sore))
    grafik.append(dict(data=grafik_salinitas, layout=layout_salinitas))
    grafik.append(dict(data=grafik_suhu_pagi, layout=layout_suhu_pagi))
    grafik.append(dict(data=grafik_suhu_sore, layout=layout_suhu_sore))
    grafik.append(dict(data=grafik_amonia, layout=layout_amonia))
    grafik.append(dict(data=grafik_alkalinitas, layout=layout_alkalinitas))
    grafik.append(dict(data=grafik_kadar_mg, layout=layout_kadar_mg))
    grafik.append(dict(data=grafik_kadar_ca, layout=layout_kadar_ca))

    return grafik
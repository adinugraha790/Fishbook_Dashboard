from web import app
import json, plotly
from flask import render_template, request
from graph.fishbook import grafik
from graph.input.user_input import input_form

@app.route('/')
def index():
    grafikPlotly = grafik()[:4]
    grafikPlotly.reverse()
    ids = ['figure-{}'.format(i) for i, _ in enumerate(grafikPlotly)]
    grafikJSON = json.dumps(grafikPlotly, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        'index.html', 
        ids=ids, 
        grafikJSON=grafikJSON,
        title="Homepage",
    )


@app.route('/daily-input', methods=['GET', 'POST'])
def daily_input():
    if request.method == 'GET':
        return render_template(
            'forms/daily_input.html',
            title="Daily Input",
            breadcrumb="Daily Input",
        )
    # else:
    #     data = input_awal()
    # return render_template('input/data_awal.html', data=data)

@app.route('/harvesting-fish', methods=['GET', 'POST'])
def harvesting_fish():
    if request.method == 'GET':
        return render_template(
            'forms/harvesting_fish.html',
            title="Harvesting Fish",
            breadcrumb="Harvesting Fish",
        )
#     else:
#         data = panen_ikan()
#     return render_template('data/hasil_panen.html', data=data)

@app.route('/about-data')
def about_data():
    grafikPlotly = grafik()
    ids = ['figure-{}'.format(i) for i, _ in enumerate(grafikPlotly)]
    grafikJSON = json.dumps(grafikPlotly, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        'data/about_data.html', 
        ids=ids, 
        grafikJSON=grafikJSON,
        title="Grafik Populasi dan Lingkungan",
        breadcrumb="Grafik Populasi dan Lingkungan",
    )

@app.route('/data-visualization')
def data_visualization():
    grafikPlotly = grafik()
    ids = ['figure-{}'.format(i) for i, _ in enumerate(grafikPlotly)]
    grafikJSON = json.dumps(grafikPlotly, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(
        'data/data_visualization.html', 
        ids=ids, 
        grafikJSON=grafikJSON,
        title="Data Visualization",
        breadcrumb="Data Visualization",
    )
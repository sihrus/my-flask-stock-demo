from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
import Quandl

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')
  
@app.route('/index', methods=['GET','POST'])
def post_ticker():
  print "MADE IT HERE 3"
  if request.method == 'POST':
    print "MADE IT HERE 4"
    stock = request.form['ticker']
    print stock
    return redirect(url_for('graph'))
  
@app.route('/graph', methods=['GET','POST'])
def graph():
  print "MADE IT HERE 5"
  #df = Quandl.get("WIKI/"+text.upper(),returns="pandas", authtoken="qCQkVD-2dfsdr6Sx4e2b")
  #stock_close = np.array(df[df.index >= '2016-02-20']['Close']) 
  #stock_dates = np.array(df[df.index >= '2016-02-20'].index, dtype=np.datetime64)
  stock_close = np.random.random(50)
  stock_dates = np.arange(50)
  window_size = 30
  window = np.ones(window_size)/float(window_size)
  # create a new plot with a a datetime axis type
  p = figure(width=800, height=350, x_axis_type="datetime")
  # add renderers
  p.line(stock_dates, stock_close, color='navy', legend='Close Price')
  # customize
  p.title = stock + " One-Month Average"
  p.grid.grid_line_alpha=0
  p.xaxis.axis_label = 'Date'
  p.yaxis.axis_label = 'Price'
  p.ygrid.band_fill_color="olive"
  p.ygrid.band_fill_alpha = 0.1
  script, div = components(p)
  return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)

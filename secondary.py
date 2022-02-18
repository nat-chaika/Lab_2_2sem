"""
Main module. Connects twitter2.py and site.html to Map_friends.html
"""
from flask import Flask, redirect, render_template, url_for, request
import twitter2

app = Flask(__name__)
  
@app.route('/', methods = ['POST', 'GET'])
def login():
   """
   Starts the program, gets name from user
   """
   if request.method == 'POST':
      user = request.form['nm']
      if twitter2.do_the_map(user):
         return redirect(url_for('start'))
   else:
      return render_template("site.html")
  
@app.route('/map')
def start():
   """
   Returns the map
   """
   return render_template('Map_friends.html')
if __name__ == '__main__':
   app.run(debug = True)
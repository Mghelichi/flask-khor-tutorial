from flask import Flask, render_template, jsonify

app = Flask(__name__)

FLASKKHORS = [
  {
    'id' : 1,
    'title' : "Mohammad",
    'location' : 'Tehran, Iran',
    'price' : '1000$'
  } ,
  {
    'id' : 2,
    'title' : "Saghar",
    'location' : 'Boushehr, Iran',
    'price' : '1$'
  },
  {
    'id' : 3,
    'title' : "Arsham the idiot",
    'location' : 'Kabol, Afghanistan',
    'price' : 'Free'
  },
  {
    'id' : 4,
    'title' : "HosseinBegh",
    'location' : 'Unknown',
    'price' : 'Not For sale'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html', flasks=FLASKKHORS,
                        company_name='Famire')

@app.route("/flasks")
def list_flasks():
  return jsonify(FLASKKHORS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
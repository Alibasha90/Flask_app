from flask import Flask,render_template,request
import sqlite3
import plotly.express as px
import pandas as pd

app = Flask(__name__)
# ============================================== Home page AND SEARCH PAGE==============================================git
@app.route('/',methods=["GET","POST"])
def search():
    if request.method == 'GET':
        SENSOR_ID = request.args.get('SENSOR_ID')
        LOCATION = request.args.get('LOCATION')

        conn=sqlite3.connect("demo.db")     # connecting to the database file
        cur = conn.cursor()                 # creating cursor object for go through the queries

        cur.execute("SELECT * FROM demo WHERE SENSOR_ID= ? AND LOCATION= ?",(SENSOR_ID,LOCATION))
      #cur.execute("SELECT * FROM demo")
        row = cur.fetchall()

        conn.close()
    return render_template("main.html",rows=row)

# ============================================= INSERT DATA PAGE =======================================================

@app.route("/insertdatabase",methods=["GET","POST"])
def insertdatabase():
    global conn
    try:
       if request.method == "POST":
          sensor_id = request.form["SENSOR_ID"]
          loc = request.form["LOCATION"]
          instal_date = request.form["INSTALLATION_DATE"]
          oil_clr = request.form["OIL_COLOR"]
          transformer_clr = request.form["TRANSFORMER_COLOR"]

          print(sensor_id)

          conn = sqlite3.connect("demo.db")
          cur = conn.cursor()  # creating cursor object for go through the queries

          cur.execute(
             "INSERT into demo(SENSOR_ID,LOCATION,INSTALLATION_DATE,OIL_COLOR,TRANSFORMER_OIL_COLOR) values(?,?,?,?,?)",
             (sensor_id, loc, instal_date, oil_clr, transformer_clr))

          conn.commit()

    except:
        conn.close()

    return render_template("insert.html")

# ======================================================= DELETE PAGE ==================================================

@app.route('/deletedatabase',methods=["GET","POST"])
def deletedatabase():
    global conn
    try:
        if request.method == 'POST':
            SENSOR_ID = request.form["SENSOR_ID"]
            LOCATION = request.form["LOCATION"]

            conn=sqlite3.connect("demo.db")   # connecting to the database file
            cur = conn.cursor()                 # creating cursor object for go through the queries
            cur.execute("DELETE  from demo where SENSOR_ID= ? AND LOCATION= ?",(SENSOR_ID,LOCATION))
            conn.commit()
    except:
        conn.close()

    return render_template("delete.html")


@app.route('/veiwdata')
def veiwdata():
    conn = sqlite3.connect("demo.db")  # connecting to the database file
    cur = conn.cursor()
    cur.execute("SELECT * FROM demo")
    row = cur.fetchall()
    conn.close()
    return render_template("veiwdata.html", rows=row)


@app.route('/graph')
def graph():
    df = pd.read_csv("sensor.csv")

    fig = px.scatter_polar(df, r="distance", theta="direction",
                           color='Oil_color', symbol="Location",
                           title="Sensor Data Visualization",
                           color_discrete_sequence=px.colors.sequential.Plasma_r)

    fig.show()
    return render_template("main.html")

@app.route('/back')
def back():
    return render_template("main.html")


# ====================================================== Main function =====================================================
if __name__ == '__main__':
    app.run(debug=True,port=8001)

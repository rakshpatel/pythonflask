from flask import Flask
from flask_restful import Resource, Api, reqparse
import sqlite3

app = Flask(__name__)
app.secret_key="polestartships"
api = Api(app)
DATABASE_PATH="shipsdata.db"
conn = sqlite3.connect(DATABASE_PATH)

class Ships(Resource):
    def get(self):
        conn = sqlite3.connect(DATABASE_PATH)
        query = "SELECT imo, shipname FROM SHIPS "
        curs = conn.cursor()
        shipdata = []
        for ships in curs.execute(query):
            shipdata.append({"imo": ships[0], "name": ships[1]})
        conn.close()
        return {"ship": shipdata}


class ShipsPosition(Resource):
    def get(self, imo):
        conn = sqlite3.connect(DATABASE_PATH)
        query = "SELECT imo, datetime, latitude, longitude FROM SHIPSPOSITION WHERE imo={imo} ORDER BY 2 ".format(imo=imo)
        curs = conn.cursor()
        shipspositions = []
        for shipsposition in curs.execute(query):
            shipspositions.append({"datetime": shipsposition[1], "latitude": shipsposition[2], "longitude": shipsposition[3]})
        conn.close()
        return {"ship": {"imo": imo, "positions": shipspositions}}

@app.route("/")
def index():
    return "Hello World"

api.add_resource(Ships, "/api/ships/")
api.add_resource(ShipsPosition, "/api/positions/<int:imo>")

if __name__ == "__main__":
    app.run(debug=True)
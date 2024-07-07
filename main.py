import json
from models.User import User as userModel
from functionsDB import usersFunctionsDB
from algorithm import mainAlgorithm

from flask import Flask, request
from flask_cors import CORS, cross_origin

# react connection
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins}": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'


# הכנסת משתמש חדש לSQL
@app.route("/sign_up", methods=["POST"])
@cross_origin("*")
def sign_up():
    data_user = json.loads(request.data)
    res = usersFunctionsDB.create_a_user(userModel(data_user["mail"], data_user["pass"]))
    return {"mail": data_user["mail"], "password": data_user["pass"]}, res

# התחברות למערכת
@app.route("/log_in", methods=["POST"])
@cross_origin("*")
def log_in():
    data_user = json.loads(request.data)
    user_email = data_user["mail"]
    user_password = data_user["pass"]
    res = usersFunctionsDB.sign_in(userModel(email=user_email, password=user_password))
    if res != None:
        if res.password == user_password:
            return {"email": res.email, "password": res.password, "id": res.id}
        else:
            return {"massage": "The password is not match"}
    else:
        return {"massage": "user not find"}


# כיסוי מבנה עם מצלמות
@app.route("/cover_apartment_by_cameras", methods=["POST"])
@cross_origin("*")
def cover_apartment_by_cameras():
    input_click = json.loads(request.data)
    apartment = input_click["rooms"]
    resultes = []
    for room in apartment:
        list_coor = []
        for coordinates in room:
            print(coordinates)
            list_coor.append((coordinates["x"], coordinates["y"]))
        print(list_coor)
        result = mainAlgorithm.main(list_coor)
        if result != None:
            resultes.append(result)
        print(result)
    print(resultes)
    return resultes


if __name__ == "__main__":
    app.run(debug=True)

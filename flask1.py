from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

#Loads squat, bench, deadlift data from JSON File
with open("sbd.json") as l:
    sbd = json.load(l)
    
#Defines homepage route.
#Renders lifts.html and passes sbd dictionary to HTML
@app.route("/")
def home():
    return render_template("lifts.html", sbd = sbd)

#Defines API route that returns all lifter stats
#as a .json file
@app.route("/api/lifts")
def get_all_lifts():
    return jsonify(sbd)

#Defines a dynamic route depending on the user's name
@app.route("/api/lifts/<name>")
def get_user_lifts(name):
    #checks if user is found
    user = sbd.get(name.lower())
    if (user):
        return jsonify({name: user})
    else:
        return jsonify({"error" : "User not found"}), 404

#Runs the Flask server on all interfaces (0.0.0.0)
#(accessible by Kubernetes)
if (__name__ == "__main__"):
    app.run(host = "0.0.0.0", port = 4000)

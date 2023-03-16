from flask import Flask, jsonify, request

app = Flask (__name__)

contacts = [
    {
        'id': 1,
        'Name': 'Big Man',
        'Contact': '8829017694'
    },
    {
        'id': 2,
        'Name': '90 Degrees',
        'Contact': '8887890254'
    }
]

@app.route("/")
def homePage():
    return "Welcome to the contacts api"

@app.route("/add-data", methods=["POST"])
def addContact():

    if not request.json:
        return jsonify({
            "status":"error",
            "message": "no json data identified!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', "")
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully :)"
    })


@app.route("/get-data")
def getContact():
    return jsonify({
        "data" : contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)

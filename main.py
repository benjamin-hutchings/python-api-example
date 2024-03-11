from flask import Flask, request, jsonify

# Test using Postman - https://web.postman.co/ (Download the desktop agent to test local host)
# send correct request type in JSON format

app = Flask(__name__)

# @app.route("/") # decorator defines root
# def home():
#     return "Home"

@app.route("/get-user/<user_id>") # decorator defines root, "GET" by default so not specified
def get_user(user_id):
    user_data = {
        "user_id":user_id,
        "name": "John Doe",
        "email": "johndoe@emample.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200 # jsonify json dictionary for python, 200 is default code for success


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
import json
from flask import Flask, jsonify, request, send_file    
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)

testuserPlJson = []

@app.route('/playlist/testuser')
@cross_origin()
def playlist():
    return jsonify(testuserPlJson)

@app.route('/playlist/create/testuser', methods=['POST'])
@cross_origin()
def createPlaylist():
    if request.method == 'POST':
        req = request.get_json()
        testuserPlJson.append(req)
        return "playlist added"
    else:
        return "method not supported"

@app.route('/playlist/delete/testuser', methods=['POST'])
@cross_origin()
def deletePlaylist():
    if request.method == 'POST':
        testuserPlJson.clear()
        return "playlist deleted"
    else:
        return "method not supported"



@app.route('/playlist/secret')
@cross_origin()
def secretPlaylist():
    return jsonify(
        {"title": "Secret", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "des": "This playlist is made with love. It contains my all time favorite songs and albums"}
        )   

@app.route('/playlist/cool')
@cross_origin()
def coolPlaylist():
    return jsonify(
        {"title": "Cool", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "des": "This is a cool playlist"}
        )         

@app.route('/playlist/secret/songs')
@cross_origin()
def secretPlaylistSongs():
    return jsonify(
        [
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200}
        ]
    )

@app.route('/playlist/cool/songs')
@cross_origin()
def coolPlaylisSongs():
    return jsonify(
        [
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "True Love", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove", "album": "True Love is the only thing i want", "duration": 200},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143},
            {"title": "Intro", "creator": "The XX", "thumbnailUrl": "thumbnails/xx", "album": "Xx", "duration": 143}
        ]
    )
    
@app.route('/playlist/popular')
@cross_origin()
def popPlaylist():
    return jsonify(
        [
            {"title": "Secret", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove"},
            {"title": "True Love is the only thing i want", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove"},
            {"title": "True Love is the only thing i want", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove"},
            {"title": "Cool", "creator": "The XX", "thumbnailUrl": "thumbnails/xx"},
            {"title": "True Love is the only thing i want", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove"},
            {"title": "True Love is the only thing i want", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove"},
            {"title": "True Love is the only thing i want", "creator": "Kendrick Lamar", "thumbnailUrl": "thumbnails/truelove"}
        ]
    )

@app.route('/thumbnails/truelove')
@cross_origin()
def getThumbnailLove():
	return send_file("thumbnails/truelove.jpg",as_attachment=True)    

@app.route('/thumbnails/xx')
@cross_origin()
def getThumbnailX():
	return send_file("thumbnails/XX.svg",as_attachment=True)    

@app.route('/music/testuser')
@cross_origin()
def music():
    return jsonify(
        [
            {"title": "My Heart Will Go On", "Artist": "Celine Dion"},
            {"title": "Confusion", "Artist": "New Order"},
            {"title": "All My Love", "Artist": "Rocazino"}
        ]
    )

@app.route('/music/Confusion')
@cross_origin()
def search():
	return jsonify(
        [
            {"title": "Confusion", "Artist": "New Order"},
        ]
    )
    	
@app.route('/mp3/Confusion')
@cross_origin()
def getSong():
	return send_file("Music/Confusion.mp3",as_attachment=True)

@app.route('/login/', methods=['GET', 'POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        req = request.get_json()
        email = req['email']
        passwd = req['passwd']
        if email == "admin":
            if passwd == "admin":
                return "200"
        else:
            return "Wrong password or username"
    else:
        return "No"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify, request, send_from_directory
from urllib.error import HTTPError
from pytube import YouTube


app = Flask(__name__)
@app.route("/")
def hello_world():
    response = {'message': 'welcome to jontonios app', 'status':True}
    return jsonify(response)

@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory('uploads', filename, as_attachment=True)

@app.route("/download-mp3", methods=['POST'])
def donwloadMusic():
    try:
        # data convert to json
        data = request.json
        # get data url
        url = data['url']
        # progress youtube url
        yt = YouTube(url)
        # stract only mp3
        video = yt.streams.filter(only_audio=True).first()
        # name file
        name = str(video.title).lower().replace(' ','-') + '.mp3'
        # download the file
        video.download(output_path='uploads', filename=name)
        # response data
        response = {
            'message': 'welcome to jontonios app - mp3', 
            'status':True, 
            'error':False, 
            "data":{'download-link':request.host_url+'uploads/' + name}
        }
        return jsonify(response)
    except HTTPError as e:
        return jsonify({'message': 'Ocurrio un error al procesar video: {}'.format(e),'error':True, 'status':False})


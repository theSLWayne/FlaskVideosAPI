from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

put_args = reqparse.RequestParser()
put_args.add_argument('name', type = str, required = True, help = 'Name of the video is required')
put_args.add_argument('views', type = int, help = 'Number of views')
put_args.add_argument('uploader', type = str, required = True, help = 'Uploader of the video is required')
put_args.add_argument('likes', type = int, help = 'Number of likes')

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, '/video/<int:video_id>')

if __name__ == '__main__':
    app.run(debug = True)
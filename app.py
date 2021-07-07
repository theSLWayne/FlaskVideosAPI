from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videodatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    uploader = db.Column(db.String(20), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<Video \nName: {} \nUploader: {} \nViews: {} \nLikes: {}\n>'.format(self.name, self.uploader, self.views, self.likes)

# Database creation - Only need to run it after models are created.
db.create_all()

put_args = reqparse.RequestParser()
put_args.add_argument('name', type = str, required = True, help = 'Name of the video is required')
put_args.add_argument('views', type = int, required = True, help = 'Number of views')
put_args.add_argument('uploader', type = str, required = True, help = 'Uploader of the video is required')
put_args.add_argument('likes', type = int, required = True, help = 'Number of likes')

resource_fields = {
    'id': fields.String,
    'name': fields.String,
    'uploader': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = 'Video for id:{} does not exist.'.format(video_id))
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if result:
            abort(409, message = 'A video from that ID already exists.')
        video = VideoModel(id = video_id, name = args['name'], uploader = args['uploader'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    '''def delete(self, video_id):
        
        del videos[video_id]
        return '', 204'''

class Videos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        results = VideoModel.query.order_by(VideoModel.id).all()
        return results, 200

    @marshal_with(resource_fields)
    def post(self):
        args = put_args.parse_args()
        video = VideoModel(name = args['name'], uploader = args['uploader'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

api.add_resource(Video, '/video/<int:video_id>')
api.add_resource(Videos, '/videos')

if __name__ == '__main__':
    app.run(debug = True)
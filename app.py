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

class UploaderModel(db.Model):
    uploader_id = db.Column(db.Integer, primary_key = True)
    uploader_name = db.Column(db.String(20), nullable = False)
    uploader_videos = db.Column(db.String(400), nullable = False)
    uploader_email = db.Column(db.String(15), nullable = False)
    uploader_password = db.Column(db.String(15), nullable = False)

    def __repr__(self):
        return '<Uploader \nName: {} \nEmail: {}\n>'.format(self.uploader_name, self.uploader_email)

class UserModel(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(20), nullable = False)
    user_email = db.Column(db.String(15), nullable = False)
    user_password = db.Column(db.String(15), nullable = False)
    user_watched_videos = db.Column(db.String(400), nullable = False)

    def __repr__(self):
        return '<User \nName: {} \nEmail: {}\n>'.format(self.user_name, self.user_email)

# Database creation - Only need to run it after models are created.
db.create_all()

video_post_args = reqparse.RequestParser()
video_post_args.add_argument('name', type = str, required = True, help = 'Name of the video is required')
video_post_args.add_argument('views', type = int, required = True, help = 'Number of views')
video_post_args.add_argument('uploader', type = str, required = True, help = 'Uploader of the video is required')
video_post_args.add_argument('likes', type = int, required = True, help = 'Number of likes')

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type = str, help = 'Name of the video')
video_put_args.add_argument('views', type = int, help = 'Number of views')
video_put_args.add_argument('uploader', type = str, help = 'Uploader of the video')
video_put_args.add_argument('likes', type = int, help = 'Number of likes')

uploader_put_args = reqparse.RequestParser()
uploader_put_args.add_argument('uploader_name', type = str, help = 'Name of the uploader')
uploader_put_args.add_argument('uploader_email', type = str, help = 'Email of the uploader')
uploader_put_args.add_argument('uploader_password', type = str, help = 'Uploader password')

user_put_args = reqparse.RequestParser()
user_put_args.add_argument('user_name', type = str, help = 'Name of the user')
user_put_args.add_argument('user_email', type = str, help = 'Email of the uploader')
user_put_args.add_argument('user_password',type = str, help = 'Password of the uploader')

resource_fields_video = {
    'id': fields.String,
    'name': fields.String,
    'uploader': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

resource_fields_uploader = {
    'uploader_id': fields.String,
    'uploader_name': fields.String,
    'uploader_videos': fields.String,
    'uploader_email': fields.String,
    'uploader_password': fields.String
}

resource_fields_user = {
    'user_id': fields.String,
    'user_name': fields.String,
    'user_emali': fields.String,
    'user_password': fields.String,
    'user_watched_videos': fields.String
}

class Video(Resource):
    @marshal_with(resource_fields_video)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = 'Video for id:{} does not exist.'.format(video_id))
        result.views += 1
        db.session.commit()
        return result

    @marshal_with(resource_fields_video)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = 'Video for id:{} does not exist.'.format(video_id))
        if args['name'] is not None:
            result.name = args['name']
        if args['views'] is not None:
            result.views = args['views']
        if args['uploader'] is not None:
            result.uploader = args['uploader']
        if args['likes'] is not None:
            result.likes = args['likes']
        db.session.commit()
        return result, 201

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message = 'Video for id:{} does not exist.'.format(video_id))
        db.session.delete(result)
        db.session.commit()
        return '', 204

class Videos(Resource):
    @marshal_with(resource_fields_video)
    def get(self):
        results = VideoModel.query.order_by(VideoModel.id).all()
        return results, 200

    @marshal_with(resource_fields_video)
    def post(self):
        args = video_post_args.parse_args()
        video = VideoModel(name = args['name'], uploader = args['uploader'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

class Uploader(Resource):
    @marshal_with(resource_fields_uploader)
    def get(self, uploader_id):
        result = UploaderModel.query.filter_by(id = uploader_id).first()
        if not result:
            abort(404, 'Uploader {} does not exist'.format(uploader_id))
        return result

    @marshal_with(resource_fields_uploader)
    def put(self, uploader_id):
        args = uploader_put_args.parse_args()
        result = UploaderModel.query.filter_by(id = uploader_id).first()
        if not result:
            abort(404, 'Uploader {} does not exist'. format(uploader_id))
        if args['uploader_name']:
            result.uploader_name = args['uploader_name']
        if args['uploader_email']:
            result.uploader_email = args['uploader_email']
        if args['uploader_password']:
            result.uploader_passord = args['uploader_password']
        db.session.commit()
        return result

    def delete(self, uploader_id):
        result = UploaderModel.query.filter_by(id = uploader_id).first()
        if not result:
            abort(404, 'Uploader {} does not exist'.format(uploader_id))
        db.session.delete(result)
        db.session.commit()
        return '', 204

class User(Resource):
    @marshal_with(resource_fields_user)
    def get(self, user_id):
        result = UserModel.query.filter_by(id = user_id).first()
        if not result:
            abort(404, 'User {} does not exist'.format(user_id))
        return result

    @marshal_with(resource_fields_user)
    def put(self, user_id):
        args = user_put_args.parse_args()
        result = UserModel.query.filter_by(id = user_id).first()
        if not result:
            abort(404, 'User {} does not exist'. format(user_id))
        if args['user_name']:
            result.user_name = args['user_name']
        if args['user_email']:
            result.user_email = args['user_email']
        if args['user_password']:
            result.user_passord = args['user_password']
        db.session.commit()
        return result

    def delete(self, user_id):
        result = UserModel.query.filter_by(id = user_id).first()
        if not result:
            abort(404, 'User {} does not exist'.format(user_id))
        db.session.delete(result)
        db.session.commit()
        return '', 204    

api.add_resource(Video, '/video/<int:video_id>')
api.add_resource(Videos, '/videos')
api.add_resource(Uploader, '/uploader/<int:uploader_id>')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug = True)
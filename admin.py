from flask import Flask, request, jsonify
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict, dict_to_model
import json

app = Flask(__name__)

# Connect to a MySQL database on network.
db = MySQLDatabase('trainticket', user='root', password='', )


# Models
class User(Model):
    id = PrimaryKeyField()
    name = CharField()
    number = IntegerField()
    address = CharField()
    password = CharField()
    createdAt = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Post(Model):
    id = PrimaryKeyField()
    trainName = CharField()
    journeyTime = TimeField()
    journeyDate = DateField()
    fromPlace = CharField()
    toPlace = CharField()
    noOfSeats = CharField()
    postedBy = ForeignKeyField(User, backref='posts')
    postedDate = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


db.connect()

db.create_tables([User, Post])


@app.route('/')
def home():
    return "Hello"


@app.route('/create-user', methods=['POST'])
def createUser():
    name = request.form.get('name')
    number = request.form.get('number')
    password = request.form.get('password')
    address = request.form.get('address')

    newUser = User(name=name, number=number, password=password, address=address)
    newUser.save()

    return jsonify({"response": "success"})


@app.route('/login', methods=['POST'])
def login():
    number = request.form.get('number')
    password = request.form.get('password')

    try:
        user = User.get(User.number == number, User.password == password)
        return jsonify(model_to_dict(user))
    except:
        return "failed"


@app.route('/post-ticket', methods=['POST'])
def postTicket():
    trainName = request.form.get('trainname')
    journeyTime = request.form.get('journeytime')
    journeyDate = request.form.get('journeydate')
    fromPlace = request.form.get('fromplace')
    toPlace = request.form.get('toplace')
    noOfSeats = request.form.get('noofseats')
    postedUserId = request.form.get('userid')
    postUser = User.get(User.id == postedUserId)
    postedBy = postUser

    ticket = Post(trainName=trainName, journeyTime=journeyTime, journeyDate=journeyDate, fromPlace=fromPlace,
                  toPlace=toPlace, noOfSeats=noOfSeats, postedBy=postedBy)
    ticket.save()

    return "success"


@app.route('/getposts')
def getAllPosts():
    posts = Post.select()
    all_posts = []

    for post in posts:
        all_posts.append(model_to_dict(post))
    return json.dumps(all_posts, default=str)


@app.route('/getposts/<userid>')
def getPosts(userid):
    posts = Post.select().where(Post.postedBy == userid)
    all_posts = []

    for post in posts:
        all_posts.append(model_to_dict(post))
    return json.dumps(all_posts, default=str)



if __name__ == "__main__":
    app.run(port=5003)

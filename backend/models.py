from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    img_url = db.Column(db.String(200), nullable=True)
    role = db.Column(db.String(50), nullable=False, default="student")

    def set_password(self, password):
        self.password_hash =generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
    
    def to_json(self):
        img_url = self.img_url
        if img_url and not (img_url.startswith('/') or img_url.startswith('http')):
            img_url = f"/{img_url}"
        return {
        "id": self.id,
        "user_Name": self.username,
        "email": self.email,
        "imgUrl": self.img_url if self.img_url else None,
        "user_type": self.role  # You might want to add a role field to your Users model
    }

    
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    video_url = db.Column(db.String(200), nullable=False)
    thumbnail = db.Column(db.String(200), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    thumbnail = db.Column(db.String(200), nullable=False)
    Videos = db.relationship('Video', backref='playlist', lazy=True)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    img_url = db.Column(db.String(200), nullable=True)

    user = db.relationship('Users', backref='comments') # backref will create a new column in the class Users named comments
    video = db.relationship('Video', backref='comments') # backref will create a new column in the class Video named comments

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)

    user = db.relationship('Users', backref='likes') 
    video = db.relationship('Video', backref='likes') 

class SavedVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('Users', backref='saved_videos')
    video = db.relationship('Video', backref='saved_by_users')

# Teacher Section
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    bio = db.Column(db.String(500), nullable=True)
    subject = db.Column(db.String(100), nullable=True)
    img_url = db.Column(db.String(200), nullable=True)
    role = db.Column(db.String(50), nullable=False, default="teacher")

    
    # Data into json file
    def to_json(self):

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "profile_picture": self.profile_picture,
            "bio": self.bio,
            "subject": self.subject,
            "imgUrl": self.img_url,
        } 

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True , nullable=False)
    number = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('Users', backref='contact')

def init_db():
    if Playlist.query.filter_by(title="Complete HTML Tutorial").first() is None:
        # ... Add HTML videos ...
        playlist_html = Playlist(title= "Complete HTML Tutorial", thumbnail="static/imgs/Html/thumb-1.png")
        video1_html = Video(
                    title = "Complete HTML Tutorial (Part 01)",
                    description = "Introduction and What I Need To Learn",
                    video_url = "static/videos/Html/Html_v1.mp4",
                    thumbnail = "static/imgs/Html/html-1.png",
                    playlist=playlist_html
        )
        video2_html = Video(
                    title = "Complete HTML Tutorial (Part 02)",
                    description = "Elements And Browser",
                    video_url = "static/videos/Html/Html_v2.mp4", 
                    thumbnail = "static/imgs/Html/html-2.png",
                    playlist=playlist_html
        )
        video3_html = Video(
                    title = "Complete HTML Tutorial (Part 03)",
                    description = "First Project And First Page",
                    video_url = "static/videos/Html/Html_v3.mp4", 
                    thumbnail = "static/imgs/Html/html-3.png",
                    playlist=playlist_html
        )
        video4_html = Video(
                    title = "Complete HTML Tutorial (Part 04)",
                    description = "Head And Nested Elements",
                    video_url = "static/videos/Html/Html_v4.mp4", 
                    thumbnail = "static/imgs/Html/html-4.png",
                    playlist=playlist_html
        )
        video5_html = Video(
                    title = "Complete HTML Tutorial (Part 05)",
                    description = "Comments And Use Cases",
                    video_url = "static/videos/Html/Html_v5.mp4", 
                    thumbnail = "static/imgs/Html/html-5.png",
                    playlist=playlist_html
        )
        video6_html = Video(
                    title = "Complete HTML Tutorial (Part 06)",
                    description = "Doctype And Standard And Quirks Mode",
                    video_url = "static/videos/Html/Html_v6.mp4", 
                    thumbnail = "static/imgs/Html/html-6.png",
                    playlist=playlist_html
        )
        db.session.add(playlist_html)
        db.session.add_all([video1_html, video2_html, video3_html, video4_html, video5_html, video6_html])
        db.session.commit()

    # Initialize CSS Playlist
    if Playlist.query.filter_by(title="Complete CSS Tutorial").first() is None:
        playlist_CSS = Playlist(title= "Complete CSS Tutorial", thumbnail= "static/imgs/CSS/thumb-2.png")
        # ... Add CSS videos ...
        video1_CSS = Video(
                    title = "Complete CSS Tutorial (Part 01)",
                    description = " Introduction And What I Need To Learn",
                    video_url = "static/videos/CSS/CSS_v1.mp4.mp4", 
                    thumbnail = "static/imgs/CSS/post-2-1.png",# missed
                    playlist=playlist_CSS
        )
        video2_CSS = Video(
                    title = "Complete CSS Tutorial (Part 02)",
                    description = "Your First Project And Syntax",
                    video_url = "static/videos/CSS/CSS_v2.mp4.mp4", 
                    thumbnail = "static/imgs/CSS/post-2-2.png",
                    playlist=playlist_CSS
        )
        video3_CSS = Video(
                    title = "Complete CSS Tutorial (Part 03)",
                    description = "Element Styling",
                    video_url = "static/videos/CSS/CSS_v3.mp4", 
                    thumbnail = "static/imgs/CSS/post-2-3.png",
                    playlist=playlist_CSS
        )
        video4_CSS = Video(
                    title = "Complete CSS Tutorial (Part 04)",
                    description = "Name Conventions And Rules",
                    video_url = "static/videos/CSS/CSS_v4.mp4", 
                    thumbnail = "static/imgs/CSS/post-2-4.png",
                    playlist=playlist_CSS
        )
        video5_CSS = Video(
                    title = "Complete CSS Tutorial (Part 05)",
                    description = "Background - Color, Image, Repeat",
                    video_url = "static/videos/CSS/CSS_v5.mp4", 
                    thumbnail = "static/imgs/CSS/post-2-5.png",
                    playlist=playlist_CSS
        )
        video6_CSS = Video(
                    title = "Complete CSS Tutorial (Part 06)",
                    description = "Background - Attachment, Position, Size",
                    video_url = "static/videos/CSS/CSS_v6.mp4", 
                    thumbnail = "static/imgs/CSS/post-2-6.png",
                    playlist=playlist_CSS
        )
        db.session.add(playlist_CSS)
        db.session.add_all([video1_CSS, video2_CSS, video3_CSS, video4_CSS, video5_CSS, video6_CSS])
        db.session.commit()

    # Initialize Bootstrap Playlist
    if Playlist.query.filter_by(title="Complete Bootstrap Tutorial").first() is None:
        playlist_Bootstrap = Playlist(title= "Complete Bootstrap Tutorial", thumbnail="static/imgs/Bootstrap/learn Bootstrap.png")
        # ... Add Bootstrap videos ...
        video1_Bootstrap = Video(
                    title = "Complete Bootstrap Tutorial (Part 01)",
                    description = "Introduction and What I Need To Learn",
                    video_url = "static/videos/Bootstrap/Bootstrap_v1.mp4",
                    thumbnail = "static/imgs/Bootstrap/Bootstrap1.png",
                    playlist=playlist_Bootstrap
        )
        video2_Bootstrap = Video(
                    title = "Complete Bootstrap Tutorial (Part 02)",
                    description = "Elements And Browser",
                    video_url = "static/videos/Bootstrap_v2.mp4", 
                    thumbnail = "static/imgs/Bootstrap/Bootstrap2.png",
                    playlist=playlist_Bootstrap
        )
        video3_Bootstrap = Video(
                    title = "Complete Bootstrap Tutorial (Part 03)",
                    description = "First Project And First Page",
                    video_url = "static/videos/Bootstrap/Bootstrap_v3.mp4", 
                    thumbnail = "static/imgs/Bootstrap/Bootstrap3.png",
                    playlist=playlist_Bootstrap
        )
        video4_Bootstrap = Video(
                    title = "Complete Bootstrap Tutorial (Part 04)",
                    description = "Head And Nested Elements",
                    video_url = "static/videos/Bootstrap/Bootstrap_v4.mp4", 
                    thumbnail = "static/imgs/Bootstrap/Bootstrap4.png",
                    playlist=playlist_Bootstrap
        )
        video5_Bootstrap = Video(
                    title = "Complete Bootstrap Tutorial (Part 05)",
                    description = "Comments And Use Cases",
                    video_url = "static/videos/Bootstrap/Bootstrap_v5.mp4", 
                    thumbnail = "static/imgs/Bootstrap/Bootstrap5.png",
                    playlist=playlist_Bootstrap
        )

        db.session.add(playlist_Bootstrap)
        db.session.add_all([video1_Bootstrap, video2_Bootstrap, video3_Bootstrap, video4_Bootstrap, video5_Bootstrap])
        db.session.commit()
        db.session.add(playlist_Bootstrap)
        db.session.add_all([video1_Bootstrap, video2_Bootstrap, video3_Bootstrap, video4_Bootstrap, video5_Bootstrap])
        db.session.commit()
    # js
    if Playlist.query.filter_by(title="Complete JAVA Tutorial").first() is None:
        playlist_java = Playlist(title= "Complete JAVA Tutorial", thumbnail="static/imgs/java/java.png")
        # ... Add java videos ...
        video1_java = Video(
                    title = "Complete JAVA Tutorial (Part 01)",
                    description = "Introduction and What I Need To Learn",
                    video_url = "static/videos/java/java_v1.mp4",
                    thumbnail = "static/imgs/java/java1.png",
                    playlist=playlist_java
        )
        video2_java = Video(
                    title = "Complete JAVA Tutorial (Part 02)",
                    description = "Elements And Browser",
                    video_url = "static/videos/java_v2.mp4", 
                    thumbnail = "static/imgs/java/java2.png",
                    playlist=playlist_java
        )
        video3_java = Video(
                    title = "Complete JAVA Tutorial (Part 03)",
                    description = "First Project And First Page",
                    video_url = "static/videos/java/java_v3.mp4", 
                    thumbnail = "static/imgs/java/java3.png",
                    playlist=playlist_java
        )
        video4_java = Video(
                    title = "Complete JAVA Tutorial (Part 04)",
                    description = "Head And Nested Elements",
                    video_url = "static/videos/java/javal_v4.mp4", 
                    thumbnail = "static/imgs/java/java4.png",
                    playlist=playlist_java
        )
        video5_java = Video(
                    title = "Complete JAVA Tutorial (Part 05)",
                    description = "Comments And Use Cases",
                    video_url = "static/videos/java/java_v5.mp4", 
                    thumbnail = "static/imgs/java/java5.png",
                    playlist=playlist_java
        )

        db.session.add(playlist_java)
        db.session.add_all([video1_java, video2_java, video3_java, video4_java, video5_java])
        db.session.commit()

    # JQuery
    if Playlist.query.filter_by(title="Complete JQuery Tutorial").first() is None:
        playlist_JQuery = Playlist(title="Complete JQuery Tutorial", thumbnail="static/imgs/JQuery/JQuery.png")
        # ... Add JQuery videos ...
        video1_JQuery = Video(
            title="Complete JQuery Tutorial (Part 01)",
            description="Introduction to JQuery",
            video_url="static/videos/JQuery/JQuery_v1.mp4",
            thumbnail="static/imgs/JQuery/JQuery1.png",
            playlist=playlist_JQuery
        )
        video2_JQuery = Video(
            title="Complete JQuery Tutorial (Part 02)",
            description="Selectors and Events",
            video_url="static/videos/JQuery/JQuery_v2.mp4",
            thumbnail="static/imgs/JQuery/JQuery2.png",
            playlist=playlist_JQuery
        )
        video3_JQuery = Video(
            title="Complete JQuery Tutorial (Part 03)",
            description="Manipulating the DOM",
            video_url="static/videos/JQuery/JQuery_v3.mp4",
            thumbnail="static/imgs/JQuery/JQuery3.png",
            playlist=playlist_JQuery
        )
        video4_JQuery = Video(
            title="Complete JQuery Tutorial (Part 04)",
            description="Animations and Effects",
            video_url="static/videos/JQuery/JQuery_v4.mp4",
            thumbnail="static/imgs/JQuery/JQuery4.png",
            playlist=playlist_JQuery
        )
        video5_JQuery = Video(
            title="Complete JQuery Tutorial (Part 05)",
            description="AJAX with JQuery",
            video_url="static/videos/JQuery/JQuery_v5.mp4",
            thumbnail="static/imgs/JQuery/JQuery5.png",
            playlist=playlist_JQuery
        )

        db.session.add(playlist_JQuery)
        db.session.add_all([video1_JQuery, video2_JQuery, video3_JQuery, video4_JQuery, video5_JQuery])
        db.session.commit()
    # Sass
    if Playlist.query.filter_by(title="Complete Sass Tutorial").first() is None:
        playlist_Sass = Playlist(title="Complete Sass Tutorial" , thumbnail="static/imgs/Sass/Learn Sass.png")
        # ... Add Sass videos ...
        video1_Sass = Video(
            title="Complete Sass Tutorial (Part 01)",
            description="Introduction to Sass",
            video_url="static/videos/Sass/Sass_v1.mp4",
            thumbnail="static/imgs/Sass/Sass1.png",
            playlist=playlist_Sass
        )
        video2_Sass = Video(
            title="Complete Sass Tutorial (Part 02)",
            description="Variables and Nesting",
            video_url="static/videos/Sass/Sass_v2.mp4",
            thumbnail="static/imgs/Sass/Sass2.png",
            playlist=playlist_Sass
        )
        video3_Sass = Video(
            title="Complete Sass Tutorial (Part 03)",
            description="Mixins and Extends",
            video_url="static/videos/Sass/Sass_v3.mp4",
            thumbnail="static/imgs/Sass/Sass3.png",
            playlist=playlist_Sass
        )
        video4_Sass = Video(
            title="Complete Sass Tutorial (Part 04)",
            description="Sass Functions",
            video_url="static/videos/Sass/Sass_v4.mp4",
            thumbnail="static/imgs/Sass/Sass4.png",
            playlist=playlist_Sass
        )
        video5_Sass = Video(
            title="Complete Sass Tutorial (Part 05)",
            description="Project Integration",
            video_url="static/videos/Sass/Sass_v5.mp4",
            thumbnail="static/imgs/Sass/Sass5.png",
            playlist=playlist_Sass
        )

        db.session.add(playlist_Sass)
        db.session.add_all([video1_Sass, video2_Sass, video3_Sass, video4_Sass, video5_Sass])
        db.session.commit()
    
import unittest
from app import app, db
from models import Users, Playlist, Video, Comment, Like, SavedVideo

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_user(self):
        # Test retrieving user profile
        response = self.app.get('/profile?user_id=1')
        self.assertEqual(response.status_code, 200)

    def test_get_user_missing_id(self):
        # Test retrieving user profile without user_id
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 400)

    def test_register_user(self):
        # Test user registration
        response = self.app.post('/register', data={
            'name': 'testuser',
            'email': 'test@gmail.com',
            'pass': 'password',
            'c_pass': 'password',
            'user_type': 'student'
        })
        self.assertEqual(response.status_code, 201)

    def test_register_user_existing(self):
        # Test registering an existing user
        self.app.post('/register', data={
            'name': 'testuser',
            'email': 'test@gmail.com',
            'pass': 'password',
            'c_pass': 'password',
            'user_type': 'student'
        })
        response = self.app.post('/register', data={
            'name': 'testuser',
            'email': 'test@gmail.com',
            'pass': 'password',
            'c_pass': 'password'
        })
        self.assertEqual(response.status_code, 409)

    def test_login_user(self):
        # Test user login
        self.app.post('/register', data={
            'name': 'testuser',
            'email': 'test@gmail.com',
            'pass': 'password',
            'c_pass': 'password'
        })
        response = self.app.post('/login', json={
            'email': 'test@gmail.com',
            'pass': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_user_invalid(self):
        # Test login with invalid credentials
        response = self.app.post('/login', json={
            'email': 'wrong@gmail.com',
            'pass': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)

    def test_update_profile(self):
        # Test updating user profile
        # Assuming user with ID 1 exists
        response = self.app.patch('/update-profile/1', data={
            'username': 'updateduser',
            'email': 'updated@gmail.com'
        })
        self.assertEqual(response.status_code, 200)

    def test_update_profile_user_not_found(self):
        # Test updating a non-existing user profile
        response = self.app.patch('/update-profile/999', data={
            'username': 'updateduser',
            'email': 'updated@gmail.com'
        })
        self.assertEqual(response.status_code, 404)

    def test_courses(self):
        # Test retrieving courses
        response = self.app.get('/courses')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
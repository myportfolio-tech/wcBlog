from weblog.models import User
 
def test_new_user():

    user = User(username='username01', email='username01@email.com', image_file='default.jpg', password='test-password')
    assert user.email == 'username01@email.com'

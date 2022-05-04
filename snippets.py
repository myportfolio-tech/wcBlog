# from itsdangerous import URLSafeTimedSerializer as Serializer

# s = Serializer("secret", 30)
# token = s.dumps('user_email', salt='password-reset-salt')
# print(token)

# token = s.dumps({'user_id':1}, salt='password-reset-salt')
# print(token)

###  

from itsdangerous import URLSafeTimedSerializer as Serializer
s = Serializer('secret', )
token = s.dumps({'user_id': 1, 'email': 'myemail.com'})
print(token)
print(s.loads(token, ))
user_id=s.loads(token, )['user_id']
print(user_id)
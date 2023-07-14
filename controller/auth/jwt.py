import os
import datetime
import jwt

class Auth:
    def __init__(self, expiration_hours):
        self.expiration_hours = expiration_hours
        self.secret_key = os.getenv('SECRET_KEY')

    def generate_token(self,user_id):

        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours= self.expiration_hours)
        }
        
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token    
    
    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms='HS256')
            return True, payload['user_id']
        except jwt.ExpiredSignatureError:
            return False, "expired token"
        except jwt.InvalidSignatureError:
            return False, "invalid token"
        
        
        
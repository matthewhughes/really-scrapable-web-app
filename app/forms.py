'''
from flask.ext.wtf import Form, TextField, BooleanField
from flask.ext.wtf import Required

class LoginForm(Form):
    username = TextField('username', validators = [Required()])
    password = TextField('password', validators = [Required()])
    '''

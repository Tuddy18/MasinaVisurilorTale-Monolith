from wtforms import Form, StringField, PasswordField, validators

class RegisterForm(Form):
    # Commit to DB
    username = StringField('Username', [
        validators.Length(min=3, max=25)
        ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')
    name = StringField('Profile Name', [
        validators.Length(min=3, max=25)
        ])
    profileType = StringField('Profile Type')
    description = StringField('Profile Description')


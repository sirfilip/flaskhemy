from wtforms import Form, StringField, TextField, validators


class PostForm(Form):
    title = StringField('Title', [validators.Length(min=4, max=100)])
    body = TextField('Body', [validators.Length(min=4, max=1000)])

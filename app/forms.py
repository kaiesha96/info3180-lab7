from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField("Description", validators=[DataRequired()])
    photo = FileField("Photo",validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'],'Images Only !')])

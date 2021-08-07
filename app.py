from fastai.text.all import *

from flask import Flask, jsonify, request, render_template, flash
from wtforms import Form, TextField, TextAreaField, validators, SubmitField
path = Path(__file__).parent
learn = load_learner(path/'saved'/'export_win10.pkl')

app = Flask(__name__)

# App config
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    comment = TextAreaField('Comment:', validators=[validators.required()])

def set_toxicity_message(comment, preds):
	'''
	sets appropriate message for toxic score
	input: toxicity score (fraction)
	output: message string
	'''
#	toxicity_message = ''

	if preds:
	    toxicity_message = f"Failed: your comment ('{comment}') cannot be allowed because it has been identified as {',  '.join(preds).upper()}"
	else:
	    toxicity_message = f"Success: your comment ('{comment}') will be posted"

	return toxicity_message


@app.route('/', methods=['GET', 'POST'])
def hello():
	form = ReusableForm(request.form)

	print(form.errors)
	if request.method == 'POST':
		comment = request.form['comment']
		if form.validate():
			preds = list(learn.predict(comment)[0])
			toxicity_message = set_toxicity_message(comment,preds)
			flash(toxicity_message)
		else:
			flash('Error: All the form fields are required. ')

	return render_template('hello.html', form=form)


if __name__ == '__main__':
    app.run()

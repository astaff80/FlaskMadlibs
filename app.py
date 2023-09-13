from flask import Flask

from flask import request

from flask import render_template

from flask_debugtoolbar import DebugToolbarExtension

import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "blahblahblah123"
#debug = DebugToolbarExtension(app)


selectedStory = stories.story


@app.route('/story')
def tell():
	urStory = selectedStory.generate(request.args)
	return render_template("story.html", yourStory=urStory)



@app.route('/')
def inputPage():
	urPrompt = ["place", "noun", "verb", "adjective", "plural_noun"]
	yourText = selectedStory.template
	return render_template("madlib.html", yourPrompt=urPrompt, urText = yourText)




#SECRET_KEY
from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
import string
import random


def random_string(size = 6, chars = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def my_tts(text,name):
	tts = gTTS(text)
	tts.save('audio.mp3')

	main_file = open('audio.mp3','rb').read()
	dest_file = open('static/'+name + '.mp3','wb+')
	dest_file.write(main_file)
	dest_file.close()

app = Flask(__name__)

@app.get('/')
def index():
	return render_template('index.html')

@app.post('/tts')
def tts():
	if request.method == 'POST':
		text = request.form.get('text')
		rand = random_string(16)
		my_tts(text,rand)
		return jsonify(audio=rand+'.mp3',statusCode = 200,message='success')

if __name__ == '__main__':
	app.run(debug=True)
	
from flask import Flask,render_template, url_for,redirect

app=Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

@app.route("/home")
def home():
	return render_template('index.html')
@app.route('/projects')
def projects():
	return render_template('projects.html')
if __name__ == '__main__':
    app.run()

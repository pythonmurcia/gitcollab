from flask import Flask, render_template

app = Flask(__name__,
            static_url_path="",
            static_folder="static",
            template_folder="templates"
        )

@app.route("/")
def home():
    return render_template('index.html')

@app.errorhandler(400)
def error404(err):
	e = {
		'number':'400',
		'description':'The request that this page has received is not valid. Perhaps your browser has been confused or you are using the wrong method access to this page.' 
	}
	return render_template('error.html', title='404', error=e), 400

@app.errorhandler(401)
def error404(err):
	e = {
		'number':'401',
		'description':'We are sorry, but you do not have authorization to access this page.' 
	}
	return render_template('error.html', title='404', error=e), 401

@app.errorhandler(403)
def error404(err):
	e = {
		'number':'403',
		'description':'We are sorry but access to this page is prohibited. Contact an administrator to grant you access.' 
	}
	return render_template('error.html', title='404', error=e), 403

@app.errorhandler(404)
def error404(err):
	e = {
		'number':'404',
		'description':'We could not find the page you are looking for, perhaps you have misspelled the link or the page is private.' 
	}
	return render_template('error.html', title='404', error=e), 404

@app.errorhandler(500)
def error404(err):
	e = {
		'number':'500',
		'description':'Do not worry, this error is not your fault. There has been an internal error on our server. We are trying to fix it.' 
	}
	return render_template('error.html', title='404', error=e), 500

if __name__ == "__main__":
    # Importante desactivar esto en producción
    app.run(debug=True)

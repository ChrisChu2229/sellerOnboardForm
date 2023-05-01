from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store form data
form_data = []


@app.route('/', methods=['GET', 'POST'])
def onboarding_form():
    global form_data
    if request.method == 'POST':
        form_data.append(request.form.to_dict())
        return redirect(url_for('results'))
    return render_template('form.html')


@app.route('/results')
def results():
    return render_template('results.html', form_data=form_data)


if __name__ == '__main__':
    app.run(debug=True)

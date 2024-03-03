from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["POST", "GET"]) # Added methods for handling the post request
def index():
    if request.method == "POST":
        note = request.form.get("note") # Changed request.args to request.form to receive the form elements
        if note:
            notes.append(note)
            return redirect(url_for('index'))  # Redirect to the same page to clear the form
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)

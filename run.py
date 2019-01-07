from annotator import Annotator
from flask import Flask, render_template, request, jsonify
import atexit

app = Flask(__name__)

annotator = Annotator()


def emergency_save_db():
    annotator._database._save_data()


@app.route('/annotate', methods=["POST", "GET"])
def annotate():
    if request.method == "POST":
        x = request.form["x"]
        y = request.form["y"]
        annotator.annotate([x,y])

    next_picture = annotator.next_to_annotate()

    if not next_picture:
        return "All pictures were annotated"
    else:
        return render_template("main.html", picture=next_picture)


if __name__ == '__main__':
    atexit.register(emergency_save_db)
    app.run(debug=True)

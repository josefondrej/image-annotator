from annotator import Annotator
from flask import Flask, render_template, request

app = Flask(__name__)

annotator = Annotator()


@app.route('/annotate', methods=["POST", "GET"])
def annotate():
    if request.method == "POST":
        try:
            x = request.form["x"]
            y = request.form["y"]
            image = request.form["img"]
            image = image.split("/")[-1]
            annotator.annotate(image, [x, y])
        except Exception as e:
            pass  # TODO: handle

    next_image = annotator.next_to_annotate()

    if not next_image:
        return "All images were annotated"
    else:
        return render_template("main.html", img=next_image)


if __name__ == '__main__':
    app.run(debug=True)

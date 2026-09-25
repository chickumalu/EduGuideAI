from flask import Flask, render_template, request
from recommendation import recommend_career

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    answers = request.form.to_dict()

    career = recommend_career(answers)

    return f"""
    <html>

    <head>
        <title>EduGuide AI - Result</title>
    </head>

    <body>

        <h1>EduGuide AI</h1>

        <h2>Your Career Recommendation</h2>

        <h1>{career}</h1>

        <p>
            Based on the information you provided,
            EduGuide AI recommends this career as a possible match.
        </p>

        <br>

        <a href="/">Take the Questionnaire Again</a>

    </body>

    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)

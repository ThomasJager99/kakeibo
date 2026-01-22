from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET", "POST"])
def index():
    amount = None

    if request.method == "POST":
        amount = request.form.get("amount")

    if amount:
        expenses.append(amount)


    return render_template("index.html", expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)






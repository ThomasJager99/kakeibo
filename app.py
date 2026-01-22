from flask import Flask, render_template, request
from database import init_bd, get_connection

app = Flask(__name__)

init_bd()

@app.route("/", methods=["GET", "POST"])
def index():
    amount = None

    if request.method == "POST":
        amount = request.form.get("amount")

    if amount:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO expenses (amount) VALUES (?)",
                (amount, )
            )
            conn.commit()

    with get_connection() as conn:
        rows=conn.execute(
            "SELECT amount FROM expenses ORDER BY id DESC"
        ).fetchall()
    expenses = [row[0] for row in rows]

    return render_template("index.html", expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)






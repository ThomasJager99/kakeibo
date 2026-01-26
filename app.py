from flask import Flask, render_template, request
from database import init_bd, get_connection

app = Flask(__name__)

init_bd()

@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    if request.method == "POST":
        amount_raw= request.form.get('amount')
        currency = request.form.get("currency")
        category = request.form.get("category")
        note = request.form.get('note')

        #basic validation for amount field
        try:
            amount = float(amount_raw)
        except (TypeError, ValueError):
            amount = None

        if amount is not None and amount > 0 and currency and category and note:
            with get_connection() as conn:
                conn.execute(
                    "INSERT INTO expenses (amount, currency, note, category) VALUES (?,?,?,?)",
                    (amount, currency, category, note)
                )
                conn.commit()
        else:
            error = 'Please fill all required field correctly'

    with get_connection() as conn:
        rows = conn.execute(
            """
    SELECT amount, currency, category, note, created_at
    FROM expenses
    ORDER BY id DESC
    """
        ).fetchall()
    expenses = rows

    return render_template("index.html", expenses=expenses, error=error)

if __name__ == '__main__':
    app.run(debug=True)


# currency = "EUR"
# category = ""
#
# if currency and category:
#     print("OK")
# else:
#     print("Missing data")



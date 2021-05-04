# pip install -r requirements.txt --> naredba za instalaciju preko terminala

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    poruka = "Ovo je string iz main.py"

    gradovi = ["Zagreb", "Rijeka", "Split", "Osijek"]

    return render_template("index.html", poruka=poruka, gradovi=gradovi)

@app.route("/about_me")  # ruta se piše u linkovima unutar html koda za skakanje sa stranice na stranicu
def about_me():
    return render_template("about_me.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == "__main__":
    app.run(use_reloader=True)  # use_reloader=True se koristi kako bi radila app sa refreshom ako promijenimo nešto u kodu

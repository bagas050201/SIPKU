from flask import Flask
from logincontroller import login
from dashboardcontroller import dashboard

app=Flask(__name__)
app.config["SECRET_KEY"]="kpm2021"

app.register_blueprint(login)
app.register_blueprint(dashboard)


if __name__ == "__main__":
    app.run()

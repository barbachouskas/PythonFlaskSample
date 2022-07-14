from werkzeug.utils import redirect
from app import app
from flask import render_template, url_for, request, session, flash, redirect
import os, uuid
from datetime import datetime, timedelta

from app import app_config

from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route("/")
def index():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()
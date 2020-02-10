from flask import render_template, Blueprint
from flask_login import login_required

charts = Blueprint('charts', __name__)

@charts.route("/piechart")
@login_required
def piechart():
    return render_template("piechart.html")

@charts.route("/doughnut")
@login_required
def doughnut():
    return render_template("doughnut.html")

@charts.route("/polararea")
@login_required
def polararea():
    return render_template("polararea.html")

@charts.route("/verticalbargraph")
@login_required
def verticalbargraph():
    return render_template("verticalbargraph.html")

@charts.route("/horizontalbargraph")
@login_required
def horizontalbargraph():
    return render_template("horizontalbargraph.html")

@charts.route("/linegraphcategory")
@login_required
def linegraphcategory():
    return render_template("linegraphcategory.html")

@charts.route("/linegraphplotting")
@login_required
def linegraphplotting():
    return render_template("linegraphplotting.html")

@charts.route("/scatterplot")
@login_required
def scatterplot():
    return render_template("scatterplot.html")

@charts.route("/bubblechart")
@login_required
def bubblechart():
    return render_template("bubblechart.html")

@charts.route("/radarchart")
@login_required
def radarchart():
    return render_template("radarchart.html")

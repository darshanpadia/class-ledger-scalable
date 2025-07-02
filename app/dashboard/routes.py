from flask import Blueprint, render_template, redirect, url_for, flash

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

dashboard_bp.route("/home")
def home():
    return render_template('dashboard/home.html')
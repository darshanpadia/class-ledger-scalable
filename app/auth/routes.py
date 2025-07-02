from flask import Blueprint, render_template, redirect, url_for, flash
from app.auth.forms import TeacherLoginForm
from app.auth.services import authenticate_teacher, login_teacher, logout_teacher

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/teacher_login", methods=["GET", "POST"])
def teacher_login():
    form = TeacherLoginForm()
    if form.validate_on_submit():
        teacher = authenticate_teacher(form.username.data, form.password.data)
        if teacher:
            login_teacher(teacher)
            flash("Login Successful", "success")
            return redirect(url_for("dashboard.home"))
        flash("Invalid Username or Password", "danger")
    return render_template("auth/teacher_login.html", form=form)

@auth_bp.route("/logout", methods=["POST"])
def teacher_logout():
    logout_teacher()
    flash("You have been logged out.", "info")
    return redirect(url_for('teacher_login'))
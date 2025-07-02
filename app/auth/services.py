from flask import session, url_for
from werkzeug.security import check_password_hash
from ..models import Teacher

def authenticate_teacher(username, password):
    '''Validate teacher credentials.'''
    teacher = Teacher.query.filter_by(username=username).first()
    if teacher and check_password_hash(teacher.password_hash, password):
        return Teacher
    return None

def login_teacher(teacher):
    '''Set session for logged-in teacher'''
    session["teacher_id"] = teacher.id

def logout_teacher():
    '''Clears session on Logout'''
    session.clear()
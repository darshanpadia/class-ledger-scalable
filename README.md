class-ledger-flask/
├── .env-sample
├── .gitignore
├── app.py
├── config.py
├── extensions.py
├── forms/
│   ├── __init__.py
│   ├── auth_forms.py
│   ├── common_forms.py
│   └── dashboard_forms.py
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       ├── 36a7ddc71eb7_add_editlog.py
│       ├── 48a1a56d4f42_add_studentrecord.py
│       └── f8d7210376c3_setup_with_teacher.py
├── models/
│   ├── __init__.py
│   ├── edit_log.py
│   ├── student_record.py
│   └── teacher.py
├── README.md
├── repositories/
│   ├── edit_log_repo.py
│   ├── student_record_repo.py
│   └── teacher_repo.py
├── requirements.txt
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py
│   └── dashboard_routes.py
├── services/
│   ├── auth_services.py
│   ├── dashboard_services.py
│   └── teacher_services.py
├── static/
│   ├── auth.css
│   └── dashboard.css
├── templates/
│   ├── auth_templates/
│   │   └── login.html
│   └── dashboard_templates/
│       └── home.html
└── wsgi.py

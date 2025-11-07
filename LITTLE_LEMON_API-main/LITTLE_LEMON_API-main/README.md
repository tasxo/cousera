# Little Lemon API (Django + DRF) - Scaffold

## What this contains
- Django project named `little_lemon_api`
- App named `api`
- Models: Menu, Booking
- Serializers, Views (ViewSets), URLs
- Token authentication skeleton (uses `rest_framework.authtoken`)
- Placeholder MySQL settings (update with your credentials) and default SQLite for quick start.
- `requirements.txt`

## Quick start (local)
1. Create virtualenv and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Edit `little_lemon_api/settings.py` DATABASES section if you want MySQL.
   For MySQL, uncomment and fill `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`.
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Run dev server:
   ```bash
   python manage.py runserver
   ```
5. API endpoints (examples):
   - `GET /api/menu/`
   - `POST /api/menu/`
   - `GET /api/bookings/`
   - `POST /api/bookings/`
   - `POST /api/auth/register/`
   - `POST /api/auth/login/`  (to obtain token)

## Notes
- This is a scaffold. You may need to adjust permissions, add tests, and secure secret keys for production.
- MySQL requires `mysqlclient` package; add it if using MySQL.

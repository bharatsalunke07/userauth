# UserAuth - Django Authentication System

A modern, full-featured User Authentication web application built using **Django 5**, **PostgreSQL**, and **Vanilla CSS** with a sleek glassmorphic UI.

---

## 🌟 Key Features

- **🔐 User Registration & Authentication**
  - Secure user signup with username, email, and password confirmation.
  - Inactive account state until email verification.
  - User login & logout with session management.

- **✉️ Email Verification via OTP**
  - Automated 6-digit One-Time Password (OTP) sent to the user's email upon registration.
  - 10-minute expiration timer on verification codes.
  - Built-in **Resend OTP** functionality.

- **🔑 Password Reset Flow**
  - Secure email-based password reset workflow using Django's authentication views.
  - Step-by-step guidance: Request Link ➔ Email Sent ➔ Set New Password ➔ Password Changed.

- **👁️ Interactive UI Features**
  - Password visibility toggle (show/hide password).
  - Glassmorphic UI design with smooth micro-animations and glowing accent buttons.
  - Fully responsive design optimized for desktop and mobile devices.

- **📊 User Dashboard & Account Management**
  - Protected User Dashboard displaying logged-in user details.
  - Account deletion option with confirmation safety prompts.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, Django 5.2
- **Database:** PostgreSQL (with `psycopg3`) / SQLite
- **Email Service:** SMTP Relay (configured for Brevo / Sendinblue)
- **Frontend:** HTML5, Custom CSS3 (Glassmorphic Design), JavaScript (ES6+)

---

## 📁 Project Structure

```text
userauth/
└── loginauth/
    ├── accounts/
    │   ├── static/accounts/
    │   │   ├── css/style.css
    │   │   └── js/script.js
    │   ├── templates/accounts/
    │   │   ├── dashboard.html
    │   │   ├── home.html
    │   │   ├── login.html
    │   │   ├── password_reset.html
    │   │   ├── password_reset_complete.html
    │   │   ├── password_reset_confirm.html
    │   │   ├── password_reset_done.html
    │   │   ├── register.html
    │   │   └── verify_email.html
    │   ├── admin.py
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    ├── loginauth/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── .env
    ├── manage.py
    └── requirements.txt
```

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.10+ and PostgreSQL installed on your machine.

### 2. Clone & Setup Virtual Environment

```bash
# Navigate to project directory
cd loginauth

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (`.env`)

Create a `.env` file inside the `loginauth/` directory:

```env
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True

DB_NAME=userauth_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST=smtp-relay.brevo.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_smtp_user
EMAIL_HOST_PASSWORD=your_smtp_password
DEFAULT_FROM_EMAIL=your_email@example.com
```

### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit `http://127.0.0.1:8000/`.

---

## 🔗 Main Application Routes

| Endpoint | View Function / Template | Description |
| :--- | :--- | :--- |
| `/` | `home` (`home.html`) | Landing page |
| `/register/` | `register` (`register.html`) | User account creation |
| `/verify-email/` | `verify_email` (`verify_email.html`) | OTP verification page |
| `/resend-otp/` | `resend_otp` | Generates & sends new OTP |
| `/login/` | `user_login` (`login.html`) | Account login |
| `/dashboard/` | `dashboard` (`dashboard.html`) | User profile dashboard (Protected) |
| `/password-reset/` | `PasswordResetView` | Forgot password request page |
| `/delete-account/` | `delete_account` | Deletes authenticated user account |
| `/logout/` | `user_logout` | Logs out the user |

---



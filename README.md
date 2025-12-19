# Resource Management System

A Django-based Resource Management System with role-based access control and pagination.

## Features

- **User Authentication**: Login/Logout functionality
- **Role-Based Access Control**:
  - **Administrator**: Full CRUD permissions
  - **Faculty**: Create, Read, Update, and limited Delete (own resources only)
  - **Student**: Read-only access
- **Resource Model** with fields:
  - Title
  - Resource Type (Lecture, Assignment, Reference)
  - Description
  - Uploaded File
  - Created By
  - Created At
- **Pagination**: 10 resources per page with navigation controls
- **Clean MVT Architecture**: Proper separation of Models, Views, and Templates

## Installation & Setup

### Prerequisites

- Python 3.8 or higher installed on your system
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/Nouman13388/adv_web_final.git
   cd adv_web_final
   ```

2. **Create a virtual environment**:

   **On Windows (PowerShell):**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **On Windows (Command Prompt):**

   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```

   **On macOS/Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Upgrade pip** (optional but recommended):

   ```bash
   python -m pip install --upgrade pip
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Create migrations for resources app**:

   ```bash
   python manage.py makemigrations resources
   python manage.py migrate
   ```

6. **Setup initial data** (creates demo users and 5 sample resources):

   ```bash
   python setup_data.py
   ```

   This script will create:

   - 3 demo users (Administrator, Faculty, Student)
   - 5 sample resources for testing
   - Required user groups (Faculty, Student)

7. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Open your browser and navigate to: `http://127.0.0.1:8000`
   - You'll be redirected to the login page
   - Use one of the demo credentials below to login

## Demo Credentials

Login with any of these pre-configured accounts:

| Role              | Username  | Password     | Permissions                                               |
| ----------------- | --------- | ------------ | --------------------------------------------------------- |
| **Administrator** | `admin`   | `admin123`   | Full CRUD - Create, Read, Update, Delete all resources    |
| **Faculty**       | `faculty` | `faculty123` | Create, Read, Update all resources + Delete own resources |
| **Student**       | `student` | `student123` | Read-only access to all resources                         |

### First Login

1. Navigate to `http://127.0.0.1:8000`
2. You'll be redirected to the login page
3. Enter one of the usernames and passwords above
4. Test different roles to see the permission differences!

## Project Structure

```
adv_web_final/
├── resource_management/          # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Project configuration
│   ├── urls.py                  # Main URL configuration
│   └── wsgi.py
├── resources/                    # Resources app (MVT structure)
│   ├── migrations/              # Database migrations
│   ├── __init__.py
│   ├── admin.py                 # Admin panel configuration
│   ├── apps.py                  # App configuration
│   ├── decorators.py            # Role-based access control decorators
│   ├── forms.py                 # Resource form
│   ├── models.py                # Resource model (Model layer)
│   ├── urls.py                  # App URL patterns
│   └── views.py                 # CRUD views with pagination (View layer)
├── templates/                    # HTML templates (Template layer)
│   ├── base.html               # Base template with navbar
│   └── resources/
│       ├── login.html          # Login page
│       ├── resource_list.html  # List view with pagination
│       ├── resource_detail.html # Detail view
│       ├── resource_form.html  # Create/Update form
│       └── resource_confirm_delete.html # Delete confirmation
├── media/                        # User uploaded files
│   └── resources/               # Resource files directory
├── static/                       # Static files (CSS, JS, images)
├── venv/                         # Virtual environment (not in git)
├── db.sqlite3                    # SQLite database (not in git)
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── setup_data.py                # Initial setup script
├── .gitignore                   # Git ignore file
└── README.md                     # This file
```

## Usage

### Administrator

- Can create, view, update, and delete all resources
- Full access to all features

### Faculty

- Can create new resources
- Can view all resources
- Can update all resources
- Can delete only their own resources

### Student

- Can view all resources
- Cannot create, update, or delete resources
- Read-only access

## Features in Detail

### Pagination

- Displays 10 resources per page
- Navigation controls: First, Previous, Page Numbers, Next, Last
- Works correctly for all user roles
- Shows current page and total count

### CRUD Operations

- **Create**: Form-based resource creation (Admin/Faculty only)
- **Read**: List view with pagination and detail view
- **Update**: Edit existing resources (Admin/Faculty only)
- **Delete**: Remove resources with confirmation (Role-based restrictions)

### Security

- Login required for all resource operations
- Role-based access control using decorators
- CSRF protection on all forms
- File upload validation

## Technologies Used

- **Backend**: Django 4.2.27
- **Frontend**: Bootstrap 5.3 (CDN)
- **Database**: SQLite3 (default Django database)
- **File Handling**: Pillow 12.0.0
- **Python**: 3.8+

## Key Features Implementation

### MVT Architecture (Model-View-Template)

- **Models** ([resources/models.py](resources/models.py)): Resource model with all required fields
- **Views** ([resources/views.py](resources/views.py)): Function-based views for CRUD operations
- **Templates** ([templates/resources/](templates/resources/)): HTML templates with Bootstrap styling

### Role-Based Access Control

- Implemented using custom decorators ([resources/decorators.py](resources/decorators.py))
- Group-based permissions (Administrator, Faculty, Student)
- Permission checks in views and templates

### Pagination

- Django's built-in Paginator class
- 10 resources per page
- Full navigation: First, Previous, Page Numbers, Next, Last
- Page information display (current page, total pages, total resources)

## Common Commands

```bash
# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Windows CMD:
venv\Scripts\activate.bat

# macOS/Linux:
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Run development server
python manage.py runserver

# Create a superuser (admin panel access)
python manage.py createsuperuser

# Access admin panel
# http://127.0.0.1:8000/admin

# Make new migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run setup script again (will skip existing data)
python setup_data.py
```

## Troubleshooting

### Issue: Virtual environment not activating

**Solution**: On Windows, you may need to enable script execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Port 8000 already in use

**Solution**: Either stop the existing server or use a different port:

```bash
python manage.py runserver 8080
```

### Issue: Static files not loading

**Solution**: Ensure the `static` directory exists and collectstatic is run (if needed):

```bash
python manage.py collectstatic
```

## License

This project is created for educational purposes.

## Contributing

This is an educational project. Feel free to fork and modify for your own learning!

## Author

**Nouman13388**

- GitHub: [@Nouman13388](https://github.com/Nouman13388)
- Repository: [adv_web_final](https://github.com/Nouman13388/adv_web_final)

---

**Happy Learning! 🚀**

# 📝 Django Personal Blog

A simple and elegant personal blog built with Django framework, featuring a clean interface and powerful search functionality.

## ✨ Features

- 📖 **Article Management**: Create, read, and manage blog articles
- 🔍 **Search Functionality**: Search through articles by title and content
- 🎨 **Clean UI**: Beautiful and responsive interface
- ⚡ **Fast Performance**: Optimized database queries
- 🛡️ **Admin Panel**: Easy content management through Django admin
- 📱 **Responsive Design**: Works perfectly on all devices

## 🚀 Demo

<img src="https://github.com/MohamedZidane11/django-blog-app/blob/main/Capture9.PNG" width=850>

## 🛠️ Technologies Used

- **Backend**: Django 5.x
- **Database**: SQLite (default) / PostgreSQL / MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Language**: Python 3.8+

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MohamedZidane11/django-blog-app.git
   cd django-personal-blog
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv blog_env
   source blog_env/bin/activate  # On Windows: blog_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   super user ==> (testuser/testuser)
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**
   - Main blog: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 🎯 Usage

### Adding Articles
1. Navigate to the admin panel: `/admin/`
2. Login with your superuser credentials
3. Click on "Articles" → "Add Article"
4. Fill in the title and content
5. Click "Save"

### Searching Articles
- Use the search box on the homepage
- Search works on both article titles and content
- Supports multiple keywords
- Shows number of results found

## 🔧 Configuration

### Database Configuration
The project uses SQLite by default. To use PostgreSQL or MySQL, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Static Files
For production, configure static files in `settings.py`:

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
```

## 🎨 Customization

### Styling
- Modify CSS in `blog_project/static/css/style.css`
- Add custom styles for better appearance
- Customize colors and fonts

### Features to Add
- 💬 Comments system
- 🏷️ Article categories
- 👤 User authentication
- ❤️ Like system
- 📊 Article statistics
- 🔗 Social sharing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

⭐ **If you found this project helpful, please give it a star!** ⭐

---

## 🐛 Issues

Found a bug? Have a feature request? Please create an issue.

## 📈 Roadmap

- [ ] Add user authentication
- [ ] Implement comment system
- [ ] Add article categories
- [ ] Create RSS feed
- [ ] Add social media sharing
- [ ] Implement article tags
- [ ] Add rich text editor
- [ ] Create API endpoints

---

**Happy Coding!** 🎉

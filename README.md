📝 Blog Management Web App
A Django-based blog management system that allows users to perform CRUD operations on blog posts and categories. The project also includes user dashboards, file uploads, and a ready-to-deploy configuration.

🚀 Features
Blog creation, update, and deletion

Category CRUD functionality

Media file upload and storage

User dashboard for managing content

Static and template handling

SQLite database integration

Ready for deployment

🗂️ Project Structure
bash
Copy
Edit
├── blog_main/           # Main Django project configuration
├── blogs/               # Blog app with views, models, URLs, etc.
├── dashboard/           # Dashboard functionality for user/admin
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, etc.)
├── media/uploads/       # Uploaded media files
├── uploads/25/01/       # Category CRUD-related uploads
├── db.sqlite3           # SQLite database file
├── manage.py            # Django management script
├── requirement.txt      # Python dependencies
└── .gitignore           # Git ignore rules
📦 Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/AnushkaShridhar18/your-repo-name.git
cd your-repo-name
Create a Virtual Environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
pip install -r requirement.txt
Apply Migrations

bash
Copy
Edit
python manage.py migrate
Run the Development Server

bash
Copy
Edit
python manage.py runserver
Access the App
Open your browser and go to: http://127.0.0.1:8000/

🛠️ Usage
Add new blog posts through the dashboard

Upload images/media using the provided UI

Manage blog categories dynamically

View and interact with blog content

🧾 Dependencies
Make sure to check requirement.txt for the full list of required packages.

📌 To-Do
Add authentication and user roles

Improve UI/UX for dashboard

Add pagination and search

Set up production deployment (e.g., Heroku or Render)

🧑‍💻 Author
Anushka Shridhar
GitHub: AnushkaShridhar18

Happy Blogging! 🎉

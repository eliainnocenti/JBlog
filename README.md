# JBlog

JBlog is a Django-based web application for creating and managing a personal blog. It allows users to create accounts, write blog posts, and interact with other users through comments.

## Modules/Apps

### Blog
The Blog app handles all functionalities related to blog posts, including creation, editing, and deletion. It includes features such as:

- Displaying a list of blog posts
- Viewing individual blog posts
- Creating new blog posts
- Updating existing blog posts
- Deleting blog posts

### Users
The Users app manages user authentication and profile management. It provides the following features:

- User registration
- User login/logout
- Profile creation and update
- Displaying user profiles

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd JBlog
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```


6. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

<!-- TODO: check and update this section -->

### Creating a Blog Post
1. Log in to your account or register if you don't have one.
2. Navigate to the "New Post" page.
3. Fill in the title and content of your post.
4. Optionally, set the published date.
5. Click the "Save" button to create your post.

### Updating a Blog Post
1. Log in to your account.
2. Navigate to the post you want to edit.
3. Click the "Edit" button.
4. Modify the title, content, or published date as needed.
5. Click the "Save" button to update the post.

### Deleting a Blog Post
1. Log in to your account.
2. Navigate to the post you want to delete.
3. Click the "Delete" button.
4. Confirm the deletion.

## Directory Structure

- `JBlog`
  - `blog/`: Contains functionalities related to blog posts.
    - `migrations/`: Contains database migration files.
    - `templates/`: Contains HTML templates for blog-related views.
      - `blog/`: Contains HTML templates specific to the Blog app.
    - `__init__.py`: Initializes the Blog app.
    - `admin.py`: Registers models with the Django admin site.
    - `apps.py`: Configures the Blog app for the Django project.
    - `forms.py`: Contains forms for creating and updating blog posts.
    - `models.py`: Defines the Post model for blog posts.
    - `urls.py`: Contains URL patterns for blog-related views.
    - `views.py`: Contains view functions for blog-related functionalities.
  - `users/`: Contains functionalities related to user authentication and profiles.
    - `migrations/`: Contains database migration files.
    - `templates/`: Contains HTML templates for user-related views.
      - `users/`: Contains HTML templates specific to the Users app.
    - `__init__.py`: Initializes the Users app.
    - `admin.py`: Registers models with the Django admin site.
    - `apps.py`: Configures the Users app for the Django project.
    - `forms.py`: Contains forms for user registration and profile updates.
    - `models.py`: Defines the User model and other models related to user profiles.
    - `signals.py`: Contains signals that are triggered by user-related actions.
    - `urls.py`: Contains URL patterns for user-related views.
    - `views.py`: Contains view functions for user-related functionalities.
  - `JBlog/`: Contains project-level settings and configurations.
    - `settings.py`: Contains project settings such as database configuration, static files, and middleware.
    - `urls.py`: Contains URL patterns for the project.
    - `wsgi.py`: Configures the WSGI application for deployment.
  - `media/`: Directory for storing user-uploaded files such as images.
  - `static/`: Directory for storing static files such as CSS and JavaScript.
  - `templates/`: Contains base HTML templates for the project.
  - `manage.py`: Command-line utility for interacting with the project.

## Contributors

- Elia Innocenti ([@eliainnocenti](https://github.com/eliainnocenti))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

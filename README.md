# Django BPosts Website

This project is a simple blog post website built using the Django web framework. It provides a platform for users to create, edit, and share their blog posts. The project includes features such as user authentication, allowing registered users to have their own profiles and manage their posts.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Create and Edit Posts**: Authenticated users can create new blog posts and edit existing ones.
- **Responsive Design**: The website is designed to be responsive, ensuring a seamless experience across different devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aza4k/BPosts.git
   ```

2. Open folder:

   ```bash
   cd BPosts/
   ```

3. Create a virtual environment:

   ```bash
   virtualenv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     Source \venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the website.

## Usage

1. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your superuser account.

2. Log in to the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) using the superuser credentials.

3. Create blog posts, manage users, and explore the admin functionalities.

4. Visit the homepage at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the blog in action.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to customize and enhance the project as needed for your own blog post website. Happy coding!

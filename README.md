# CustomerEdge

This is a Django Customer Record Management project. It is a web application that allows you to manage customer records efficiently. It provides functionality to create, view, update, and delete customer records, as well as search and filter records.
![Screenshot 2023-07-01 103428](https://github.com/NatalioF22/CustomerEdge/assets/116610989/24b70031-078c-4ca1-b83c-a3f5c4e0bd0e)
![Screenshot 2023-07-01 103505](https://github.com/NatalioF22/CustomerEdge/assets/116610989/ef6a66b4-15a8-4022-8370-3d4c26d48742)
![Screenshot 2023-07-01 103524](https://github.com/NatalioF22/CustomerEdge/assets/116610989/0172358f-8243-4bc4-980a-e44bd80b7db3)
![Screenshot 2023-07-01 103537](https://github.com/NatalioF22/CustomerEdge/assets/116610989/6bf1645c-0dcb-45b2-8238-87c95e8f278d)

## Features

- User Authentication: The application supports user registration, login, and authentication to ensure secure access to the customer record management system.

- Customer Record CRUD Operations: Users can perform Create, Read, Update, and Delete operations on customer records. They can add new customers, view details of existing customers, update customer information, and delete customer records when necessary.

- Search and Filter: The application allows users to search for specific customers based on attributes like name, email, phone number, or any other relevant criteria. Users can also apply filters to narrow down the displayed records based on specific conditions.


- Responsive Design: The user interface is designed to be responsive and accessible across different devices and screen sizes, providing a seamless experience for users on desktop and mobile devices.

## Technologies Used

- Python: The project is built using the Django framework, which is a high-level Python web framework that simplifies the development of web applications.

- Django: Django provides a robust set of tools and features for building web applications, including the ORM (Object-Relational Mapping) for database operations, URL routing, form handling, and user authentication.

- HTML/CSS: The frontend of the application is developed using HTML and CSS, providing the structure, layout, and styling for the user interface.

- Bootstrap: Bootstrap, a popular CSS framework, is used to enhance the frontend design and make the application responsive and visually appealing.

- Database: The project utilizes a database system supported by Django, such as SQLite, PostgreSQL, or MySQL, to store customer records and related data.

## Setup and Installation

To set up the project locally, follow these steps:

1. Clone the repository:

```
git clone [<repository_url>](https://github.com/NatalioF22/CustomerEdge.git)
```

2. Navigate to the project directory:

```
cd django-customer-record-management
```

3. Create a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:
```
venv\Scripts\activate
```

- On macOS and Linux:
```
source venv/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Set up the database:

- Update the database settings in `settings.py` file to configure the database connection and credentials.

- Run migrations to create the necessary database tables:

```
python manage.py migrate
```

7. Start the development server:

```
python manage.py runserver
```

8. Access the application in your web browser:

```
http://localhost:8000
```

## Contribution

Contributions to this project are welcome! If you encounter any issues, have suggestions, or would like to contribute new features or improvements, feel free to submit a pull request or open an issue in the GitHub repository.

Please ensure to follow the established coding style, provide clear commit messages, and adhere to best practices when making contributions.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial projects.

```

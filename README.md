# crud-project
 PostrgeSQL, Django and React interactivity demonstration


**NOTES**

1. **`settings.py`**:
   - This file acts as the central configuration for your Django project. It includes database settings where you define the connection to your PostgreSQL database using the `DATABASES` setting.

2. **`models.py` (in the `tasks` app)**:
   - Here, you define your data models, which Django translates into database tables. For example, a `Task` model will result in a `tasks_task` table in your PostgreSQL database. Each field in the model becomes a column in the table.

3. **`views.py` (in the `tasks` app)**:
   - The views interact with the database through the models. They process incoming HTTP requests, perform operations on the data (like creating, retrieving, updating, or deleting records), and return HTTP responses. Views can render templates or return data, often in JSON format.

4. **`urls.py` (in the `tasks` app and the project's main `urls.py`)**:
   - Both the app-level and project-level `urls.py` define URL patterns. These patterns tell Django how to route incoming HTTP requests to the correct views based on the request URL.

5. **`admin.py` (in the `tasks` app)**:
   - This file is used to register models with the Django admin site, allowing you to manage your database tables (like adding, editing, and deleting tasks) through a user-friendly web interface.

6. **`serializers.py` (in the `tasks` app)**:
   - If you're building an API, serializers convert complex data types, like Django queryset results, to JSON so they can be easily rendered into content types that can be consumed by client-side applications, like your React frontend.

7. **PostgreSQL Database**:
   - This is where all your data is stored. The models you define in Django are used to create tables in PostgreSQL, and any data you add, update, or retrieve through Django's ORM (Object-Relational Mapping) will be reflected here.

So, when you interact with your Django application (e.g., through the React frontend or the Django admin), here's what happens:

- You make a request (like viewing, creating, or deleting a task).
- The request is received by Django and routed to the appropriate view via the URL patterns you've defined.
- The view processes the request, interacts with the model, and performs any necessary actions (like querying or updating the database).
- If the request was for data, a serializer might be used to format the data into JSON.
- The view then returns a response, which could be a web page or JSON data.
- Throughout this process, Django's ORM handles all the communication with the PostgreSQL database, abstracting away the SQL queries you would otherwise have to write manually.

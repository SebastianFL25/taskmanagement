Task Manager API

Summary

The Task Manager API is a web service that allows users to create and manage tasks. Users can create an account, sign in, and view a list of their current tasks. They can also create new tasks, update existing tasks, and mark tasks complete.

Used technology

The API is implemented using the Django rest framework for creating microservices. A sqlite3 database is used to store task and user information. The API also has a Swagger documentation for ease of use.

Requeriments

Before using the project, create an .env file inside the settings folder.
Download the requirements with the command (pip install requirements).

How to use the API

The API can be used through HTTP and JSON calls. The available operations are:

● POST /api/register/: Register a new user. It is required to send the
following information in the body of the request: email (email address
e-mail) and password.

● POST /api/login/: Log in to the API. It is required to send the following
data in the body of the request: email (email address) and password (password). You will receive a valid access token in the response.


For more detailed information about endpoints and the data required, see the Swagger documentation.

Installation and execution

Then clone the repository to build and run the app containers.

git clone https://github.com/{nombre_usuario}/{nombre_repositorio}
cd {nombre_repositorio}

Luego, puede acceder al servidor utilizando la URL http://localhost:8000/.
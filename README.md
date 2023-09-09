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

● GET /api/tasks/: Gets the list of all the tasks of the authenticated user.

● POST /api/tasks/: Create a new task. It is required to send the following
data in the request body: title (task title), description (task description), and due date (due date in YYYY-MM-DD format).

● GET /api/tasks/{task_id}/: Gets the details of a specific task identified by its task_id.

● PUT /api/tasks/{task_id}/ – Updates a specific task identified by its task_id. The following data is required to be sent in the request body: title (optional), description (optional), expiration_date (optional) and status (optional).

● DELETE /api/tasks/{task_id}/: Deletes a specific task identified by its task_id.
additional functionalities

● POST /api/tasks/{task_id}/assign/: Assigns a specific identified task
by its task_id to another user. It is required to send the user_id of the user to whom
the task will be assigned in the request body.

● POST /api/tasks/{task_id}/complete/: Mark a specific task
identified by its task_id as completed.

● GET /api/tasks/stats/: Obtiene estadísticas sobre las tareas del usuario
autenticado, incluyendo la cantidad total de tareas, la cantidad de tareas completadas y la cantidad de tareas pendientes.

For more detailed information about endpoints and the data required, see the Swagger documentation.

Installation and execution

Then clone the repository to build and run the app containers.

git clone https://github.com/{nombre_usuario}/{nombre_repositorio}
cd {nombre_repositorio}

Luego, puede acceder al servidor utilizando la URL http://localhost:8000/.
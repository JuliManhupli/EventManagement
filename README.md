# EventManagement

## Local Development with Docker Compose

This is a Django-based REST API for managing events such as conferences, meetups, and workshops. 
The API allows users to create, view, update, and delete events, as well as register for them. 
Authentication is handled using JWT.

## Features

- **Event Management**: Create, retrieve, update, and delete events.
- **User Authentication**: Register and authenticate users using JWT.
- **Event Registration**: Users can register for events.
- **Filtering**: Filter events by title, location, and date.
- **Email Notifications**: Sends confirmation emails upon event registration.
- **API Documentation**: Swagger-based documentation with `drf-spectacular`.

## Installation

### Prerequisites

- Python 3.11+
- PostgreSQL (or SQLite for development)
- Poetry (for dependency management)

## Steps

**1. Clone the Repository**

Open a terminal and navigate to your desired project directory. Then, clone the repository using the following command:

```bash
git clone https://github.com/JuliManhupli/EventManagement.git
cd EventManagement
```

**2.Create a virtual environment and install dependencies**

```bash
poetry install
```

**3. Setting Up the Environment File**

1. Navigate to the root directory of your project.
2. Create a new file named `.env`.
3. Inside the `.env` file, paste the necessary environment variables specific to your project. These variables will
   likely be in the `.env.ini` format.

**4. Building Docker Containers**

After setting up the `.env` file, run the following command to build the Docker containers defined in your
`docker-compose.yml` file:

```bash
docker-compose build
```

**5. Starting Docker Containers**

Once the build process completes, run the following command to start the Docker containers in detached mode (meaning the
terminal will not be blocked):

```bash
docker-compose up -d
```

**6. Database Migrations**

Apply the migrations to the database within the container:

```bash
docker-compose exec web python manage.py migrate
```

**7. Creating a Superuser (if applicable)**

If your project uses Django and requires a superuser for administrative tasks, run the following command:

```bash
docker-compose exec web python manage.py createsuperuser
```

**8. Accessing the Application**

Once the containers are running, you can access the application at the following URL:

```
http://localhost:8000
```

**9. API Documentation**

You can access API documentation at:

```
http://localhost:8000/api/docs
```

**10. Stopping Docker Containers**

To stop the Docker containers, run the following command:

```bash
docker-compose down
```

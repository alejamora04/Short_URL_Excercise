## Installation & Setup
To run the application repository source code has been containerized using Docker via a compose.yaml file. In order to install and run all dependencies Docker Compose must be installed in the target machine.

### Application Prerequisites 
- Docker Engine
- Docker Compose

### Application Setup
1. Install Docker Compose and Docker Engine by following Docker's documentation for installation instructions depending on your OS.
   
   a. Docker Engine Setup (Optional): Required to modify existing docker containers of the repository.  
   https://docs.docker.com/engine/install/

   b. Docker Compose Installation (Required): Necessary for running application.    
   https://docs.docker.com/compose/install/standalone/  
   **Note: Unless configured within your docker installation all docker commands require sudo permissions!**

3. Clone the git repository and cd into the project root directory.  
    `$ /Short_URL`

5. Build an image of the container reflecting the current state of the project with changes to the source code reflected.  
        `$ docker compose build`

6. Run updated containers for both the database as well as the application.  
       `$ docker compose up -d`
   
7. Apply existing migrations to the Django project database to reflect the state of the database from the command line.
       `$ docker compose exec web python manage.py makemigrations --noinput`

       `$ docker compose exec web python manage.py migrate --noinput`
   
9. Open the running appplication within your web browser via the specified localhost http: port.  
        http://localhost:8000
   
11. To stop any running images.  
        `$ docker compose down`
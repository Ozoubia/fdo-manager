# FDO Manager (API)

## Tables of contents
* Project description
* Features
* API endpoints
* Running with Docker

### Project description
The Fdo manager allows the management of Artifcats following the standards of Schema.org. 

### Features
These are the already implemented features of the Fdo manager
* CRUD operations ()
  * Inserting Artifiacts such as (code, dataset, article, person, organisation...)
  * Modifying existing artifacts.
  * Deleting existing artifacts.
  * Patching existing artifacts.
* .

### API endpoints
List all the available API endpoints and their corresponding HTTP methods. Include a brief description of what each endpoint does. For example:

* `Person`
  * GET: `http://127.0.0.1:8000/getPerson/`
  * POST: `http://127.0.0.1:8000/addPerson/`
  * PUT: `http://127.0.0.1:8000/persons/{id}/`
  * PATCH: `http://127.0.0.1:8000/persons/{id}/patch/`
  * DELETE: `http://127.0.0.1:8000/persons/{id}/delete/`
* `Organisation` 
  * GET: `http://127.0.0.1:8000/getOrganization/`
  * POST: `http://127.0.0.1:8000/addOrganization/`
  * PUT: `http://127.0.0.1:8000/organisation/{id}/`
  * PATCH: `http://127.0.0.1:8000/organisation/{id}/patch/`
  * DELETE: `http://127.0.0.1:8000/organisation/{id}/delete/`
* `CreativeWork`
  * GET: `http://127.0.0.1:8000/getCreativeWork/`
  * POST: `http://127.0.0.1:8000/addCreativeWork/`
  * PUT: `http://127.0.0.1:8000/creativework/{id}/`
  * PATCH: `http://127.0.0.1:8000/creativework/{id}/patch/`
  * DELETE: `http://127.0.0.1:8000/creativework/{id}/delete/`
* `Service`
  * GET: `http://127.0.0.1:8000/getService/`
  * POST: `http://127.0.0.1:8000/addService/`
  * PUT: `http://127.0.0.1:8000/service/{id}/`
  * PATCH: `http://127.0.0.1:8000/service/{id}/patch/`
  * DELETE: `http://127.0.0.1:8000/service/{id}/delete/`
* `WebAPI`
  * GET: `http://127.0.0.1:8000/getWebapi/`
  * POST: `http://127.0.0.1:8000/addWebapi/`
  * PUT: `http://127.0.0.1:8000/webapi/{id}/`
  * PATCH: `http://127.0.0.1:8000/webapi/{id}/patch/`
  * DELETE: `http://127.0.0.1:8000/webapi/{id}/delete/`
* `Software application`
  * GET: `http://127.0.0.1:8000/getSoftwareApp/`
  * POST: `http://127.0.0.1:8000/addSoftwareApp/`
  * PUT: `http://127.0.0.1:8000/softwareApp/{id}/`
  * PATCH: `http://127.0.0.1:8000/softwareApp/{id}/patch/`
  * DELETE: `http://127.0.0.1:8000/softwareApp/{id}/delete/`


### Running with Docker 
to be able to run with docker, a latest version of docker must be installed, then 
please follow the instruction to be able to run it.
* Clone the repository in your local system
* Navigate to the folder in which the docker file exists (FDO api)
* run the following command to start the image (which would start two images; one for Django and one for mysql db)
  * `docker-compose up --build`
* [Optional] : if you need to use the Django admin panel, a superuser must be created such as 
  * Open a command prompt and run `docker ps` to show the running containers; then copy the ID for the fdo app container
  * then you can run this command to create a superuser; you'll get several prompt to choose the username and password.
    * `docker exec -it {fdo container ID} python manage.py createsuperuser`
* you can then access the fdo api dashboard with 
  * `localhost:8000/admin`
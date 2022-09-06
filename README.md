# weBlog -  Student Project

## Local Deployment

Use the [`Main branch`](https://github.com/myportfolio-tech/wcBlog/tree/main) to set up and test the app locally.
The web service is a flask app.
The db service is a postgresql databse.
In this version, both services run on the same host.

----

## Setting up the Project from the github repo

### Before you start:
Ensure docker & docker-compose is intalled in the server [Docker on Ubuntu installation](https://docs.docker.com/engine/install/ubuntu/) 

&nbsp;

1. Clone the [repo ](https://github.com/myportfolio-tech/wcBlog) into the weblog direcotory

```console
git clone git@github.com:myportfolio-tech/wcBlog.git weblog
```
2. Navigate the project folder 
```console
cd weblog
```
3. The docker-compose file pulls images from a public repo.
You <ins>don't need</ins> to build the image with docker-compose

</br>
4. Bownload the images and bring up the containers with
```console
docker-compose up
```
For testing, avoid the -d parameter to troubleshoot flask requests on the command line.


### Test the app locally

Check the app is running [`locally`](http://localhost:5000).
&nbsp;
You should be able to:

1. Register
2. Sign in
3. Create a post
4. Edit a post
4. Reset password

### Volumes
    
The docker-compose file sets up a persistant volume. 
```console
    volumes:
      - postgres_data:/var/lib/postgresql/data/ 
```

Stop the conatiners and restart them.
Test that users and posts are still available.


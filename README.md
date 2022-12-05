# docker-demo


## Docker
### Installation
* https://docs.docker.com/get-docker/

### Container
* web: Python Django web application
* db: PostgreSQL database

### Commands
```
docker compose build
docker compose up -d

docker compose ps
docker compose logs web --follow

docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```

## Web Application Endpoints

```
localhost:8000/api (GET, POST)

POST request data for creating a `DanceClass` record
{
    "teacher": "Jose",
    "location": "Long Beach",
    "date": "2022-11-10T19:00:00"
}
```

The `POST` endpoint returns an error when attempting to create a duplicate `DanceClass` record

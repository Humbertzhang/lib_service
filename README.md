# lib_service

## Deploy

1. Configure Environment File

**Deploy Environment FILE (container.env)**

```
REST_MONGO_HOST=<Book Attention MongoDB host>
REST_MONGO_PORT=<MongoDB port>
PROXY=OFF
```

2. Run

```
docker-compose stop && docker-compose build && dockder-compose up -d && docker-compose ps
```

## Test

1. Configure Environment File

**Test Environment FILE (container.test.env)**

```
REST_MONGO_HOST=<Book Attention MongoDB host>
REST_MONGO_PORT=<MongoDB port>
SID=<Library Student ID>
PASSWD=123456<Library Password>
PROXY=OFF
```

2. Run

```
./start_test.sh && docker-compose -f docker-compose.test.yml logs --tail="100" lib_api_test
```

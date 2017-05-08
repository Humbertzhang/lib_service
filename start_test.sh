#!/bin/sh

docker-compose -f docker-compose.test.yml stop
docker-compose -f docker-compose.test.yml build
docker-compose -f docker-compose.test.yml up
docker-compose -f docker-compose.test.yml logs lib_api_test

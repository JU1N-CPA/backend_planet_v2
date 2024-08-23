run-db:
	docker run --name mongo-db --env-file .env.docker -p 27017:27017 mongo

create-migrations:
	docker-compose exec admin python manage.py makemigrations

run-migrations:
	docker-compose exec admin python manage.py migrate

run:
	docker-compose up -d

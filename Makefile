.PHONY = all build

all: build

build:
	docker build -t guystlr/php-apache:7.2 -t guystlr/php-apache:latest 7.2
	docker build -t guystlr/php-apache:7.2-symfony 7.2-symfony
	docker build -t guystlr/php-apache:5.6 5.6

publish:
	docker push guystlr/php-apache

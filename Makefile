.PHONY = all build

all: build

build:
	docker build -t silarhi/php-apache:7.2 -t silarhi/php-apache:latest 7.2
	docker build -t silarhi/php-apache:7.2-symfony 7.2-symfony
	docker build -t silarhi/php-apache:5.6 5.6

publish:
	docker push silarhi/php-apache

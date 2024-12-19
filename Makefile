.PHONY = all build publish update
DOCKER_BUILDER = docker buildx build --platform linux/arm64/v8,linux/amd64
DOCKER_BUILD_AND_PUSH = $(DOCKER_BUILDER) --push --pull

all: build

update:
	./update.sh

build: update
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.4 -t silarhi/php-apache:latest 8.4
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.4-frankenphp-alpine 8.4-frankenphp-alpine
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.4-frankenphp-bookworm 8.4-frankenphp-bookworm
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.4-symfony 8.4-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.3 8.3
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.3-frankenphp-alpine 8.3-frankenphp-alpine
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.3-frankenphp-bookworm 8.3-frankenphp-bookworm
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.3-symfony 8.3-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.2 8.2
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.2-ci 8.2-ci
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.2-frankenphp-alpine 8.2-frankenphp-alpine
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.2-frankenphp-bookworm 8.2-frankenphp-bookworm
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.2-symfony 8.2-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.1 8.1
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.1-ci 8.1-ci
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.1-symfony 8.1-symfony

build-legacy: update
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.0 8.0
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.0-ci 8.0-ci
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:8.0-symfony 8.0-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.4 7.4
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.4-ci 7.4-ci
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.4-symfony 7.4-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.3 7.3
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.3-symfony 7.3-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.2 7.2
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.2-symfony 7.2-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.1 7.1
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:7.1-symfony 7.1-symfony
	$(DOCKER_BUILD_AND_PUSH) -t silarhi/php-apache:5.6 5.6

publish:
	docker push silarhi/php-apache --all-tags

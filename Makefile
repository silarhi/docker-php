.PHONY = all build publish update

all: build

update:
	./update.sh

build:
	$(update)
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.3 --no-cache -t silarhi/php-apache:latest 8.3
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.3-frankenphp-alpine 8.3-frankenphp-alpine
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.3-frankenphp-bookworm 8.3-frankenphp-bookworm
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.3-symfony 8.3-symfony
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.2 8.2
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.2-ci 8.2-ci
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.2-frankenphp-alpine 8.2-frankenphp-alpine
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.2-frankenphp-bookworm 8.2-frankenphp-bookworm
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.2-symfony 8.2-symfony
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.1 8.1
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.1-ci 8.1-ci
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.1-symfony 8.1-symfony

build-legacy:
	$(update)
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.0 8.0
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.0-ci 8.0-ci
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:8.0-symfony 8.0-symfony
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.4 7.4
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.4-ci 7.4-ci
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.4-symfony 7.4-symfony
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.3 7.3
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.3-symfony 7.3-symfony
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.2 7.2
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.2-symfony 7.2-symfony
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.1 7.1
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:7.1-symfony 7.1-symfony
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --no-cache -t silarhi/php-apache:5.6 5.6

publish:
	docker push silarhi/php-apache --all-tags

FROM dunglas/frankenphp:1-php8.2-alpine

EXPOSE 80
WORKDIR /app

HEALTHCHECK --interval=1m --timeout=3s --start-period=5s --start-interval=1s --retries=3 \
    CMD curl -f http://localhost:2019/metrics || exit 1

ENV COMPOSER_ALLOW_SUPERUSER=1
ENV SERVER_NAME=:80

# git, unzip & zip are for composer
RUN apk add --no-cache \
    git \
    gnupg \
    unzip \
    zip

# PHP Extensions
RUN install-php-extensions @composer opcache pdo_mysql

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
COPY --link conf/php.ini $PHP_INI_DIR/conf.d/app.ini

# Caddy
COPY --link conf/Caddyfile /etc/caddy/Caddyfile
COPY --link conf/symfony-worker.Caddyfile /etc/caddy/symfony-worker.Caddyfile
COPY --link index.php /app/public/index.php

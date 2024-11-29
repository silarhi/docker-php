FROM dunglas/frankenphp:1-php8.2-bookworm

EXPOSE 80
WORKDIR /app

HEALTHCHECK CMD curl -f http://localhost || exit 1

ENV COMPOSER_ALLOW_SUPERUSER=1
ENV SERVER_NAME=:80

# git, unzip & zip are for composer
RUN apt-get update -qq && \
    apt-get install -qy \
    git \
    gnupg \
    unzip \
    zip && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# PHP Extensions
RUN install-php-extensions opcache pdo_mysql

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
COPY conf/php.ini $PHP_INI_DIR/conf.d/app.ini

# Caddy
COPY --link conf/Caddyfile /etc/caddy/Caddyfile
COPY index.php /app/public/index.php

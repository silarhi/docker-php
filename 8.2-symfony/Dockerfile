FROM php:8.2-apache

ENV COMPOSER_ALLOW_SUPERUSER=1

EXPOSE 80
WORKDIR /app

HEALTHCHECK --interval=1m --timeout=3s --start-period=5s --start-interval=1s --retries=3 \
    CMD curl -f http://localhost/_health || exit 1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update -qq && \
    apt-get install -qy \
    git \
    gnupg \
    libicu-dev \
    libzip-dev \
    unzip \
    zip \
    zlib1g-dev && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/log/*

# PHP Extensions
RUN docker-php-ext-configure zip && \
    docker-php-ext-install -j"$(nproc)" intl opcache pdo_mysql zip
COPY --link conf/php.ini /usr/local/etc/php/conf.d/app.ini

# Apache
COPY --link errors /errors
COPY --link health.php /health/index.php
COPY --link conf/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY --link conf/apache.conf /etc/apache2/conf-available/z-app.conf
COPY --link index.php /app/index.php

RUN a2enmod rewrite remoteip && \
    a2enconf z-app

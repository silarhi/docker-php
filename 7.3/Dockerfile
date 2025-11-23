FROM mlocati/php-extension-installer:latest AS php-extension-installer
FROM php:7.3-apache-stretch

ENV COMPOSER_ALLOW_SUPERUSER=1

EXPOSE 80
WORKDIR /app

HEALTHCHECK --interval=1m --timeout=3s --start-period=5s --start-interval=1s --retries=3 \
    CMD curl -f http://localhost/_health || exit 1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

#Update stretch repositories
RUN sed -i s/deb.debian.org/archive.debian.org/g /etc/apt/sources.list && \
    sed -i 's|security.debian.org|archive.debian.org/|g' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list

# git, unzip & zip are for composer
RUN apt-get update -qq && \
    apt-get install -qy \
    git \
    gnupg \
    iputils-ping \
    libicu-dev \
    unzip \
    zip && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/log/*

# PHP Extensions
COPY --from=php-extension-installer /usr/bin/install-php-extensions /usr/local/bin/
RUN install-php-extensions opcache pdo_mysql
COPY --link conf/php.ini /usr/local/etc/php/conf.d/app.ini

# Apache
COPY --link errors /errors
COPY --link health.php /health/index.php
COPY --link conf/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY --link conf/apache.conf /etc/apache2/conf-available/z-app.conf
COPY --link index.php /app/index.php

RUN a2enmod rewrite remoteip && \
    a2enconf z-app

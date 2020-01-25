FROM php:7.4-apache

ENV COMPOSER_ALLOW_SUPERUSER=1

WORKDIR /app
EXPOSE 80

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
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# PHP Extensions
RUN docker-php-ext-configure zip && \
	docker-php-ext-install -j$(nproc) opcache pdo_mysql intl zip
COPY conf/php.ini /usr/local/etc/php/conf.d/app.ini

# Apache
COPY errors /errors
RUN a2enmod rewrite remoteip
COPY conf/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY conf/apache.conf /etc/apache2/conf-available/z-app.conf
RUN a2enconf z-app
COPY index.php /app/index.php

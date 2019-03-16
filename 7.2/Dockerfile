FROM php:7.2-apache

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    gnupg \
    iputils-ping \
    libicu-dev \
    nano \
    ssh \
    unzip \
    wget \
    zip

# Composer
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer --version

# BashRC
RUN echo 'export LS_OPTIONS="--color=auto"' >> ~/.bashrc
RUN echo 'eval "`dircolors`"' >> ~/.bashrc
RUN echo 'alias ls="ls --color=auto"' >> ~/.bashrc
RUN echo 'alias ll="ls -alF"' >> ~/.bashrc

# PHP Extensions
RUN docker-php-ext-install intl opcache pdo pdo_mysql
ADD conf/php.ini /usr/local/etc/php/conf.d/app.ini

# Apache
ADD errors /errors
RUN a2enmod rewrite remoteip
ADD conf/vhost.conf /etc/apache2/sites-available/000-default.conf
ADD conf/apache.conf /etc/apache2/conf-available/z-app.conf
RUN a2enconf z-app
ADD index.php /app/index.php

WORKDIR /app
EXPOSE 80
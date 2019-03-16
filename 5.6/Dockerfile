FROM php:5.6-apache

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    gnupg \
    iputils-ping \
    libicu-dev \
    locales \
    nano \
    wget \
    unzip \
    zip

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN composer --version

# BashRC
RUN echo 'alias ls="ls --color=auto"' >> ~/.bashrc
RUN echo 'alias ll="ls -alF"' >> ~/.bashrc

# Locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
RUN sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen
RUN locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8


# PHP Extensions
RUN docker-php-ext-install pdo pdo_mysql 
RUN docker-php-ext-install opcache 
RUN docker-php-ext-install intl
ADD conf/app.ini /usr/local/etc/php/conf.d/app.ini

# Apache
ADD app.conf /etc/apache2/sites-available/000-default.conf
ADD conf/app.conf /etc/apache2/conf-available/app.conf
RUN a2enconf app
ADD index.php /app/index.php

WORKDIR /app
EXPOSE 80
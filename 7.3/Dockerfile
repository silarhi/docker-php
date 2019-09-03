FROM php:7.3-apache-stretch

ENV COMPOSER_ALLOW_SUPERUSER=1

EXPOSE 80
WORKDIR /app

# git, unzip & zip are for composer
RUN apt-get update -q && \
    apt-get install -qy \
    git \
    gnupg \
    iputils-ping \
    libicu-dev \
    unzip \
    zip && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# PHP Extensions
RUN docker-php-ext-install -j$(nproc) opcache pdo_mysql
ADD conf/php.ini /usr/local/etc/php/conf.d/app.ini

# Apache
ADD errors /errors
RUN a2enmod rewrite remoteip
ADD conf/vhost.conf /etc/apache2/sites-available/000-default.conf
ADD conf/apache.conf /etc/apache2/conf-available/z-app.conf
RUN a2enconf z-app
ADD index.php /app/index.php
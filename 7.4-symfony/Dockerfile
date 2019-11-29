FROM php:7.4-apache

WORKDIR /app
EXPOSE 80

RUN apt-get update -qq && \
    apt-get install -qy \
    libicu-dev \
    libzip-dev \
    zlib1g-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# PHP Extensions
RUN docker-php-ext-configure zip && \
	docker-php-ext-install -j$(nproc) opcache pdo_mysql intl zip
ADD conf/php.ini /usr/local/etc/php/conf.d/app.ini

# Apache
ADD errors /errors
RUN a2enmod rewrite remoteip
ADD conf/vhost.conf /etc/apache2/sites-available/000-default.conf
ADD conf/apache.conf /etc/apache2/conf-available/z-app.conf
RUN a2enconf z-app
ADD index.php /app/index.php
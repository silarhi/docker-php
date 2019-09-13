FROM silarhi/php-apache:7.2

WORKDIR /app
EXPOSE 80

RUN apt-get update -qq && \
    apt-get install -qy \
    libzip-dev \
    zlib1g-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# PHP Extensions
RUN docker-php-ext-configure zip --with-libzip && \
	docker-php-ext-install -j$(nproc) intl zip

# Apache
ADD conf/vhost.conf /etc/apache2/sites-available/000-default.conf

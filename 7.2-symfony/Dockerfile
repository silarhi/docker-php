FROM guystlr/php-apache:7.2

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    zlib1g-dev

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# PHP Extensions
RUN docker-php-ext-install zip

# Apache
ADD conf/vhost.conf /etc/apache2/sites-available/000-default.conf

WORKDIR /app
EXPOSE 80
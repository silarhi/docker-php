FROM guystlr/php-apache:7.2

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    zlib1g-dev && \
	curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    npm install -g yarn && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# PHP Extensions
RUN docker-php-ext-install -j$(nproc) intl zip

# Apache
ADD conf/vhost.conf /etc/apache2/sites-available/000-default.conf

WORKDIR /app
EXPOSE 80
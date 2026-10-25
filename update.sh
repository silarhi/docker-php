#!/bin/bash

set -e

for version in *; do
	[ -d "$version" ] || continue
	[[ "$version" != "_shared" ]] || continue
	[[ "$version" != *"-ci" ]] || continue

	# index.php needs PHP 8: the legacy PHP 5/7 images keep their own
	if [[ "$version" == 5.* || "$version" == 7.* ]]; then
		find _shared -mindepth 1 -maxdepth 1 ! -name index.php -exec cp -R {} "$version" \;
	else
		cp -R _shared/* "$version"
	fi

	if [[ "$version" == *"-symfony"* ]]; then
		mv "$version/conf/vhost-symfony.conf" "$version/conf/vhost.conf"
	else
		rm "$version/conf/vhost-symfony.conf"
	fi

	if [[ "$version" != *"-frankenphp"* ]]; then
    rm "$version/conf/Caddyfile" "$version/conf/symfony-worker.Caddyfile" "$version/conf/symfony-worker-native.Caddyfile"
  else
    rm "$version/conf/apache.conf" "$version/conf/vhost.conf"
    rm -rf "$version/errors"
  fi
done

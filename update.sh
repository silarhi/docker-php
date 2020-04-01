#/bin/bash

set -e

for version in *; do
	[ -d "$version" ] || continue
	[[ "$version" != "_shared" ]] || continue
	cp -R _shared/* "$version"

	if [[ "$version" == *"-symfony"* ]]; then
		mv "$version/conf/vhost-symfony.conf" "$version/conf/vhost.conf"
	else
		rm "$version/conf/vhost-symfony.conf"
	fi
done
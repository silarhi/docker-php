<?php

declare(strict_types=1);

// Default page of the silarhi/php-apache images (same as https://labs.silarhi.fr/php): shows what the image provides
// without the full phpinfo(), which would publish the environment variables (often secrets), paths and build flags.

$h = static fn (mixed $value): string => htmlspecialchars((string) $value, \ENT_QUOTES);
$bool = static fn (mixed $value): string => filter_var($value, \FILTER_VALIDATE_BOOL) ? 'On' : 'Off';

$isFrankenPhp = 'frankenphp' === \PHP_SAPI;
$server = $isFrankenPhp ? 'FrankenPHP' : 'Apache';
if (!$isFrankenPhp && function_exists('apache_get_version')) {
    $server = apache_get_version() ?: $server;
}

$opcache = function_exists('opcache_get_status') ? (opcache_get_status(false) ?: []) : [];

$sections = [
    'Runtime' => [
        'PHP version' => \PHP_VERSION,
        'Server' => $server,
        'SAPI' => \PHP_SAPI,
        'OS' => php_uname('s').' '.php_uname('m'),
        'Timezone' => date_default_timezone_get(),
    ],
    'Request' => [
        'Client IP (REMOTE_ADDR)' => $_SERVER['REMOTE_ADDR'] ?? '',
        'HTTPS' => ($_SERVER['HTTPS'] ?? '') ?: 'off',
        'Host' => $_SERVER['HTTP_HOST'] ?? '',
        'Protocol' => $_SERVER['SERVER_PROTOCOL'] ?? '',
        'Method' => $_SERVER['REQUEST_METHOD'] ?? '',
        'URI' => $_SERVER['REQUEST_URI'] ?? '',
    ],
    'Configuration' => [
        'memory_limit' => ini_get('memory_limit'),
        'max_execution_time' => ini_get('max_execution_time'),
        'upload_max_filesize' => ini_get('upload_max_filesize'),
        'post_max_size' => ini_get('post_max_size'),
        'display_errors' => $bool(ini_get('display_errors')),
        'expose_php' => $bool(ini_get('expose_php')),
    ],
    'OPcache' => [
        'Enabled' => $bool($opcache['opcache_enabled'] ?? false),
        'JIT' => $bool($opcache['jit']['on'] ?? false),
        'Validate timestamps' => $bool(ini_get('opcache.validate_timestamps')),
        // FrankenPHP can report a negative used_memory
        'Memory used' => ($opcache['memory_usage']['used_memory'] ?? -1) >= 0
            ? round($opcache['memory_usage']['used_memory'] / 1024 / 1024, 1).' MB'
            : 'n/a',
    ],
];

$extensions = get_loaded_extensions();
natcasesort($extensions);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex">
    <title>PHP <?= $h(\PHP_VERSION) ?> · <?= $h($isFrankenPhp ? 'FrankenPHP' : 'Apache') ?> · silarhi/php-apache</title>
    <style>
        :root { color-scheme: light dark; --bg: #f6f8fb; --card: #fff; --fg: #1d273b; --muted: #667382; --border: #e6e7e9; --accent: #4f5b93; }
        @media (prefers-color-scheme: dark) { :root { --bg: #151f2c; --card: #1d2a3a; --fg: #e6e9ef; --muted: #9aa0ac; --border: #2c3a4d; --accent: #8892bf; } }
        * { box-sizing: border-box; }
        body { margin: 0; padding: 2rem 1rem; background: var(--bg); color: var(--fg); font: 15px/1.5 system-ui, -apple-system, sans-serif; }
        main { max-width: 960px; margin: 0 auto; }
        header { margin-bottom: 1.5rem; }
        h1 { margin: 0; font-size: 1.75rem; }
        h1 span { color: var(--accent); }
        header p { margin: .25rem 0 0; color: var(--muted); }
        a { color: var(--accent); }
        .grid { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); }
        section { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 1rem 1.25rem; }
        h2 { margin: 0 0 .5rem; font-size: .8rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
        dl { display: grid; grid-template-columns: max-content 1fr; gap: .35rem 1rem; margin: 0; }
        dt { color: var(--muted); }
        dd { margin: 0; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .9em; overflow-wrap: anywhere; }
        .extensions { margin-top: 1rem; }
        ul { display: flex; flex-wrap: wrap; gap: .4rem; margin: 0; padding: 0; list-style: none; }
        li { padding: .1rem .5rem; border: 1px solid var(--border); border-radius: 4px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .85em; }
        footer { margin-top: 1.5rem; color: var(--muted); font-size: .9em; }
    </style>
</head>
<body>
<main>
    <header>
        <h1>PHP <span><?= $h(\PHP_VERSION) ?></span> on <?= $h($isFrankenPhp ? 'FrankenPHP' : 'Apache') ?></h1>
        <p>Running the <code>silarhi/php-apache</code> Docker image. Copy your application into the image to replace this page.</p>
    </header>

    <div class="grid">
        <?php foreach ($sections as $title => $rows) { ?>
            <section>
                <h2><?= $h($title) ?></h2>
                <dl>
                    <?php foreach ($rows as $label => $value) { ?>
                        <dt><?= $h($label) ?></dt>
                        <dd><?= $h($value) ?></dd>
                    <?php } ?>
                </dl>
            </section>
        <?php } ?>
    </div>

    <section class="extensions">
        <h2>Extensions (<?= count($extensions) ?>)</h2>
        <ul>
            <?php foreach ($extensions as $extension) { ?>
                <li><?= $h($extension) ?></li>
            <?php } ?>
        </ul>
    </section>

    <footer>
        Sources: <a href="https://github.com/silarhi/docker-php">silarhi/docker-php</a>
        · Images: <a href="https://hub.docker.com/r/silarhi/php-apache">Docker Hub</a>
        · <a href="https://blog.silarhi.fr/image-docker-php-apache-parfaite/">Blog post</a>
        · Demo: <a href="https://labs.silarhi.fr/php">labs.silarhi.fr</a>
    </footer>
</main>
</body>
</html>

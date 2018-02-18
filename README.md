# monit

`monit` is a small Open Source utility for managing and monitoring Unix systems. Monit conducts automatic maintenance and repair and can execute meaningful causal actions in error situations.

This makes it an easy-to-use alternative to Icinga2 in simple setups.

## Maintenance notice

As of February 2018 this bundle will not be mainained anymore. If you encounter any issues I cannot help.

## Integrations

* Bundles:
  * [collectd](https://github.com/rullmann/bundlewrap-collectd)
  * [jenkins](https://github.com/rullmann/bundlewrap-jenkins)
  * [openssh](https://github.com/rullmann/bundlewrap-openssh)
  * [php-fpm](https://github.com/rullmann/bundlewrap-php)
  * [postgresql](https://github.com/rullmann/bundlewrap-postgresql)

## Metadata

    'metadata': {
        'monit': {
          'alert_email': 'root@example.org', # optional, if not set alerts are send to `root@localhost`
          'email_from': 'monit@localhost', # optional, but required in a secure mail server setup
          'load_check': True, # optional, True by default. Alerts if load is high
          'disk_check': False, # optional, False by default. Enable and set disks metadata to enable disk space checks
          'load_check': True, optional, True by default. Disable for nodes where load checks are annoying
          'disable_notification_time': False, # optional, False by default. Enable if you want to stop monit at some point of the day, e.g. when backups occur
          'disable_stop_time': "0 2 * * *", # optional, set to a specific time when monit should be stopped when `disable_notification_time` is set to True
          'disable_start_time': "0 3 * * *", # optional, set to a specific time when monit should be started again when `disable_notification_time` is set to True
        },
        'disks': { # optional, enable a disk check
            'root': '/',
            'data': '/var/opt/mydata',
        },
    }

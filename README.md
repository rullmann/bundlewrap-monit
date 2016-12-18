# monit

`monit` is a small Open Source utility for managing and monitoring Unix systems. Monit conducts automatic maintenance and repair and can execute meaningful causal actions in error situations.

This makes it an easy-to-use alternative to Icinga2 in simple setups.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| Fedora 24   | `[x]` |
| Fedberry 24 | `[x]` |
| Fedora 25   | `[x]` |

## Integrations

* Bundles:
  * [collectd](https://github.com/rullmann/bundlewrap-collectd)
  * [jenkins](https://github.com/rullmann/bundlewrap-jenkins)

## Metadata

    'metadata': {
        'monit': {
          'alert_email': 'root@example.org', # optional, if not set alerts are send to `root@localhost`
          'email_from': 'monit@localhost', # optional, but required in a secure mail server setup
          'load_check': True, # optional, True by default. Alerts if load is high
        },
        'disks': { # optional, enable a disk check
            'root': '/',
            'data': '/var/opt/mydata',
        },
    }

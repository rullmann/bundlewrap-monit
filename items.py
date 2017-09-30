pkg_dnf = {
    'monit': {},
}

svc_systemd = {
    'monit': {
        'needs': ['pkg_dnf:monit', 'file:/etc/monitrc'],
    },
}

files = {
    '/etc/monitrc': {
        'source': 'monitrc',
        'mode': '0700',
        'content_type': 'mako',
        'needs': ['pkg_dnf:monit'],
        'triggers': ['svc_systemd:monit:restart'],
    },
    '/etc/monit.d/system': {
        'source': 'system',
        'mode': '0700',
        'content_type': 'mako',
        'needs': ['pkg_dnf:monit'],
        'triggers': ['svc_systemd:monit:restart'],
    },
}

if node.metadata.get('monit', {}).get('disable_notification_time', False):
    files['/etc/cron.d/monit'] = {
        'content_type': 'mako',
        'source': 'crond',
        'mode': '0644',
        'needs': ['pkg_dnf:monit'],
    }
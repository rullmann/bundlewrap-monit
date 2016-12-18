pkg_dnf = {
    'monit': {},
}

svc_systemd = {
    'monit': {
        'enabled': True,
        'needs': [
            "pkg_dnf:monit",
            "file:/etc/monitrc",
        ],
    },
}

files = {
    '/etc/monitrc': {
        'source': "monitrc",
        'owner': "root",
        'mode': "0700",
        'content_type': "mako",
        'needs': [
            "pkg_dnf:monit",
        ],
        'triggers': [
            "svc_systemd:monit:restart",
        ],
    },
    '/etc/monit.d/system': {
        'source': "system",
        'owner': "root",
        'mode': "0700",
        'content_type': "mako",
        'needs': [
            "pkg_dnf:monit",
        ],
        'triggers': [
            "svc_systemd:monit:restart",
        ],
    },
}

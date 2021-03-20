"""Role testing files using testinfra"""


import pytest


@pytest.mark.parametrize("config", [
    ("auth \"on\""),
    ("syslog \"on\""),
    ("tls \"on\""),
    ("account \"gmail\""),
    ("host \"smtp.gmail.com\""),
    ("port \"587\""),
    ("from \"username@gmail.com\""),
    ("user \"username\""),
    ("password \"plain-text-password\""),
    ("account default :gmail")
])
def test_msmtp_config(host, config):
    """Check msmtp config file"""
    f = host.file("/etc/msmtprc")
    assert config in f.content_string


def test_sendmail_command(host):
    """Check sendmail command"""
    f = host.file("/usr/sbin/sendmail")

    assert f.is_symlink
    assert f.linked_to == "/usr/bin/msmtp"

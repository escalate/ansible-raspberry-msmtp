[![Test](https://github.com/escalate/ansible-raspberry-msmtp/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-msmtp/actions/workflows/test.yml)

# Ansible Role: Raspberry - msmtp

An Ansible role that manages [msmtp](https://marlam.de/msmtp/) on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-msmtp/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

- Roles: None
- Collections: None

## Installation

```
$ ansible-galaxy role install escalate.msmtp
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.msmtp
      tags: msmtp
```

## License

MIT

# Ansible Role: Raspberry - msmtp

[![CI](https://github.com/escalate/ansible-raspberry-msmtp/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/escalate/ansible-raspberry-msmtp/actions/workflows/ci.yml)

An Ansible role that manages [msmtp](https://marlam.de/msmtp/) on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.msmtp
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-msmtp/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.msmtp
      tags: msmtp
```

## License

MIT

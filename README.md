# Ansible Role: Self-signed certificate

An Ansible Role that generates a TSL/SSL self-signed certificate.

## Requirements

None.

## Role Variables

None.

# Dependencies

None.

# Example Playbook

```yaml
- name: Generate self-signed certificate
  hosts: all
  roles:
    - hadrienpatte.self_signed_certificate
```

## License

MIT

## Author Information

Hadrien Patte [![PGP 0xFB500BB0](https://peegeepee.com/badge/orange/FB500BB0.svg)](https://peegeepee.com/FB500BB0)

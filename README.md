# Ansible Role: Self-signed certificate

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-self-signed-certificate.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-self-signed-certificate)

An Ansible Role that generates a TSL/SSL self-signed certificate.

## Requirements

None.

## Role Variables

* `self_signed_certificate_FQDN`: your Fully Qualified Domain Name

### Private key variables

* `self_signed_certificate_key_path`: directory where the private key will be
* `self_signed_certificate_key_type`: private key type, can be `RSA` (default)
  or `DSA`
* `self_signed_certificate_key_size`: private key bits, defaults to `4096`

### Certificate Signing Request variables

* `self_signed_certificate_csr_path`: directory where the certificate signing
  request will be
* `self_signed_certificate_csr_digest`: certificate signing request digest,
  defaults to `sha512`
* `self_signed_certificate_email`: certificate signing request email address (E)
* `self_signed_certificate_domains`: list of domains for the certificate signing
  request (CN)
* `self_signed_certificate_city`: certificate signing request locality name (L)
* `self_signed_certificate_state`: certificate signing request state or province
  name (ST)
* `self_signed_certificate_country`: certificate signing request country name
  (C)
* `self_signed_certificate_organisation`: certificate signing request
  organization name (O)
* `self_signed_certificate_organizational_unit`: certificate signing request
  organizational unit name (OU)

### Certificate variables

* `self_signed_certificate_path`: directory where the certificate will be
* `self_signed_certificate_digest`: certificate digest, defaults to `sha512`
* `self_signed_certificate_days_valid`: number of days the certificate will be
  valid, defaults to `3650` (ten years)

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

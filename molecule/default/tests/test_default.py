import os

import testinfra.utils.ansible_runner

import pytest

from cryptography import x509

from cryptography.hazmat.backends import default_backend

from cryptography.x509 import oid

from cryptography.hazmat.primitives.asymmetric import rsa

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_certificate(host):
    file = host.file('/etc/ssl/private/a.example.com/fullchain.pem')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_certificate_common_name(host):
    cert = x509.load_pem_x509_certificate(
        host.file('/etc/ssl/private/a.example.com/fullchain.pem').content,
        default_backend(),
    )
    assert (
        cert.subject.get_attributes_for_oid(oid.NameOID.COMMON_NAME)[0].value
        == 'a.example.com'
    )


def test_certificate_email_address(host):
    cert = x509.load_pem_x509_certificate(
        host.file('/etc/ssl/private/a.example.com/fullchain.pem').content,
        default_backend(),
    )
    assert (
        cert.subject.get_attributes_for_oid(oid.NameOID.EMAIL_ADDRESS)[0].value
        == 'admin@a.example.com'
    )


@pytest.mark.parametrize('fqdn', [
    ('a.example.com'),
    ('b.example.com'),
])
def test_certificate_subject_alternative_name(host, fqdn):
    cert = x509.load_pem_x509_certificate(
        host.file('/etc/ssl/private/a.example.com/fullchain.pem').content,
        default_backend(),
    )
    assert fqdn in cert.extensions.get_extension_for_oid(
        oid.ExtensionOID.SUBJECT_ALTERNATIVE_NAME
    ).value.get_values_for_type(x509.DNSName)


def test_certificate_public_key(host):
    cert = x509.load_pem_x509_certificate(
        host.file('/etc/ssl/private/a.example.com/fullchain.pem').content,
        default_backend(),
    )
    assert isinstance(cert.public_key(), rsa.RSAPublicKey)
    assert cert.public_key().key_size == 4096

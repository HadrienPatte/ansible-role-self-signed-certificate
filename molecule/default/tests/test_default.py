import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_file(host):
    file = host.file('/etc/letsencrypt/live/example.com/fullchain.pem')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_certificate(host):
    output = host.check_output(
        'openssl x509 -in /etc/letsencrypt/live/example.com/fullchain.pem' +
        ' -text -noout')
    assert ('Subject: CN = example.com, emailAddress = admin@example.com'
            in output)
    assert 'Public-Key: (4096 bit)' in output

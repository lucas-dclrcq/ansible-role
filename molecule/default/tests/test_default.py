import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/opt/keycloak')

    assert f.exists
    assert f.user == 'keycloak'
    assert f.group == 'keycloak'

import requests
import json


def delete_folder(name, domain=None, username=None, password=None,
                 method=None, test_path=None):
    if domain is None:
        domain = 'https://istepanko29.qa-egnyte.com'
    if username is None:
        username = 'admin'
    if password is None:
        password = 'apitest2'
    if method is None:
        method = 'DELETE'
    if test_path is None:
        test_path = '/Shared/smoke_test/'

    endpoint = '/public-api/v1/fs'
    url = domain + endpoint + test_path + name
    r = requests.request(
        url=url,
        auth=(username, password),
        method=method
    )
    return r

for i in range(1000):
    resp = delete_folder(name='test%s' % i)
    print('\n'
          'Folder %s deleted!\n'
          'Data:'
          '\n'
          '%s'
          '\n'
          'Status_code:'
          '\n'
          '%s' % (resp.content, resp.status_code, i))
from __future__ import print_function
try:
    from urlparse import urlparse
except:
    from urllib.parse import urlparse

from hypothesis import given  #, reject
from hypothesis.strategies import text

url = 'mysql://user:password@localhost:3306/thedatabase?auto_reconnect=1&connection_timeout=100'


# from: https://github.com/dbcli/pgcli/blob/master/pgcli/main.py#L278
# def parse_uri(self, uri):
def parse_uri(uri):
    uri = urlparse(uri)
    database = uri.path[1:]  # ignore the leading fwd slash
    arguments = {}
    if database is not None and len(database) > 0:
        arguments['database'] = database
    if uri.hostname is not None:
        arguments['host'] = uri.hostname
    if uri.hostname is not None:
        arguments['user'] = uri.username
    if uri.port is not None:
        arguments['port'] = uri.port
    if uri.password is not None:
        arguments['password'] = uri.password

    print(arguments)

    # unquote each URI part (they may be percent encoded)
    # self.connect(*list(map(lambda p: unquote(str(p)) if p else p, arguments)))
    return arguments


@given(text())
def test_connect(url):
    result = parse_uri(url)
    assert result is not None
    assert isinstance(result, dict)
    assert len(result) == 0

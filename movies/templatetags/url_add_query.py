from urlparse import urlsplit, urlunsplit
from django import template
from django.http import QueryDict


register = template.Library()

@register.simple_tag
def url_add_query(url, **kwargs):
    """
    Lets you append a querystring to a url.

    If the querystring argument is already present it will be replaced
    otherwise it will be appended to the current querystring.

    > url = 'http://example.com/?query=test'
    > url_add_query(url, query='abc', foo='bar')
    'http://example.com/?query=abc&foo=bar'

    It also works with relative urls.

    > url = '/foo/?page=1'
    > url_add_query(url, query='abc')
    '/foo/?query=abc&page=1'

    and blank strings

    > url = ''
    > url_add_query(url, page=2)
    '?page=2'
    """

    parsed = urlsplit(url)
    querystring = QueryDict(parsed.query.encode('utf-8'), mutable=True)
    querystring.update(kwargs)
    return urlunsplit(parsed._replace(query=querystring.urlencode()))
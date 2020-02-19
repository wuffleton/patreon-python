from collections import OrderedDict
from six.moves.urllib.parse import urlencode


def joined_or_null(arr):
    return "null" if len(arr) == 0 else ','.join(arr)


def build_url(path, includes=None, fields=None, filters=None):
    connector = '&' if '?' in path else '?'
    params = {}

    if includes:
        params.update({'include': joined_or_null(includes)})

    if fields:
        params.update(
            {
                "fields[{resource_type}]".format(resource_type=resource_type):
                joined_or_null(attributes)
                for resource_type, attributes in fields.items()
            }
        )

    if filters:
        params.update(
            {
                "filter[{resource_type}]".format(resource_type=resource_type):
                attributes
                for resource_type, attributes in filters.items()
            }
        )    
        
    if not params:
        return path

    sorted_params = OrderedDict(sorted(params.items(), key=lambda t: t[0]))
    return path + connector + urlencode(sorted_params)

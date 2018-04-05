import os
import re

import mappings

m = {}


def compile(nile_intent):
    compiled = None
    intent = re.sub(' +', ' ', nile_intent.split('Intent:')[1].strip())
    if intent in m:
        compiled = m[intent]
    return compiled


def handle_request(request):
    status = {
        'code': 200,
        'details': 'Success'
    }

    intent = request.get('intent')
    sdn_rule = compile(intent)
    if sdn_rule is None:
        status = {
            'code': 404,
            'details': 'No mapping found for this intent.'
        }

    return {
        'status': status,
        'input': {
            'type': 'nile',
            'intent': intent
        },
        'output': {
            'type': 'sdn-rule',
            'policy': sdn_rule
        }
    }


m = mappings.read()

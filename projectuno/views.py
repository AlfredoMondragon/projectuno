from pyramid.view import view_config
import random

def get_random_nickname():
    adjvs = ['crystal', 'amber', 'brandy', 'lola', 'angel', 'ginger', 'candy']
    nouns = ['tiffany', 'porsche', 'peaks', 'smiles', 'bunny', 'diamond', 'passion']

    return random.choice(adjvs) + ' ' + random.choice(nouns)

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    random_nickname = get_random_nickname()

    return {'project': 'ProjectUno', 'nickname': random_nickname}

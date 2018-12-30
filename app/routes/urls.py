"""
Author:MukuruH
"""

from app.views.views import IncidentMap
from app import app


view_rules = IncidentMap.as_view('view_rules')
app.add_url_rule('/api/v1/red-flags', defaults={'id': None},
                 view_func=view_rules, methods=['GET',])
app.add_url_rule('/api/v1/red-flags', view_func=view_rules, methods=['POST',])
app.add_url_rule('/api/v1/red-flags/<int:id>', view_func=view_rules,
                 methods=['GET', 'DELETE'])
app.add_url_rule('/api/v1/red-flags/<int:id>/<string:key>', view_func=view_rules,
                 methods=['PATCH'])
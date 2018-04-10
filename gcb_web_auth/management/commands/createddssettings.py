from django.core.management.base import BaseCommand
from gcb_web_auth.models import DDSEndpoint


class Command(BaseCommand):
    help = 'Create/Replace DDSEndpoint in the database.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Endpoint Name')
        parser.add_argument('api_root', type=str, help='DukeDS API url')
        parser.add_argument('agent_key', type=str, help='Agent key to use when authenticating this application')
        parser.add_argument('portal_root', type=str, help='DukeDS portal url')
        parser.add_argument('openid_provider_id', type=str, help='OpenID provider from DukeDS api/v1/auth_providers')

    def handle(self, *args, **options):
        name = options['name']

        try:
            endpoint = DDSEndpoint.objects.get(name=name)
            endpoint.update(**options)
            endpoint.save()
        except DDSEndpoint.DoesNotExist:
            endpoint = DDSEndpoint.objects.create(**options)

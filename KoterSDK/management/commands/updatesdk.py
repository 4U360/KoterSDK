from django.conf import settings
from django.core.management.base import BaseCommand
from KoterSDK import has_new_version
import git

class Command(BaseCommand):
    help = 'Update SDK for the last version'

    def handle(self, *args, **options):
        if has_new_version():
            g = git.cmd.Git(settings.BASE_DIR)
            self.stdout.write(self.style.WARNING(g.pull()))
            self.stdout.write(self.style.SUCCESS('Successfully updated SDK.'))
        else:
            self.stdout.write(self.style.SUCCESS('Your SDK is already at the latest version.'))


from django.conf import settings
from django.core.management.base import BaseCommand
import git

class Command(BaseCommand):
    help = 'Update SDK for the last version'

    def handle(self, *args, **options):
        g = git.cmd.Git(settings.BASE_DIR)
        self.stdout.write(self.style.WARNING(g.pull()))
        self.stdout.write(self.style.SUCCESS('Successfully updated SDK.'))


"""
Management command to remove bots/crawlers from trackers
"""

from optparse import make_option

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from orb.models import ResourceTracker, SearchTracker, TagTracker
from orb.lib import search_crawler

class Command(BaseCommand):
    help = "Removes bots/crawlers from trackers"

    def handle(self, *args, **options):
        for spider in search_crawler.SPIDERS:
            rts = ResourceTracker.objects.filter(user_agent__contains=spider)
            print spider + ":" + str(rts.count())
            rts.delete()


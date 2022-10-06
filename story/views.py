from .core import story
from pathlib import Path
from django.conf import settings

__my_story = story(settings.BASE_DIR.parent/'stories'/'khatoon')

story_server = __my_story.serv


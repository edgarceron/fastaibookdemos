from fastbook import (
    search_images_bing, DataBlock, ImageBlock, 
    CategoryBlock, download_images, get_image_files,
    verify_images
)
from fastai.vision.widgets import *
from pathlib import Path
import os

key = os.environ.get('AZURE_SEARCH_KEY', 'XXX')
print(key)

results = search_images_bing(key, 'grizzly bear')
ims = results.attrgot('contentUrl')
path = Path('bears')

def download_images():
    bear_types = 'grizzly','black','teddy'

    if not path.exists():
        path.mkdir()
        for o in bear_types:
            dest = (path/o)
            dest.mkdir(exist_ok=True)
            results = search_images_bing(key, f'{o} bear')
            download_images(dest, urls=results.attrgot('contentUrl'))

fns = get_image_files(path)
failed = verify_images(fns)
failed.map(Path.unlink)

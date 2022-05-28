import os
from django.core.management.base import BaseCommand
from tqdm import tqdm


class Command(BaseCommand):

    help = ("Generate Base User")

    def add_arguments(self, parser):
        parser.add_argument('--username', '-u', type=str, help='Username')

    def handle(self, *args, **kwargs):

        self.search()

    def search(self):
        dirs = os.listdir()
        print(dirs)
        # dirs.remove('blog')
        for dir in dirs:
            if os.path.exists(f'{dir}/migrations'):
                subdir = os.listdir(f'{dir}/migrations')
                unwanted_files = {'__init__.py', '__pycache__'}
                removed = list()
                for file in subdir:
                    if file not in unwanted_files:
                        # file_dir = f'{dir}/migrations/{file}' 
                        os.remove(f'{dir}/migrations/{file}' )
                        removed.append(file)


                print(removed, dir)

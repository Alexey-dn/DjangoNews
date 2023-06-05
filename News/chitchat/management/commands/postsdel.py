from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import gettext_lazy as _
from chitchat.models import Post, Category


class Command(BaseCommand):
    help = _('Your command hint')

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(_('Do you really want to delete all articles in a category') + f'{options["category"]}' + _('? yes/no \n'))

        if answer != 'yes' or answer != 'да':
            self.stdout.write(self.style.ERROR(_('Canceled')))

        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(post_category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted all news from category {category.name}')) # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {options["category"]}'))

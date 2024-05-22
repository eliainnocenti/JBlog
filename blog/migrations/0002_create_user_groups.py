# blog/migrations/0002_create_user_groups.py
from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_user_groups(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Comment = apps.get_model('blog', 'Comment')

    # Create groups
    readers_group, created = Group.objects.get_or_create(name='Readers')
    writers_group, created = Group.objects.get_or_create(name='Writers')

    # Get permissions
    post_content_type = ContentType.objects.get_for_model(Post)
    comment_content_type = ContentType.objects.get_for_model(Comment)

    # Readers permissions
    view_post = Permission.objects.get(codename='view_post', content_type=post_content_type)
    add_comment = Permission.objects.get(codename='add_comment', content_type=comment_content_type)

    # Writers permissions
    add_post = Permission.objects.get(codename='add_post', content_type=post_content_type)
    change_post = Permission.objects.get(codename='change_post', content_type=post_content_type)
    delete_post = Permission.objects.get(codename='delete_post', content_type=post_content_type)
    add_comment = Permission.objects.get(codename='add_comment', content_type=comment_content_type)
    change_comment = Permission.objects.get(codename='change_comment', content_type=comment_content_type)
    delete_comment = Permission.objects.get(codename='delete_comment', content_type=comment_content_type)

    # Assign permissions to groups
    readers_group.permissions.add(view_post, add_comment)
    writers_group.permissions.add(view_post, add_post, change_post, delete_post, add_comment, change_comment, delete_comment)

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_user_groups),
    ]

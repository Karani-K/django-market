# Generated by Django 5.0.2 on 2024-02-22 13:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_chat_chats_rename_chat_chatmsg_chats'),
        ('item', '0003_rename_categoy_item_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chats',
            new_name='Chat',
        ),
        migrations.RenameModel(
            old_name='ChatMsg',
            new_name='ChatMessage',
        ),
    ]

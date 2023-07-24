# Generated by Django 4.2 on 2023-06-02 09:08

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_notes_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='title',
            new_name='note_title',
        ),
        migrations.AddField(
            model_name='notes',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='note_title', unique=True),
        ),
    ]
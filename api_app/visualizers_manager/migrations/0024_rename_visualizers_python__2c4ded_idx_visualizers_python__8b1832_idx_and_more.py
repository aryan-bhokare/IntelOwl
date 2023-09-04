# Generated by Django 4.1.10 on 2023-08-22 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_app", "0037_pythonmodule_and_more"),
        ("visualizers_manager", "0023_alter_visualizerconfig_name"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="visualizerconfig",
            new_name="visualizers_python__8b1832_idx",
            old_name="visualizers_python__2c4ded_idx",
        ),
        migrations.AddField(
            model_name="visualizerconfig",
            name="python_module2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)ss",
                to="api_app.pythonmodule",
                null=True,
            ),
        ),
    ]

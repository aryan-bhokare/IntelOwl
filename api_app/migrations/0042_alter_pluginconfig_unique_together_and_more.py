# Generated by Django 4.1.10 on 2023-08-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_app", "0041_alter_pythonmodule_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="pluginconfig",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="pluginconfig",
            constraint=models.UniqueConstraint(
                fields=("owner", "for_organization", "parameter", "analyzer_config"),
                name="unique_with_analyzer_config",
            ),
        ),
        migrations.AddConstraint(
            model_name="pluginconfig",
            constraint=models.UniqueConstraint(
                fields=("owner", "for_organization", "parameter", "connector_config"),
                name="unique_with_connector_config",
            ),
        ),
        migrations.AddConstraint(
            model_name="pluginconfig",
            constraint=models.UniqueConstraint(
                fields=("owner", "for_organization", "parameter", "visualizer_config"),
                name="unique_with_visualizer_config",
            ),
        ),
        migrations.AddConstraint(
            model_name="pluginconfig",
            constraint=models.UniqueConstraint(
                fields=("owner", "for_organization", "parameter", "ingestor_config"),
                name="unique_with_ingestor_config",
            ),
        ),
    ]

# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_app", "0019_mitm_configs"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="playbook_requested",
            field=models.ForeignKey(
                "playbooks_manager.PlaybookConfig",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
                related_name="requested_in_jobs_new",
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="playbook_to_execute",
            field=models.ForeignKey(
                "playbooks_manager.PlaybookConfig",
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
                related_name="executed_in_jobs_new",
            ),
        ),
    ]

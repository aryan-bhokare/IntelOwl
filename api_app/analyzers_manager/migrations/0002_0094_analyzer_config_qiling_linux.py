from django.db import migrations
from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ForwardOneToOneDescriptor,
    ManyToManyDescriptor,
)

plugin = {
    "name": "Qiling_Linux",
    "python_module": {
        "module": "qiling.Qiling",
        "base_path": "api_app.analyzers_manager.file_analyzers",
    },
    "description": "Qiling ELF emulation",
    "disabled": False,
    "soft_time_limit": 120,
    "routing_key": "long",
    "health_check_status": True,
    "type": "file",
    "docker_based": True,
    "maximum_tlp": "RED",
    "observable_supported": [],
    "supported_filetypes": [
        "application/x-sharedlib",
        "application/x-executable",
        "application/x-elf",
    ],
    "run_hash": False,
    "run_hash_type": "",
    "not_supported_filetypes": [],
    "health_check_task": None,
    "model": "analyzers_manager.AnalyzerConfig",
}

params = [
    {
        "python_module": {
            "module": "qiling.Qiling",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "os",
        "type": "str",
        "description": "Change operating system for the emulation.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "qiling.Qiling",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "arch",
        "type": "str",
        "description": "Change system architecture for the emulation.",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "qiling.Qiling",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "profile",
        "type": "str",
        "description": "Add a Qiling [profile](https://docs.qiling.io/en/latest/profile/).",
        "is_secret": False,
        "required": False,
    },
    {
        "python_module": {
            "module": "qiling.Qiling",
            "base_path": "api_app.analyzers_manager.file_analyzers",
        },
        "name": "shellcode",
        "type": "bool",
        "description": "true if the file is a shellcode.",
        "is_secret": False,
        "required": False,
    },
]

values = [
    {
        "parameter": {
            "python_module": {
                "module": "qiling.Qiling",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "os",
            "type": "str",
            "description": "Change operating system for the emulation.",
            "is_secret": False,
            "required": False,
        },
        "for_organization": False,
        "value": "linux",
        "updated_at": "2024-02-09T10:52:19.151737Z",
        "owner": None,
        "analyzer_config": "Qiling_Linux",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "qiling.Qiling",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "arch",
            "type": "str",
            "description": "Change system architecture for the emulation.",
            "is_secret": False,
            "required": False,
        },
        "for_organization": False,
        "value": "x86",
        "updated_at": "2024-02-09T10:52:19.171039Z",
        "owner": None,
        "analyzer_config": "Qiling_Linux",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "qiling.Qiling",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "profile",
            "type": "str",
            "description": "Add a Qiling [profile](https://docs.qiling.io/en/latest/profile/).",
            "is_secret": False,
            "required": False,
        },
        "for_organization": False,
        "value": "",
        "updated_at": "2024-02-09T10:52:19.184869Z",
        "owner": None,
        "analyzer_config": "Qiling_Linux",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
    },
    {
        "parameter": {
            "python_module": {
                "module": "qiling.Qiling",
                "base_path": "api_app.analyzers_manager.file_analyzers",
            },
            "name": "shellcode",
            "type": "bool",
            "description": "true if the file is a shellcode.",
            "is_secret": False,
            "required": False,
        },
        "for_organization": False,
        "value": False,
        "updated_at": "2024-02-09T10:52:19.204697Z",
        "owner": None,
        "analyzer_config": "Qiling_Linux",
        "connector_config": None,
        "visualizer_config": None,
        "ingestor_config": None,
        "pivot_config": None,
    },
]


def _get_real_obj(Model, field, value):
    if (
        type(getattr(Model, field))
        in [ForwardManyToOneDescriptor, ForwardOneToOneDescriptor]
        and value
    ):
        other_model = getattr(Model, field).get_queryset().model
        # in case is a dictionary, we have to retrieve the object with every key
        if isinstance(value, dict):
            real_vals = {}
            for key, real_val in value.items():
                real_vals[key] = _get_real_obj(other_model, key, real_val)
            value = other_model.objects.get_or_create(**real_vals)[0]
        # it is just the primary key serialized
        else:
            value = other_model.objects.get(pk=value)
    return value


def _create_object(Model, data):
    mtm, no_mtm = {}, {}
    for field, value in data.items():
        if type(getattr(Model, field)) is ManyToManyDescriptor:
            mtm[field] = value
        else:
            value = _get_real_obj(Model, field, value)
            no_mtm[field] = value
    try:
        o = Model.objects.get(**no_mtm)
    except Model.DoesNotExist:
        o = Model(**no_mtm)
        o.full_clean()
        o.save()
        for field, value in mtm.items():
            attribute = getattr(o, field)
            attribute.set(value)
        return False
    return True


def migrate(apps, schema_editor):
    Parameter = apps.get_model("api_app", "Parameter")
    PluginConfig = apps.get_model("api_app", "PluginConfig")
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    exists = _create_object(Model, plugin)
    if not exists:
        for param in params:
            _create_object(Parameter, param)
        for value in values:
            _create_object(PluginConfig, value)


def reverse_migrate(apps, schema_editor):
    python_path = plugin.pop("model")
    Model = apps.get_model(*python_path.split("."))
    Model.objects.get(name=plugin["name"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("api_app", "0001_2_initial_squashed"),
        ("analyzers_manager", "0002_0093_analyzer_config_pulsedive"),
    ]

    operations = [migrations.RunPython(migrate, reverse_migrate)]
    atomic = False

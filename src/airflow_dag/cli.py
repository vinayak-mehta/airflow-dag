# -*- coding: utf-8 -*-

import os
import glob
import shutil

import yaml
import click
from jinja2 import Template

from airflow_dag.__version__ import __version__


@click.group("airflow-dag")
@click.version_option(version=__version__)
@click.pass_context
def cli(*args, **kwargs):
    """A tool to manage Airflow dags."""
    pass


@cli.command("build")
@click.option("-t", "--template-dir", help="Path to dag templates")
@click.option("-c", "--config", help="Path to dag config")
@click.option("-o", "--output-dir", help="Output path")
@click.pass_context
def build(*args, **kwargs):
    """Convert a yaml config to an Airflow dag."""
    template_dir = kwargs["template_dir"]
    output_dir = kwargs["output_dir"] if kwargs["output_dir"] is not None else os.getcwd()

    if template_dir is not None:
        templates = glob.glob(os.path.join(template_dir, "*.j2"))
    else:
        cwd = os.path.dirname(__file__)
        templates = glob.glob(os.path.join(cwd, "templates", "*.j2"))

    templates = {
        os.path.splitext(os.path.basename(templates[0]))[0]: t for t in templates
    }

    with open(kwargs["config"], "r") as f:
        config = yaml.load(f, Loader=yaml.Loader)

    if "template" not in config:
        raise click.UsageError("Config does not have template type")

    config_dir = os.path.dirname(kwargs["config"])
    notebook_path = os.path.join(config_dir, config["notebook_name"])

    if not os.path.isfile(notebook_path):
        raise click.UsageError(f"{config['notebook_name']} not found in {config_dir}")

    template_type = config["template"]
    if template_type not in templates:
        raise click.UsageError(f"{template_type} template not found in {kwargs['template_dir']}")

    with open(templates[template_type], "r") as f:
        template = Template(f.read())
    dag = template.render(config)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, f"{config['dag_name']}_v{config['version']}.py"), "w") as f:
        f.write(dag)
    shutil.copy(notebook_path, os.path.join(output_dir, config["notebook_name"]))


if __name__ == "__main__":
    cli()

# airflow-dag

A tool to manage Airflow dags.

## Installation

You can use `pip` to install `airflow-dag`:

```
$ pip install airflow-dag
```

## Usage

You can use the `build` command to convert a yaml config to an Airflow dag:

```
$ airflow-dag build -t examples/ -c examples/notebook.yml -o examples/out
```

```
$ airflow-dag build --help
Usage: airflow-dag build [OPTIONS]

  Convert a yaml config to an Airflow dag.

Options:
  -t, --template-dir TEXT  Path to dag templates
  -c, --config TEXT        Path to dag config
  -o, --output-dir TEXT    Output path
  --help                   Show this message and exit.
```

If a template path is not provided, `airflow-dag` will look into the [default templates](https://github.com/vinayak-mehta/airflow-dag/blob/main/src/airflow_dag/templates).

You can define your own dag templates too, and put them in a `templates` directory in Airflow's home folder.

The dag yaml configs can be placed in a `configs` directory in the same home folder, and the output path can then be the Airflow dags folder. The usage will look like:

```
$ airflow-dag build -t airflow/templates -c airflow/configs/dag.yml -o airflow/dags
```

## Roadmap

You can check out the open issues to look at new commands that might be added in the future, and also express interest by commenting on them!

## Versioning

`airflow-dag` uses [Semantic Versioning](https://semver.org/). For the available versions, see the tags on the GitHub repository.

## License

This project is licensed under the Apache License, see the [LICENSE](https://github.com/vinayak-mehta/airflow-dag/blob/master/LICENSE) file for details.

import jinja2
from datasette import hookimpl


def is_email(value):
    # This is a pretty lightweight check.
    # If value is a string of the form something@something.something
    # it quacks like an email sufficiently for us
    if type(value) != str:
        return False
    if value.count("@") != 1:
        return False
    _, domain = value.split("@")
    if "." in domain:
        return True
    return False


@hookimpl()
def render_cell(value, column, table, database, datasette):
    config = (
        datasette.plugin_config(
            "datasette-mailto-links", database=database, table=table
        )
        or {}
    )

    columns = config.get("columns")
    if columns is not None:
        if column not in columns:
            return None

    if is_email(value):
        return jinja2.Markup(
            f'<a href="mailto:{jinja2.escape(value)}">{jinja2.escape(value)}</a>'
        )
    return None

from datasette.app import Datasette

from datasette_mailto_links import render_cell


def test_not_strings():
    for value in [None, 1, False, 23.9, -7]:
        assert None is render_cell(value, None, None, None, Datasette([]))


def test_not_emails():
    for value in [
        "foobar",  # just a string
        "root@localhost",  # domain part must include a .
        "foo@bar@baz.qux",  # more than one @ sign
    ]:
        assert None is render_cell(value, None, None, None, Datasette([]))


def test_emails():
    for value in [
        "simple@example.com",
        "very.common@example.com",
        "abc@example.co.uk",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "example-indeed@strange-example.com",
        "example-indeed@strange-example.inininini",
        "1234567890123456789012345678901234567890123456789012345678901234+x@example.com",
    ]:
        markup = render_cell(value, None, None, None, Datasette([]))
        assert str(markup).startswith('<a href="mailto:')


def test_escaping():
    markup = render_cell(
        "foo@<script>alert('XSS');</script>.bar", None, None, None, Datasette([])
    )
    assert None is not markup
    assert "<script>" not in str(markup)


def test_settings_explicit_column():
    metadata = {
        "databases": {
            "mydatabase": {
                "tables": {
                    "mytable": {
                        "plugins": {
                            "datasette-mailto-links": {
                                "columns": ["email"],
                            }
                        }
                    }
                }
            }
        }
    }
    datasette = Datasette([], metadata=metadata)
    assert None is render_cell(
        "simple@example.com", "some_other_column", "mytable", "mydatabase", datasette
    )
    markup = render_cell(
        "simple@example.com", "email", "mytable", "mydatabase", datasette
    )
    assert str(markup).startswith('<a href="mailto:')


def test_settings_disable():
    metadata = {
        "databases": {
            "mydatabase": {
                "tables": {
                    "mytable": {
                        "plugins": {
                            "datasette-mailto-links": {
                                "columns": [],
                            }
                        }
                    }
                }
            }
        }
    }
    datasette = Datasette([], metadata=metadata)
    assert None is render_cell(
        "simple@example.com", "email", "mytable", "mydatabase", datasette
    )
    markup = render_cell(
        "simple@example.com", "email", "some_other_table", "mydatabase", datasette
    )
    assert str(markup).startswith('<a href="mailto:')

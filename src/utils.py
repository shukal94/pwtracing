import configparser
import os
import pathlib
import uuid
from datetime import date

from allure_commons.model2 import TestResult, Attachment
from allure_commons.reporter import AllureReporter


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def attach_trace(trace_path: pathlib.Path, test_name):
    test_item: TestResult = last_test(test_name)
    test_item.attachments.append(
        Attachment(name="Trace", source=str(trace_path), type="application/zip")
    )


def attach_link_to_viewer(test_name):
    trace_link_filename = f"trace-link-{uuid.uuid4()}.html"
    trace_link_path = os.path.join("allure-results", trace_link_filename)

    today = date.today().isoformat()
    viewer_url = f"https://shukal94.github.io/pwtracing/traces/run-{today}/index.html"

    with open(trace_link_path, "w") as f:
        f.write(
            f'<iframe src="{viewer_url}" '
            'width="100%" height="800px" frameborder="0" '
            'allowfullscreen></iframe>'
        )

    test_item: TestResult = last_test(test_name)
    test_item.attachments.append(
        Attachment(
            name="View Trace in Browser",
            source=trace_link_filename,
            type="text/html"
        )
    )


def last_test(test_name):
    reporter: AllureReporter = AllureReporter()
    return next(
        item for item in reporter._items.thread_context.values()
        if item.name and item.name == test_name
    )

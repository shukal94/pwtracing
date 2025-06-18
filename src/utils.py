import configparser
import pathlib

from allure_commons.model2 import TestResult, Attachment
from allure_commons.reporter import AllureReporter


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def attach_trace(trace_path: pathlib.Path, test_name):
    reporter: AllureReporter = AllureReporter()
    test_item: TestResult = next(
        item for item in reporter._items.thread_context.values()
        if item.name and item.name == test_name
    )
    test_item.attachments.append(
        Attachment(name="Trace", source=str(trace_path), type="application/zip")
    )

from unittest.mock import MagicMock, Mock
import json
from datetime import datetime, timedelta, timezone
import pytest


from homematicip.EventHook import EventHook
from homematicip.base.helpers import bytes2str, detect_encoding

def event_hook_handler2(mustBe2):
    assert mustBe2 == 2

def event_hook_handler3(mustBe3):
    assert mustBe3 == 3

def test_event_hook():
    eh = EventHook()
    eh += event_hook_handler2
    eh.fire(2)
    eh += event_hook_handler3
    eh -= event_hook_handler2
    eh.fire(3)


def test_detect_encoding():
    testString = 'This is my special string to test the encoding'
    assert detect_encoding(testString.encode('utf-8')) == 'utf-8'
    assert detect_encoding(testString.encode('utf-8-sig')) == 'utf-8-sig'
    assert detect_encoding(testString.encode('utf-16')) == 'utf-16'
    assert detect_encoding(testString.encode('utf-32')) == 'utf-32'
    assert detect_encoding(testString.encode('utf-16-be')) == 'utf-16-be'
    assert detect_encoding(testString.encode('utf-32-be')) == 'utf-32-be'
    assert detect_encoding(testString.encode('utf-16-le')) == 'utf-16-le'
    assert detect_encoding(testString.encode('utf-32-le')) == 'utf-32-le'

def test_bytes2str():
    testString = 'This is my special string to test the encoding'
    assert bytes2str(testString.encode('utf-8')) == testString
    assert bytes2str(testString.encode('utf-8-sig')) == testString
    assert bytes2str(testString.encode('utf-16')) == testString
    assert bytes2str(testString.encode('utf-32')) == testString
    assert bytes2str(testString.encode('utf-16-be')) == testString
    assert bytes2str(testString.encode('utf-32-be')) == testString
    assert bytes2str(testString.encode('utf-16-le')) == testString
    assert bytes2str(testString.encode('utf-32-le')) == testString
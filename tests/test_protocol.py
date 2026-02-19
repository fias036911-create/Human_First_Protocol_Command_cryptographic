"""Tests for the Human First Protocol stub helpers."""

from human_first_protocol import protocol


def test_check_human_sovereignty():
    assert protocol.check_human_sovereignty("alice")
    assert not protocol.check_human_sovereignty("")
    assert not protocol.check_human_sovereignty("   ")


def test_log_transparency(capfd):
    protocol.log_transparency("action", "details")
    captured = capfd.readouterr()
    assert "[TRANSPARENCY] action: details" in captured.out


def test_requires_consent():
    assert protocol.requires_consent() is True

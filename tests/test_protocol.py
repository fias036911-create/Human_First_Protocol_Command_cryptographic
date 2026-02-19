"""Tests for the Human First Protocol stub helpers."""

from human_first_protocol import protocol, check_human_sovereignty


def test_check_human_sovereignty_function():
    # old standalone functions still exist for backwards compatibility
    # new implementation only returns true for subject == "human"
    assert check_human_sovereignty("human")
    assert not check_human_sovereignty("alice")
    assert not check_human_sovereignty("")


def test_protocol_class_behavior(capfd):
    p = protocol.HumanFirstProtocol()
    assert p.check_human_sovereignty("human")
    assert not p.check_human_sovereignty("robot")

    # logging should append and print
    p.log_transparency("act", {"foo": "bar"})
    captured = capfd.readouterr()
    assert "[TRANSPARENCY] act: {'foo': 'bar'}" in captured.out
    assert len(p.transparency_log) == 1

    assert p.requires_consent("alice", "terminate")
    assert not p.requires_consent("alice", "read")

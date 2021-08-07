#!/usr/bin/env python
# coding: utf-8

from prompt_toolkit.keys import Keys
from prompt_toolkit.key_binding.key_bindings import KeyBindings


def set_key_binding(cntrllr):
    bindings = KeyBindings()

    @bindings.add(Keys.ControlQ, eager=True)
    @bindings.add(Keys.ControlC, eager=True)
    def _(event):
        event.cli.future.set_result(None)

    @bindings.add(Keys.Down, eager=True)
    @bindings.add(Keys.ControlN, eager=True)
    def _(_):
        cntrllr.selected_option_index = (
            (cntrllr.selected_option_index + 1) % cntrllr.choice_count)

    @bindings.add(Keys.Up, eager=True)
    @bindings.add(Keys.ControlP, eager=True)
    def _(_):
        cntrllr.selected_option_index = (
            (cntrllr.selected_option_index - 1) % cntrllr.choice_count)

    @bindings.add(Keys.Enter, eager=True)
    def _(event):
        cntrllr.answered = True
        event.cli.future.set_result(None)

    return bindings

#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from prompt_toolkit.application import Application
from prompt_toolkit.filters import IsDone
from prompt_toolkit.layout.containers import (ConditionalContainer, HSplit,
                                              ScrollOffsets, VerticalAlign, Window)
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.dimension import LayoutDimension as LD
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import style_from_pygments_dict
from pygments.token import Token

from selectmenu.control import SelectControl
from selectmenu.keybinding import set_key_binding


class SelectMenu():
    def __init__(self, choices=None, actions=None):
        self.prompt_msg = None
        if choices and len(choices) > 0:
            self.add_choices(choices, actions)

    def add_choices(self, choices, actions=None):
        actions = actions if actions else []
        if not isinstance(choices, (list, dict)):
            raise ValueError("The choices is not list nor a dict.")

        if isinstance(choices, dict) and len(actions) > 0:
            raise ValueError("Actions list is not empty. \
                If choices is a dict then the actions should be in the dict too")

        if len(actions) > 0 and len(actions) != len(choices):
            raise ValueError(
                "Number of choices not equal to number of actions." +
                "If you select an action for a choice, you have to do it for all")

        if isinstance(choices, dict):
            self.choices = list(choices.keys())
            self.actions = list(choices.values())
        else:
            self.choices = choices
            self.actions = actions

        self.controller = SelectControl(self.choices)

    def select_index(self, message=None):
        self.prompt_msg = message

        layout = self._get_layout(message)
        style = SelectMenu._get_style()
        registry = set_key_binding(self.controller)

        application = Application(
            layout=layout,
            style=style,
            key_bindings=registry
        )

        application.run()
        return self.controller.selected_option_index

    def select(
        self, message=None): return self.choices[self.select_index(message)]

    def select_action(
        self, message=None): return self.actions[self.select_index(message)]()

    def _get_layout(self, message=None):
        conditional_window = ConditionalContainer(
            Window(
                self.controller,
                width=LD.exact(43),
                height=LD.exact(len(self.choices)),
                scroll_offsets=ScrollOffsets(top=1, bottom=1)
            ),
            filter=~IsDone()
        )
        return Layout(HSplit([
            Window(FormattedTextControl(message, show_cursor=False), height=1),
            conditional_window
        ], align=VerticalAlign.TOP))

    @classmethod
    def _get_style(cls):
        return style_from_pygments_dict(
            {
                Token.Selected: '#FF9D00',
                Token.Instruction: '',
                Token.Answer: '#FF9D00 bold',
                Token.Question: 'bold'
            }
        )

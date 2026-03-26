"""Tests for the think tool."""

from __future__ import annotations

import pytest

from openjarvis.tools.think import ThinkTool


class TestThinkTool:
    def test_spec(self):
        tool = ThinkTool()
        assert tool.spec.name == "think"
        assert tool.spec.category == "meta"
        assert "meta:thought" in tool.spec.required_capabilities

    @pytest.mark.skip(reason="requires openjarvis_rust module")
    def test_think_simple(self):
        tool = ThinkTool()
        result = tool.execute(thought="This is my thought process.")
        assert result.success is True
        assert "thought process" in result.content

    @pytest.mark.skip(reason="requires openjarvis_rust module")
    def test_think_multiline(self):
        tool = ThinkTool()
        thought = """Step 1: Analyze the problem
Step 2: Consider possible solutions
Step 3: Evaluate each solution"""
        result = tool.execute(thought=thought)
        assert result.success is True
        assert "Step" in result.content

    @pytest.mark.skip(reason="requires openjarvis_rust module")
    def test_think_empty(self):
        tool = ThinkTool()
        result = tool.execute(thought="")
        assert result.success is True
        assert result.content == ""

    @pytest.mark.skip(reason="requires openjarvis_rust module")
    def test_think_special_chars(self):
        tool = ThinkTool()
        result = tool.execute(thought="Thought with special chars: @#$%^&*()")
        assert result.success is True
        assert "@#$" in result.content

    def test_to_openai_function(self):
        tool = ThinkTool()
        fn = tool.to_openai_function()
        assert fn["type"] == "function"
        assert fn["function"]["name"] == "think"
        assert "thought" in fn["function"]["parameters"]

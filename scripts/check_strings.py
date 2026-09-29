#!/usr/bin/env python3
"""Checks every translation in Strings/ against the English base file.

The app passes these strings to string.Format, so a bad placeholder can crash
it (for example "{nama bandara}" instead of "{2}"). Run from the repo root:

    python3 scripts/check_strings.py
"""
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

STRINGS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Strings")
TOKEN = re.compile(r"\{[^{}]*\}")
FORMAT_ITEM = re.compile(r"\{(\d+)(?:,-?\d+)?(?::[^}]*)?\}")

# The app edits these strings with Replace, so they must keep the text it looks for.
REPLACE_RULES = {
    "Time.Minutes": "{0} ",
    "Time.MinuteShortForm": "{0} ",
    "WorldModeModalControl.GradeThreeRequired": "3",
}


def load(path):
    root = ET.parse(path).getroot()
    return {d.get("name"): d.findtext("value") or "" for d in root.iter("data")}


def placeholders(value):
    text = value.replace("{{", "").replace("}}", "")
    indexes, invalid = set(), []
    for token in TOKEN.findall(text):
        match = FORMAT_ITEM.fullmatch(token)
        if match:
            indexes.add(int(match.group(1)))
        else:
            invalid.append(token)
    rest = TOKEN.sub("", text)
    if "{" in rest or "}" in rest:
        invalid.append("unmatched brace")
    return indexes, invalid


def check(lang, key, value, english):
    errors = []
    indexes, invalid = placeholders(value)
    expected, _ = placeholders(english) if english is not None else (set(), [])
    if invalid:
        errors.append(f"invalid format item {invalid}; use {{0}}, {{1}}, ...")
    if english is not None:
        extra = sorted(indexes - expected)
        missing = sorted(expected - indexes)
        if extra:
            errors.append(f"placeholder {extra} is not in English")
        if missing:
            errors.append(f"placeholder {missing} is missing")
    if "\\n" in value or '\\"' in value:
        errors.append('literal \\n or \\" (use a real line break or a plain quote)')
    required = REPLACE_RULES.get(key)
    if required and value and required not in value and not (required == "{0} " and "{0}" not in value):
        errors.append(f"must contain {required!r} (the app replaces it)")
    return errors


def main():
    english = load(os.path.join(STRINGS, "AppResources.resx"))
    failures = 0
    for path in sorted(glob.glob(os.path.join(STRINGS, "AppResources*.resx"))):
        name = os.path.basename(path)
        lang = name[len("AppResources."):-len(".resx")] or "en"
        for key, value in load(path).items():
            if not value.strip():
                continue
            base = None if lang == "en" else english.get(key)
            if lang != "en" and base is None:
                continue
            for error in check(lang, key, value, base):
                failures += 1
                print(f"{name}: {key}: {error}\n    {value!r}")
    if failures:
        print(f"\n{failures} problem(s) found")
        return 1
    print("All strings OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

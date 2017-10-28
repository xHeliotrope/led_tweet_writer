#!/bin/bash
sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" nohup python examples/scroll_text.py & disown

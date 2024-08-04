# En Dash Bash for NVDA
En Dash Bash is an add-on for the [NVDA screen reader](https://nvaccess.org) that adds input gestures (NVDA commands) to enter the en dash (–) and em dash (—) quickly. En dashes are used to connect symmetric items, such as the two ends of a range of numbers or dates; to contrast values or illustrate a relationship between two things (such as Mexican–American War); to compound attributes, where one of the connected items is itself a compound (such as New York–style pizza); and, when spaced, to set off parenthetical expressions – like this one – in the middle of sentences. In some languages, en dashes are sometimes used to indicate a change of speaker in quoted dialogue. Unspaced em dashes are used similarly to spaced en dashes to set off parenthetical expressions.

By default, <kbd>NVDA</kbd>+<kbd>-</kbd> types an en dash, and <kbd>NVDA</kbd>+<kbd>Shift</kbd>+<kbd>-</kbd> types an em dash. These commands can be changed in NVDA's input gestures dialog.

## Building
Much like NVDA, this add-on is built with [SCons](https://scons.org). Run `scons` from the root of the repo to build an `nvda-addon` package.

import globalPluginHandler

from brailleInput import handler as brailleInputHandler
from scriptHandler import script


"""
En Dash Bash for NVDA
Copyright 2024 Bill Dengler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def _sendCharacters(self, chars: str):
		if brailleInputHandler is not None:
			brailleInputHandler.sendChars(chars)

	@script(
		gesture="kb:NVDA+-",
		description=(
			# Translators: a gesture description.
			_("Enters an en dash (\N{en dash}) character")
		),
		category=(
			# Translators: an input gesture category.
			_("En Dash Bash")
		),
	)
	def script_enDash(self, gesture):
		self._sendCharacters("\N{en dash}")

	@script(
		gesture="kb:NVDA+Shift+-",
		description=(
			# Translators: a gesture description.
			_("Enters an em dash (\N{em dash}) character")
		),
		category=(
			# Translators: an input gesture category.
			_("En Dash Bash")
		),
	)
	def script_emDash(self, gesture):
		self._sendCharacters("\N{em dash}")

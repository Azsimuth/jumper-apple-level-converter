# jumper-apple-level-converter
My game that I have been working on, Jumper &amp; Apple has built-in level editor, but you can also use a text file with the extension (.jms) This repository contains the code to convert the new text format into a playable level. (aka the old "format")
This was originally done in python, but since then I implemented it in GML in the main game as well, the python verison isn't as important now. I did create a sublime text sytnax highlight, and build system (that uses the python implementation)

The JMS format is a grid, with letters correlating to in game objects. For example: B -- > Brick; Meanwhile the .JumperMap "format" isn't really a format, more just a set of instructions in gml which are executed to build the map. This was .JumperMap provides more control, however is riskier, due to it just being plain code. The JMS format doesn't suffer from this, however it greatly restricts the possibilities of level creation. For this reason, Jumper &amp; will continue to support both "formats"
It's unlikely anyone will ever find any use to this, but just in case for any reason you need to turn a .jms formatted map into a .JumperMap, you can do it by passing the file name as a command line argument to the script.

Perhaps, the python implementation could work better using a dictionary or something of the sorts, but that isn't going to be used frequently anyways.

#!/usr/bin/zsh
SCRIPT=`realpath -s $0`
SCRIPTPATH=`dirname $SCRIPT`
SCRIPTPATH_KEYBND="$SCRIPTPATH/keybinds_cheatsheet.py"
KEYBIND_CHEATSHEET_ARGV="\"keybinds:$SCRIPTPATH_KEYBND $1 $2\""
rofi -modi $KEYBIND_CHEATSHEET_ARGV -show keybinds

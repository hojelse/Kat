#!/usr/bin/env python3
import sys

from commands.work import workCommand
from commands.archive import archiveCommand
from commands.get import getCommand
from commands.submit import submitCommand
from commands.test import testCommand
from commands.watch import watchCommand
from commands.list import listCommand
from commands.help import printHelp, helpIfNotCommand
from commands.read import readCommand
from helpers.exceptions import RedundantCommandException, InvalidProblemException
from helpers.flags import divideArgs
from commands.unarchive import unarchiveCommand

execCommand = {
    "archive": archiveCommand,
    "unarchive": unarchiveCommand,
    "get": getCommand,
    "submit": submitCommand,
    "test": testCommand,
    "list": listCommand,
    "read": readCommand,
    "watch": watchCommand,
    "work": workCommand,
}

problemCommands = [  # problem commands are commands that take a problem as their only argument
    "archive",
    "unarchive",
    "get",
    "read",
]


def main():
    args, options = divideArgs(sys.argv)

    command = args[1] if args[1:] else ""
    args = args[2:] if args[2:] else []

    if command == "" or "help" in options:
        printHelp(command)
    elif command in execCommand:
        if command in problemCommands:
            for arg in args:
                try:
                    execCommand[command](arg, options)
                except (RedundantCommandException, InvalidProblemException) as error:
                    print()
                    print(error)
                    print()
        else:
            try:
                execCommand[command](args, options)
            except (RedundantCommandException, InvalidProblemException) as error:
                print()
                print(error)
                print()
    else:
        helpIfNotCommand(command)


main()

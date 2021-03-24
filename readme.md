### RDP remote execution command utility

The tool facilitates quick lateral movement given access credentials to a set of remote desktops. Previous remote command-line execution tools are found to be deprecated; to avoid deprecation of this tool, it executes commands on the Windows Remote Desktop GUI given a pre-defined set of commands.

#### Instructions:

*Running the CLI*
* `python cli.py`
* `python <filepath>/cli.py --commands_file commands.txt --credentials_file credentials.txt`


*Storing commands*
* `commands.txt` stores the time delays between each command.
* default time delay between characters in text is 100ms.
* default time delay between commands is 1000ms.
* entering ms value in time_delay column specifies time delay after the execution of the command.

*Storing credentials*
* `credentials.txt` contain the list of remote desktop ip & password configurations.

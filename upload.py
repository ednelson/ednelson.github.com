#!/usr/bin/pythonprint 'yoyoyoyoy'import subprocesssubprocess.call(["git", "add",  "-A", "."])subprocess.call(["git", "commit", "-a", \				"--allow-empty-message", "-m", "\'\'"])subprocess.call(["git", "push"])subprocess.call(["echo", "\'this process may take a while...\'"])
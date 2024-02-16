#!/usr/bin/env python

import sys
import subprocess
import time

class PynovaInterpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, statement):
        if statement.startswith("math "):
            expression = statement[5:].strip()
            try:
                result = eval(expression, {"__builtins__": None}, self.variables)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
        elif statement.startswith("print"):
            value = statement[6:].strip()
            if value.startswith('@'):
                var_name = value[1:]
                if var_name in self.variables:
                    print(self.variables[var_name])
                else:
                    print(f"Variable '{var_name}' not found.")
            else:
                print(value)
        elif statement.startswith("wait "):
            amount = statement[5:].strip()
            if amount.startswith('@'):
                var_name = amount[1:]
                if var_name in self.variables:
                    wait_time = self.variables[var_name]
                    time.sleep(wait_time)
                else:
                    print(f"Variable '{var_name}' not found.")
            else:
                try:
                    wait_time = float(amount)
                    time.sleep(wait_time)
                except ValueError:
                    print("Invalid amount or variable.")
        elif statement.startswith("ping "):
            site = statement[5:].strip()
            try:
                result = subprocess.run(['ping', '-c', '4', site], stdout=subprocess.PIPE)
                print(result.stdout.decode())
            except Exception as e:
                print(f"Error: {e}")
        elif statement == "help":
            print("pynova Commands:")
            print("- math <expression>: Evaluate a mathematical expression.")
            print("- print <text or variable>: Print text or the value of a variable.")
            print("- wait <amount or variable>: Pause execution for a specified amount of time or the value of a variable.")
            print("- ping <site>: Ping a website to check its response time.")
            print("- deletevar <variable>: Delete a variable.")
            print("- listvar: List all defined variables.")
            print("- readfile <filename>: Read the contents of a file.")
            print("- writefile <filename>: Write text or variable contents to a file.")
            print("- help: Display this help message.")
        elif statement.startswith("deletevar "):
            var_name = statement[10:].strip()
            if var_name in self.variables:
                del self.variables[var_name]
                print(f"Variable '{var_name}' deleted.")
            else:
                print(f"Variable '{var_name}' not found.")
        elif statement == "listvar":
            print("Defined Variables:")
            for var_name, var_value in self.variables.items():
                print(f"{var_name}: {var_value}")
        elif statement.startswith("readfile "):
            filename = statement[9:].strip()
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
        elif statement.startswith("writefile "):
            parts = statement.split(" ", 1)
            if len(parts) == 2:
                filename = parts[1].strip()
                content = input("Enter content: ")
                try:
                    with open(filename, 'w') as file:
                        file.write(content)
                    print(f"Content written to '{filename}'.")
                except Exception as e:
                    print(f"Error writing to '{filename}': {e}")
            else:
                print("Invalid syntax. Usage: writefile <filename>")
        elif "=" in statement:
            parts = statement.split("=")
            var_name = parts[0].strip()
            var_value = "=".join(parts[1:]).strip()
            self.variables[var_name] = var_value
            print(f"Variable '{var_name}' set to '{var_value}'.")
        elif statement == "--amogus":
            print("sus")
        else:
            print("Invalid statement")

    def execute_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    self.execute(line.strip())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--execute":
        filename = sys.argv[2]
        interpreter = PynovaInterpreter()
        interpreter.execute_file(filename)
    elif len(sys.argv) > 1 and sys.argv[1] == "--amogus":
        print("sus")
    else:
        interpreter = PynovaInterpreter()
        while True:
            user_input = input("pynova> ")
            interpreter.execute(user_input)

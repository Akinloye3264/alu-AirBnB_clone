AirBnB Clone Project
Description of the Project
This project is the first step toward building a full web application: an AirBnB clone. The goal is to create a command-line interpreter to manage and interact with different objects in the application, such as Users, States, and Places. This interpreter will be the foundation for future parts of the project, including a database, an API, and a front-end interface.

The Command Interpreter
The command interpreter is a simple shell that lets you perform operations on the objects of the AirBnB project. You can use it to:

Create new objects (like a new User or Place).

Retrieve objects.

Update an object's attributes.

Destroy an object.

Manage the number of objects.

How to Start the Interpreter
To start the interpreter, run the console.py file from your terminal:

Bash

./console.py
After running the command, you will see a prompt like this: (hbnb). This means the interpreter is ready for your commands.

How to Use the Interpreter
You can use the interpreter in two ways:

Interactive Mode: Type a command and press Enter. The interpreter will execute it and wait for your next command. To exit, use the quit command.

Non-Interactive Mode: Run the console.py file with a command passed through a pipe. This is useful for running a single command or a series of commands from a script.

A couple of examples:
Interactive Mode

Bash

$ ./console.py
(hbnb) help
... (the help message) ...

(hbnb) create BaseModel
<a long ID number will appear>
(hbnb) show BaseModel <that long ID number>
... (all the details of the new object) ...
(hbnb) quit
$
Non-Interactive Mode

Bash

$ echo "help" | ./console.py
(hbnb) 
... (the help message) ...
(hbnb) 
$ 

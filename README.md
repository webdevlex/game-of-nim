# game-of-nim

## Setup Instructions

1. **Create a Virtual Environment**
   - Open your terminal or command prompt.
   - Navigate to the directory containing your project.
   - Run the following command to create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - This will create a folder named `venv` in your project directory that contains the virtual environment.

2. **Activate the Virtual Environment**
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     venv\Scripts\activate
     ```
   - You should now see `(venv)` at the beginning of your command line, indicating the environment is active.

3. **Install Dependencies**
   - With the virtual environment activated, install the required packages by running:
     ```bash
     pip install -r requirements.txt
     ```
   - This command installs all packages listed in `requirements.txt`.

4. **Run the Game of Nim**
   - Now, you're ready to run your program within this virtual environment.
   - When you’re done, you can deactivate the virtual environment by running:
     ```bash
     deactivate
     ```

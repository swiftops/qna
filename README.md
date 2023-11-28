# qna
Question and answer

## Installation

1. Install the required packages by running the command `pip install -r requirements.txt` in your terminal.

## Running the Application

1. Navigate to the directory containing your `main.py` file. If your `main.py` is inside the `app` directory, you should be in the same directory as the `app` folder.
2. Run the command `uvicorn app.main:app --reload` in your terminal. This command tells Uvicorn to run your application, which is located in the `app.main` module, and the `--reload` flag enables hot reloading, which means the server will automatically update whenever you make changes to your code.

After running the command, you should see output indicating that the server is running. You can then access the application by navigating to `http://localhost:8000` in your web browser.

## Running the Tests

1. Navigate to the root directory of the project (the same directory as the `app` folder).
2. Run the command `pytest` in your terminal.

This will discover and run all test cases in the `tests` directory. Make sure you have the `pytest` package installed. If not, you can install it with `pip install pytest`.
# Running the tests:

Create an environment:
On macOS / linux:

```
python3 -m venv .venv
```

On Windows:
```
py -m venv .venv
```

Or use your IDE.

Activate your environment:

On macOS / linux:

```
source .venv/bin/activate
```

On Windows:
```
.\.venv\Scripts\activate
```

Or use your IDE.

Change your interpreter in your IDE to use your .venv/scripts/python

- In PyCharm: File > Settings > Project Interpreter > Add > Existing Environment > Select location of .venv/scripts/python3X.exe

- In VSC: Open the Command Pallete (win: Ctrl+Shift+P Mac: ⇧⌘P) Type: < Python: Select Interpreter > And select the one of the .venv.

- Other IDES: Check the documentation.

Install dependencies:
```
pip install -r requirements.txt
```

To run a specific test:
- Pass the name of the file to pytest:
```
pytest EX_01_test.py
```

To run all the tests:
```
pytest
```


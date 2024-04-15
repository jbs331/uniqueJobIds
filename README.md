# uniqueJobIds

## Overview
The contents of this repo provides a solution to the problem outlined in the code challenge.

### Requirements
- Python 3.8+

### Installation
Clone the repository:
```bash
git clone https://github.com/jbs331/uniqueJobIds.git
```
Navigate to the project directory and create a virtual environment:
```bash
cd uniqueJobIds
python -m venv venv
source venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
### Configuration and Testing
- Update the `baseUrl` variable in `main.py` to point to an endpoint that behaves as described in the code challenge.
- If the reviewer of the code challenge does not have an endpoint setup, they can use the baseUrl provided in the email notification that the code challenge is ready for review. The code running on this endpoint can be found in the `app.py` script. Note: this code introduces response delays as well as network error simulations.

### Usage
```bash
python main.py
```
This will execute the requests and print the output, along with errors, to the console.

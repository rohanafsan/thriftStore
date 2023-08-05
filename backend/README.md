# backend

Central backend for the thriftStore application.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:

```bash
git clone git@github.com:rohanafsan/thriftStore.git
```

2. Navigate to the project directory:
```
cd thriftStore/backend
```

3. Create a virtual environment and activate it:
```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install the required packages:
```bash
Copy code
pip install -r requirements.txt
```

5. Set up the database:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
Copy code
python manage.py runserver
```

## Usage
The backend can now serve requests, interact with the database to store and retrieve information


## API Endpoints
These are the active endpoints: 

/product/<:id>/: Returns a product with id 
/product/: Returns all the products
...

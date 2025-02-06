
# ATDEV Technical Assessment - Paystub Notifier API

Notification Automation Project in FastAPI for the ATDEV Technical Assessment.

## Description

Paystub Notifier API is a RESTful application developed in Python using FastAPI. Its purpose is to process CSV files containing payroll data, generate paystub PDFs for each employee, and send these PDFs via email. The project is built with a modular, scalable architecture following best practices for file handling and security, and it is container-ready (including ARM support for Mac M1/M2).

## Scope

- **CSV Processing:** Convert CSV files with payroll data into Python objects.
- **PDF Generation:** Create paystub PDFs using XML templates and XSLT transformations.
- **Email Sending:** Dispatch the generated PDFs as email attachments.
- **Containerization:** Preconfigured for Docker and Docker Compose with ARM support.
- **Automated Testing:** Unit tests for individual services and integration tests for the API.
- **Security:** Secure configuration management using environment variables.

## Features

- **CSV Handling:** Efficiently processes payroll CSV files.
- **PDF Generation:** Produces paystubs from XML/XSLT templates.
- **Email Integration:** Sends out emails via SMTP with PDF attachments.
- **Modular Architecture:** Organized into models, routes, services, and utilities.
- **Container-Ready:** Fully configured for Docker and Docker Compose.
- **ARM Support:** Compatible with ARM architectures (ideal for Mac M1/M2).
- **Automated Testing:** Comprehensive unit and integration tests.

## Project Structure

```plaintext
atdev-technical-assessment/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   └── models.py
│   ├── routes/
│   │   └── payroll.py
│   ├── services/
│   │   ├── email_service.py
│   │   ├── file_handler.py
│   │   └── pdf_generator.py
│   ├── utils/
│   │   └── security.py
│   └── tests/
│       ├── data/
│       │   └── fixtures.py
│       ├── test_api.py
│       ├── test_file_handler.py
│       ├── test_pdf_generator.py
│       ├── test_security.py
│       └── test_data/
│           └── test_sample.csv
├── templates/
│   ├── template.xml
│   └── template.xsl
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## How To Install (Mac/Linux)

### 1. Install Homebrew

If you do not already have Homebrew installed, run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install pyenv

Update Homebrew and install pyenv:

```bash
brew update
brew install pyenv
```

Then, add pyenv to your shell configuration. For example, if you’re using zsh, add the following to your `~/.zshrc` (or to `~/.bashrc` if you use bash):

```bash
# pyenv configuration
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
```

Reload your shell:

```bash
source ~/.zshrc  # or source ~/.bashrc
```

### 3. Install Python 3.9.21

Use pyenv to install Python 3.9.21:

```bash
pyenv install 3.9.21
pyenv global 3.9.21
```

Verify the installation:

```bash
python --version  # Should display: Python 3.9.21
```

### 4. Create a Virtual Environment

From the root of the project, create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 5. Install Project Dependencies

Upgrade pip and install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Run the Application

Start the application using uvicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```

The API will be accessible at [http://localhost:3000](http://localhost:3000). Verify its functionality by visiting the interactive API docs at [http://localhost:3000/docs](http://localhost:3000/docs).

### 7. Test the Application

To confirm that the application is running, you can:

- Open your browser and navigate to [http://localhost:3000/docs](http://localhost:3000/docs) to view the API documentation.
- Or run the following command in your terminal:

```bash
curl http://localhost:3000/
```

## Docker & Docker Compose

### Installing Docker

#### On Mac:

- Download and install **[Docker Desktop for Mac](https://www.docker.com/products/docker-desktop)**.
- Follow the installer instructions and ensure Docker Desktop is running.

#### On Linux:

- Follow the official Docker documentation for installing Docker on Linux. For example, on Ubuntu:

  ```bash
  sudo apt-get update
  sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

- Verify the installation by running:

  ```bash
  docker --version
  ```

### Cloning and Building the Project

1. **Clone the Project:**

   ```bash
   git clone https://github.com/your-username/atdev-technical-assessment.git
   cd atdev-technical-assessment
   ```

2. **Build the Container:**

   Use Docker Compose to build the image and start the container:

   ```bash
   docker-compose up --build
   ```

3. **Verify the Container is Running:**

   Check that the container is running with:

   ```bash
   docker ps
   ```

   Look for a container that exposes port `3000`.

4. **Test the Connection to Port 3000:**

   From your browser or using `curl`, verify that the API is accessible:

   - **Browser:** Visit [http://localhost:3000](http://localhost:3000) (or use your server's IP if on Linux).
   - **Terminal:**

     ```bash
     curl http://localhost:3000/
     ```

## Running Tests

To execute all unit and integration tests, run:

```bash
pytest --maxfail=1 --disable-warnings -q
```

## Contributing

Contributions are welcome! Please follow best development practices and include unit tests for any significant changes.

## License

This project is distributed under the GNU General Public License (GPL).  
For more details, see the [LICENSE](LICENSE) file.
```

---
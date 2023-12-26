# Contributing to Taysen Academy

Thank you for considering contributing to Taysen Academy! We welcome contributions from the community to enhance the platform and make it even better. Before you start, please take a moment to read the following guidelines.

## Development Environment

Taysen Academy is built using the following technologies:

- **Django**: A high-level Python web framework.
- **GraphQL**: A query language for APIs.
- **PostgreSQL**: A powerful, open-source relational database.
- **Vercel**: The platform where the application is deployed.

Before you start contributing, make sure you have the following installed:

- Python (with pip)
- Node.js
- PostgreSQL
- Git

## Setting Up the Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/taysenacademy/taysen-academy.git
   cd taysen-academy
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   # Assuming PostgreSQL is installed and running
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Visit `http://localhost:8000` in your browser to view the application.

## Making Contributions

1. **Fork the repository**: Click on the "Fork" button on the top right of the [Taysen Academy repository](https://github.com/suwilanji-chipofya-hadat/taysen-academy-backend).

2. **Create a new branch**: Create a new branch for your contribution:
   ```bash
   git checkout -b feature/new-feature
   ```

3. **Make changes**: Implement your changes and ensure that your code follows the project's coding standards.

4. **Testing**: Run tests to ensure that your changes do not break existing functionality:
   ```bash
   python manage.py test
   ```

5. **Commit your changes**: Please write meaningful commit messages:
   ```bash
   git commit -m "Add new feature"
   ```

6. **Push your changes**: Push your changes to your forked repository:
   ```bash
   git push origin feature/new-feature
   ```

7. **Create a Pull Request**: Open a pull request from your fork to the `main` branch of the Taysen Academy repository. Provide a detailed description of your changes.

## Code of Conduct

Please note that Taysen Academy has a [Code of Conduct](CODE_OF_CONDUCT.md) in place. We expect all contributors to adhere to it.

## Contact

If you have any questions or need assistance, feel free to reach out to us at [hadat_hq@outlook.com](mailto:hadat_hqcontributors@outlook.com).

Thank you for contributing to Taysen Academy!

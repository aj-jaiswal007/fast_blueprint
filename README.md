# FastAPI Blueprint

FastAPI Blueprint is a comprehensive blueprint project designed to accelerate your development process and get you up and running with a production-grade FastAPI application in no time. Whether you're a seasoned developer or just starting out, this project provides a solid foundation packed with essential features and configurations.

## Features

- **Postgres DB Integration**: Seamlessly integrate your FastAPI application with a PostgreSQL database using SQL Alchemy, ensuring efficient data management and scalability.

- **Linter with pre commit hooks**: Say no to unformatted code, pre-commit hooks to the rescue.

- **Dockerized App**: Deploy your application effortlessly with Docker, allowing for easy setup and portability across different environments.

- **Alembic for DB Migrations**: Simplify database schema management with Alembic, enabling smooth and hassle-free migrations as your application evolves.

- **Structured Logging Configuration**: Utilize structured logging with structlog to enhance visibility into your application's behavior and performance.

- **Heartbeat Endpoints**: Implement heartbeat endpoints for service health checks, ensuring your application is always up and running smoothly.

- **JWT-based User Authentication**: Secure your application with JWT-based user authentication, providing robust security measures to protect sensitive data.

- **Role-based Access Control**: Define fine-grained access control with role-based permissions, allowing you to manage user privileges effectively.

- **Access Token and User CRUD APIs**: Quickly set up access token management and user CRUD operations with out-of-the-box APIs, saving you time and effort in development.

- **Unit Testing with Pytest**: Ensure the reliability of your application with unit tests built using the Pytest framework, complete with pre-defined test cases for user APIs.

- **Global Exception Handler**: Centralised place to handle all your exceptions.



## Getting Started

1. Clone the repository:

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    ```bash
    cp .env.example .env
    ```

4. Update `.env` with your PostgreSQL database credentials and other configurations.

5. Generate migrations:
    ```bash
    alembic revision — autogenerate -m “First commit”
    ```

5. Run migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the FastAPI server:
   ```bash
   make run
   ```
   To run the dockerised version:
   ```bash
   make restart
   ```

## White label your project
- Rename the top level folder (project) name from `blueprint` to your own name.
- Search for `blueprint` in the codebase and replace all occurances with the new name.

## Running tests
- Install pytest
```bash
pip install pytest
```
- Run tests
```bash
pytest
```

## Contributing

We welcome contributions from the community to further enhance FastAPI Blueprint. Feel free to submit bug reports, feature requests, or pull requests on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to adjust or expand upon any section to better fit your project's specifics!

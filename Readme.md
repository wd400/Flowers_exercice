# INRIA Flowers exercice

This project is a full-stack application that uses Flask for the backend API and Angular for the frontend UI. The backend API provides a RESTful interface for managing a database of examples and training a deep learning model. The frontend UI provides an interface for interacting with the API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installing

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Running the Application

The application can be run using Docker Compose. This will start both the Flask API and the Angular UI.

```sh
docker-compose up
```

The Angular UI will be available at http://localhost:4000



## Built With

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - The web framework used for the backend API.
- [Angular](https://angular.io/) - The web framework used for the frontend UI, V18.
- [Docker](https://www.docker.com/) - Used for containerization and deployment.
- [Docker Compose](https://docs.docker.com/compose/) - Used for defining and running multi-container Docker applications.


## Improvements

- Add a more resilient database solution.
- Make the UI more user friendly.
- Add more unit tests.
- Add more error handling.
- Add more tailored types for the API.
- Multilang/dark mode for the UI.
- ...


## License

MIT License
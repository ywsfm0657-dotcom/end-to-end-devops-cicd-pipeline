# End-to-End DevOps CI/CD Pipeline

A portfolio project for practicing application testing, Docker, Jenkins Pipeline-as-Code, and Kubernetes deployment manifests.

## Architecture

1. A small Flask web application exposes `/` and `/health`.
2. Unit tests validate the HTTP endpoints.
3. Docker packages the application into an image.
4. Jenkins runs tests, builds the image, and performs a container smoke test.
5. Kubernetes manifests describe a two-replica Deployment and a ClusterIP Service.

## Repository layout

```text
.
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── test_app.py
├── k8s/
│   └── deployment.yaml
├── Dockerfile
├── compose.yaml
├── Jenkinsfile
└── README.md
```

## Run locally

Requirements: Python 3 and Docker with the Compose plugin.

### Run with Python

```bash
cd app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000/` and `http://localhost:5000/health`.

Run tests from the `app` directory:

```bash
python -m unittest -v
```

### Run with Docker Compose

From the repository root:

```bash
docker compose up --build -d
docker compose ps
curl http://localhost:5000/health
docker compose logs -f
docker compose down
```

## Jenkins pipeline

The included `Jenkinsfile` demonstrates checkout, unit tests, Docker image building, and a container smoke test. The Jenkins agent must have Python 3, Docker CLI/daemon access, and `curl` installed.

Create a Pipeline job in Jenkins and configure it to load the `Jenkinsfile` from this repository (Pipeline script from SCM). Configure Docker access securely; do not expose the Docker socket or give broad privileges without understanding the risks.

## Kubernetes deployment

1. Build and publish the image to a registry such as Docker Hub.
2. Edit `k8s/deployment.yaml` and replace `YOUR_DOCKERHUB_USERNAME` with your registry username.
3. Apply the manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl get deployments,pods,services
kubectl rollout status deployment/devops-demo-app
kubectl port-forward service/devops-demo-app 8080:80
```

Open `http://localhost:8080/health`.

The image must be published to a registry accessible by your cluster before deployment.

## Suggested next improvements

- Add a GitHub webhook trigger.
- Publish versioned images to Docker Hub from Jenkins using credentials stored in Jenkins Credentials.
- Add Terraform to provision a test environment.
- Add Prometheus and Grafana for monitoring.
- Add a rollback demonstration and document the results.

## CV description (use after you have run and verified the project)

**End-to-End DevOps CI/CD Pipeline**
- Built a Flask application with unit tests and a health endpoint.
- Containerized the application using Docker and Docker Compose.
- Created a Jenkins pipeline for testing, image building, and container smoke testing.
- Prepared Kubernetes Deployment and Service manifests with readiness/liveness probes and resource requests/limits.

## Safety notes

Never commit passwords, access keys, tokens, or private credentials.
Do not claim cloud deployment or automated registry publishing until you have implemented and tested those parts.

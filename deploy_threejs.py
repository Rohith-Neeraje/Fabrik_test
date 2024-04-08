import subprocess
import requests

def check_docker_installed():
    """Check if Docker is installed on the target machine."""
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE)
        print("Docker is already installed.")
    except subprocess.CalledProcessError:
        print("Docker is not installed.")
        install_docker()

def install_docker():
    """Install Docker on the target machine."""
    print("Installing Docker...")
    subprocess.run(["curl", "-fsSL", "https://get.docker.com", "-o", "get-docker.sh"], check=True)
    subprocess.run(["sudo", "sh", "get-docker.sh"], check=True)
    print("Docker installed successfully.")

def pull_docker_image(image_name):
    """Pull the Docker image for the three.js editor application."""
    print(f"Pulling Docker image: {image_name}")
    try:
        subprocess.run(["docker", "pull", image_name], check=True)
        print("Docker image pulled successfully.")
    except subprocess.CalledProcessError:
        print("Failed to pull Docker image. Make sure the image exists.")

def start_docker_container(image_name, container_name, port_mapping):
    """Start the Docker container with the specified configuration."""
    print("Starting Docker container...")
    try:
        subprocess.run(["docker", "run", "-d", "-p", port_mapping, "--name", container_name, image_name], check=True)
        print("Docker container started successfully.")
    except subprocess.CalledProcessError:
        print("Failed to start Docker container.")

def verify_application_accessibility(container_name, port):
    """Verify that the application is running and accessible."""
    print("Verifying application accessibility...")
    try:
        response = requests.get(f"http://localhost:{port}")
        if response.status_code == 200:
            print("Application is running and accessible.")
        else:
            print("Application is not accessible.")
    except requests.RequestException:
        print("Failed to connect to the application.")

if __name__ == "__main__":
    # Configuration
    IMAGE_NAME = "rohithneeraje/editor:latest"
    CONTAINER_NAME = "threejs-editor"
    PORT_MAPPING = "8080:8080"

    # Check if Docker is installed
    check_docker_installed()

    # Pull Docker image
    pull_docker_image(IMAGE_NAME)

    # Start Docker container
    start_docker_container(IMAGE_NAME, CONTAINER_NAME, PORT_MAPPING)

    # Verify application accessibility
    verify_application_accessibility(CONTAINER_NAME, 8080)

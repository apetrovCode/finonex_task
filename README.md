# finonex_task
Kubernetes-based Microservices Architecture on AWS EC2

Features
Nginx Ingress Controller: Manages path-based routing to the microservices.
Scalability: The Scale Service autoscales based on CPU utilization, with 80% as the threshold.
Database: A shared MySQL service that houses the customers database feeding the Content Service.
Terraform: Infrastructure-as-code using Terraform for provisioning EC2 and related AWS resources. Found in the main branch.
Helm Charts: Each service branch has its own Helm chart for deployment.

1. Architecture Overview
The system is a web application running on a single-node Kubernetes cluster provisioned on an AWS EC2 instance. The application is composed of four distinct microservices:

Name Service: Provides a random name upon request.
Number Service: Provides a random number upon request.
Content Service: Retrieves a list of customer names from a MySQL database.
Scale Service: A CPU-intensive service to demonstrate Kubernetes' autoscaling capabilities.
The services are exposed via an Nginx ingress controller responsible for path-based routing.

2. Advantages
Scalability: The application's microservices architecture ensures each service can be independently scaled. If the CPU utilization for the Scale Service crosses 80%, Kubernetes can automatically scale the number of pods.

Maintainability: Each service is containerized, ensuring consistency in environments and isolating application dependencies. If one service needs an update or encounters an issue, it can be modified without affecting the others.

Efficient Resource Usage: With Kubernetes, the resources (CPU and Memory) are used efficiently as the pods can share the same node, allowing for better resource optimization.

Rapid Deployment & Rollback: Using Helm, the entire stack can be deployed or rolled back to a previous version with a single command.

Extensibility: New services or updates can be integrated into the existing architecture with ease, making it future-proof.

3. Downsides
Single Point of Failure: The use of a single-node Kubernetes cluster presents a significant risk. If the node fails, the entire application will be unavailable.

Complexity: Kubernetes, even in a single-node setup, can be overkill for small projects and introduces unnecessary complexity.

Performance Overhead: Running a container orchestration system on a single node might introduce overhead which can impact the performance of the applications running on it.

Security Concerns: Exposing the application through an ingress controller requires careful security considerations, especially when integrating with databases and handling user data.

4. Additional Modules Description
As per instructions there is a 4th service(scale-service) that can be used to test the scalability of the other services.





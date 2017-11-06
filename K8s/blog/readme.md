# Container Orchestrator: Kubernetes on Azure

The container frenzy is in full swing across the IT universe and it has likely engulfed you and your organization as well. And why should it not? Containers have fundamentally changed the way developers develop their applications, the way applications are deployed, and the way system administrators manage their environments. Containers offer a broadly accepted and open standard, enabling simple portability between platforms and between clouds. On top of all that, containers give control of the applications, their dependencies as well as the infrastructure that they run on back to developers instead of having the operations teams having to manage it all on behalf of the development teams. 

By abstracting the infrastructure binaries, containers put the onus of uptime back in the hands of the development teams. No longer is compiled code and the dictated configurations for said code, going to be handed over to operations teams to be run and maintain. Instead, development teams output a fully *vetted* Docker image which contains the application code, its dependencies as well as the required configurations. 

The application that manage the containers is called a container orchestrator. The process of orchestration typically involves tooling that can automate all aspects of application management from initial placement, scheduling and deployment to steady-state activities such as update, deployment, update and health monitoring functions that support scaling and failover.

The orchestrator being discussed here is Kubernetes, and the reason for that  is because it's emerging as the front runner in the orchestration space. The Azure platform has three services that make it easy to deploy and manage Kubernetes clusters. The services are, Azure Kubernetes managed Service (aka AKS), Azure Container Service Engine (aka ACS-engine), and Azure Container Instance.

**Why should you use Kubernetes?**

Kubernetes has the most momentum going and as such both community and adoption is strong. The application has been proven at scale and is evolving constantly. It is the only orchestrator that has *cloud-provider* concept natively, which allows seamless integration into public clouds such as Microsoft Azure, Amazon Web Services and Google Cloud Platform. With cloud providers making investments in services such as AKS, ACS-Engine, ACI and GKE, it is the best bet to win the war of orchestrators.

**Let's expand on the services available to manage Kubernetes on Azure.**
### Azure Kubernetes Service (aka AKS)
Recently released service in preview makes it easier to manage and operate Kubernetes environments, all without sacrificing portability. AKS features an Azure-hosted control plane, automated upgrades, self-healing, easy scaling, and a simple user experience for both developers and cluster operators. With AKS, customers get the benefit of open source Kubernetes without complexity and operational overhead. AKS is free and you only pay for the consumption resulting from agent nodes and the infrastructure associated with them.

### Azure Container Instance - Kubernetes Connector (Preview)
An Azure Container Instance is a single container that starts in seconds and is billed by the second. ACI offer highly versatile sizing, allowing you to select the exact amount of memory separate from the exact count of vCPUs, so your application perfectly fits on the infrastructure. 

The Azure Container Instances Connector for Kubernetes allows Kubernetes clusters to deploy Azure Container Instances. This enables on-demand and nearly instantaneous container compute, orchestrated by Kubernetes, without having VM infrastructure to manage and while still leveraging the portable Kubernetes API. This will allow you to utilize both VMs and container instances simultaneously in the same Kubernetes cluster, giving you the best of both worlds.

### OTHER OPTIONS
### Azure Container Service Engine (aka ACS-Engine)
Currently there is a service called Azure Container Service (ACS) which will be deprecated in favor of a managed Kubernetes service described above (AKS). However, there is still an open-source project called ACS-Engine which can be used to deploy unmanaged clusters on the Azure platform. The Azure Container Service Engine (acs-engine) generates ARM (Azure Resource Manager) templates for Docker enabled clusters on Microsoft Azure with your choice of DCOS, Kubernetes, or Swarm orchestrators. The input to acs-engine is a cluster definition file which describes the desired cluster, including orchestrator, features, and agents. 

### Deploying Cluster on Azure VMs manually (Hard-way)
The last option to deploy an orchestrator is to deploy generic Azure VMs and installing and configuring the appropriate orchestrator from scratch. This is the most cumbersome method of deployment and management but allows the most control over the deployed orchestrator. 

## Rules of thumb

**Azure Kubernetes Service**: Use AKS when you want the Kubernetes Application managed for you. 

**Azure Container Service - Engine**: Use ACS-Engine when you want an unmanaged Kubernetes deployment but do not want to worry about the deployment and configuration of bringing up a K8s cluster.

**Kubernetes on Azure VMs**: Deploy K8s on Azure VMs when you want full control on what is being executed to bring up the cluster.

**Azure Container Instance - Kubernetes Connector**: Use this service to have your cluster burst its computing capacity for short periods of time.

## Community Call
If you'd like to hear more on this topic, we encourage you to attend the Microsoft Azure Apps and Infrastructure Community Call on Friday November 17th.  We'll have a conversational dialogue between two technology professionals that is designed to appeal to both technical professionals as well as sales or business professionals; providing insight to what is most important in the Microsoft Partner Ecosystem. One person will talk about Containers from an Infrastructure perspective, the other from an application development perspective. No death by PowerPoint!

Please register at the following link: https://msuspartner.eventbuilder.com/event?eventid=h9r2x7

# References
* [Case Study](https://azure.microsoft.com/en-us/resources/videos/docker-metlife/) 
* [AKS Announcement Video](https://azure.microsoft.com/en-us/resources/videos/azure-friday-managed-kubernetes-in-azure-container-service-aks/)
* [ACI - Kubernetes Connector](https://azure.microsoft.com/en-us/resources/videos/using-kubernetes-with-azure-container-instances/)
* [Jenkins Plugins for Kubernetes](https://azure.microsoft.com/en-us/resources/videos/azure-friday-jenkins-plugins-for-kubernetes/)
* [Azure Container Registry General Availability](https://azure.microsoft.com/en-us/resources/videos/azure-container-registry-general-availability/)
* [Use Helm with Azure Container Service and Kubernetes
](https://azure.microsoft.com/en-us/resources/videos/use-helm-with-azure-container-service-and-kubernetes/)
* [Azure Container Registry Geo-replication
](https://azure.microsoft.com/en-us/resources/videos/azure-friday-azure-container-registry-geo-replication/)

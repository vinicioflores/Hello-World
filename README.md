# Hello-World
Frontend, Kubernetes containerized app build with Flask as runtime (listening on 8080 port as default HTTP REST API standards) . Includes ARM template to deploy via Azure Portal.


``az group create --name NetworkWatcherRg --location eastus``

After creating a resource group in Azure (NetworkWatcherRg)  based on East US initially, we can create more to be able to countabilize costs based on GEOs for example (AMR, LATAM, APAC, EMEA)

Run all these commands using embedded Powershell in Azure Portal  ==> ``az aks create --resource-group NetworkWatcherRg --name KSClusterPOC --node-count 1 --enable-addons monitoring --generate-ssh-keys``

Then install the Kubernetes client application *kubectl* as well *helm* package manager that will be useful for us to provision monitoring and CI/CD tools in the future (allows you to interact with the cluster and deploy apps)

``az aks install-cli``


Then, for security purposes & and as requirement for Kubernetes Azure instance, credentials need to be stored:

``az aks get-credentials --resource-group NetworkWatcherRg --name myAKSCluster``

Now one simple way to lookup whether the Kubernetes (server side) is up and running by checking if at least it has 1 node UP

``kubectl get nodes``

If there's a node and cluster is up, the proceed to deploy via *kubectl* and provide your YAML file

``kubectl apply -f deployment.yaml``

Now as architects we need to ensure that we have a single centralized place where app's logs arrive so it's easier to maintain in the longer term and easier for developers to debug.

Let's install prometeus as our (proactive monitoring tool to collect defautl stats such as I/O, network latency, etc. ) as well as Grafana to display all that visually. Grafana is already bundled together with Prometheus.

``helm install --name sampleapp stable/prometheus-operator``




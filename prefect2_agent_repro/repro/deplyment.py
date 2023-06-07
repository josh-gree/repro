from prefect.deployments import Deployment
from prefect.infrastructure import KubernetesJob

from prefect2_agent_repro.repro.flow import repro

infra = KubernetesJob(
    image="prefect2agentrepro:latest",
    image_pull_policy="Never",
    namespace="prefect",
)

deployment = Deployment.build_from_flow(
    repro,
    name="repro",
    infrastructure=infra,
    infra_overrides={"namespace": "prefect"},
    work_queue_name="default",
    path="/usr/local/lib/python3.9/site-packages",
)

if __name__ == "__main__":
    deployment.apply()

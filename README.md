```
> minikube start
> eval $(minikube docker-env)
> eval $(minikube -p minikube docker-env)
> kubectl apply -f ./k8s_manifests/manifest.yml
```

```
> prefect server database reset --yes
> prefect server start --log-level DEBUG
```

```
> docker build --pull --rm -f "Dockerfile" -t prefect2agentrepro:latest "."
```

```
> python prefect2_agent_repro/repro/deplyment.py
> prefect deployment run 'repro/repro'
```

```
10:57:39.193 | INFO    | prefect.flow_runs.worker - Worker 'KubernetesWorker 9a427d43-e8c3-48e2-912b-3483ac2c2f6b' submitting flow run '5d473698-8719-432e-a165-c19c584e07c1'
10:57:39.365 | INFO    | prefect.flow_runs.worker - Creating Kubernetes job...
10:57:39.402 | ERROR   | prefect.flow_runs.worker - Failed to submit flow run '5d473698-8719-432e-a165-c19c584e07c1' to infrastructure.
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/prefect/workers/base.py", line 827, in _submit_run_and_capture_errors
    result = await self.run(
  File "/usr/local/lib/python3.9/site-packages/prefect_kubernetes/worker.py", line 503, in run
    pid = await run_sync_in_worker_thread(
  File "/usr/local/lib/python3.9/site-packages/prefect/utilities/asyncutils.py", line 91, in run_sync_in_worker_thread
    return await anyio.to_thread.run_sync(
  File "/usr/local/lib/python3.9/site-packages/anyio/to_thread.py", line 33, in run_sync
    return await get_asynclib().run_sync_in_worker_thread(
  File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 877, in run_sync_in_worker_thread
    return await future
  File "/usr/local/lib/python3.9/site-packages/anyio/_backends/_asyncio.py", line 807, in run
    result = context.run(func, *args)
  File "/usr/local/lib/python3.9/site-packages/prefect_kubernetes/worker.py", line 657, in _get_infrastructure_pid
    cluster_uid = self._get_cluster_uid(client)
  File "/usr/local/lib/python3.9/site-packages/prefect_kubernetes/worker.py", line 705, in _get_cluster_uid
    namespace = core_client.read_namespace("kube-system")
  File "/usr/local/lib/python3.9/site-packages/kubernetes/client/api/core_v1_api.py", line 22476, in read_namespace
    return self.read_namespace_with_http_info(name, **kwargs)  # noqa: E501
  File "/usr/local/lib/python3.9/site-packages/kubernetes/client/api/core_v1_api.py", line 22555, in read_namespace_with_http_info
    return self.api_client.call_api(
  File "/usr/local/lib/python3.9/site-packages/kubernetes/client/api_client.py", line 348, in call_api
    return self.__call_api(resource_path, method,
  File "/usr/local/lib/python3.9/site-packages/kubernetes/client/api_client.py", line 180, in __call_api
    response_data = self.request(
  File "/usr/local/lib/python3.9/site-packages/kubernetes/client/api_client.py", line 373, in request
    return self.rest_client.GET(url,
  File "/usr/local/lib/python3.9/site-packages/kubernetes/client/rest.py", line 241, in GET
    return self.request("GET", url,
  File "/usr/local/lib/python3.9/site-packages/kubernetes/client/rest.py", line 235, in request
    raise ApiException(http_resp=r)
kubernetes.client.exceptions.ApiException: (403)
Reason: Forbidden
HTTP response headers: HTTPHeaderDict({'Audit-Id': 'e86272f0-aa68-4ea4-96ad-5b082a5c8587', 'Cache-Control': 'no-cache, private', 'Content-Type': 'application/json', 'X-Content-Type-Options': 'nosniff', 'X-Kubernetes-Pf-Flowschema-Uid': '4fc75ea6-37ad-434a-9bc0-b761a8eb7184', 'X-Kubernetes-Pf-Prioritylevel-Uid': '22cde4aa-8fef-4d7d-a048-d5eb2d77ff2d', 'Date': 'Wed, 07 Jun 2023 10:57:39 GMT', 'Content-Length': '347'})
HTTP response body: {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"namespaces \"kube-system\" is forbidden: User \"system:serviceaccount:prefect:prefect-worker\" cannot get resource \"namespaces\" in API group \"\" in the namespace \"kube-system\"","reason":"Forbidden","details":{"name":"kube-system","kind":"namespaces"},"code":403}


10:57:39.427 | INFO    | prefect.flow_runs.worker - Completed submission of flow run '5d473698-8719-432e-a165-c19c584e07c1'
```

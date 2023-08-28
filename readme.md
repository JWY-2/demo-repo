# Demo

## Demo Requirements
### What you should have before you start
1. A K8s cluster `API endpoint`
2. A K8s cluster `access token`
3. A set of `client key/certificate` data with the token above
4. A `Github repository` to store and version your demo code

### What the API needs to do
Write a simple API in Python using a framework of your choice that has the following endpoints:
1. POST `/file` - takes a json structure as body param and writes it in memory or on disk, returns a file ID integer
Request example:
`POST /file`
```json
{
    "data": {
        "firstName": "Geralt",
        "lastName": "Of Rivia"
    }
}
```
Response example:
```json
{
    "fileId": 1
}
```



2. GET `/file/{fileId}` - returns the json structure of a file stored in the previous endpoint
Request: `GET /file/1`

Response example:
```json
{
    "firstName": "Geralt",
    "lastName": "Of Rivia"
}

```

3. GET `/version` - returns the version of the API that should be parameterizable at deployment time
Request: `GET /version`

Response example:
```json
{
    "version": "0.0.1"
}
```

### How the API should be deployed
1. Wrap the API code in a docker container and deploy it on the given K8s cluster.
2. Make sure you deploy using your helm chart and can deploy 2 releases with differing parameter (i.e. `version` of the API)
3. Deploy it using any resource types you think of. The API should be publicly available through some IP address (Hint: AKS automatically binds a LoadBalancer to a `LoadBalancer` type service)
4. You can use any external supporting Helm charts if you see the need for it, but it is not a requirement.

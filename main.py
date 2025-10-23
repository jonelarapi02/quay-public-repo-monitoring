import requests

url = "https://dso-quay-registry-quay-quay-enterprise.apps.ocp4.azure.dso.digital.mod.uk"
params = {
    "public": "true",
    "popularity": "true",
    "page": 1,
    "page_size": 100
}

public_repos = []

while True:
    response = requests.get(url, params=params)
    data = response.json()

    for repo in data.get("repositories", []):
        name = repo.get("name")
        namespace = repo.get("namespace")
        repo_url = f"https://quay.io/repository/{namespace}/{name}"
        public_repos.append(f"{namespace}/{name} - {repo_url}")

    if not data.get("has_additional", False):
        break
    params["page"] += 1

with open("public_quay_repos.txt", "w") as f:
    for repo in public_repos:
        f.write(repo + "\n")

print(f"Saved {len(public_repos)} public repositories to public_quay_repos.txt.")

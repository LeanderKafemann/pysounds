import base64
import os

import requests

def upload_content_to_github(content: str, file_path: str, repo: str, token: str, branch: str, comment: str):
    """
    Uploads content to GitHub.
    content -- content that is uploaded
    file_path
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    repo_api_url = f"https://api.github.com/repos/{repo}"
    file_url = f"{repo_api_url}/contents/{file_path}"

    encoded_content = base64.b64encode(content.encode()).decode("utf-8")

    file_response = requests.get(file_url, headers=headers)
    file_exists = file_response.status_code != 404
    file_data = file_response.json() if file_exists else {}

    update_data = {
        "message": f"{comment}",
        "content": encoded_content,
        "branch": branch,
    }

    if "sha" in file_data:
        update_data["sha"] = file_data["sha"]

    response = requests.put(file_url, json=update_data, headers=headers)
    response.raise_for_status()

    print(f"Successfully uploaded content to {repo}/{branch}/{file_path}")


def upload_file_to_github(file: str, repo: str, token: str, branch: str = "main", alias: str = "", comment: str = ""):
    """
    Uploads given file to GitHub repository repo.
    Comments in branch branch and uses token token.
    Provide an alias to upload to a different path then the file is saved.
    Provide a comment to upload a comment different from "Update ...".
    """
    with open(file, "r") as f:
        content = f.read()
    
    if alias == "":
        alias = file
    alias_ = os.path.normpath(alias).replace("\\", "/")

    if comment == "":
        comment = "Update "+str(alias_).split("/")[-1]

    upload_content_to_github(content, alias, repo, token, branch, comment)

def about():
    """
    Return information about your release.
    """
    return {"version": "1.0.2", "author": "Leander Kafemann", "date": "22.10.2024", "feedbackTo": "leander@kafemann.berlin"}

def main():
    """
    Calls main functions with given data.
    """
    file_path = input("Enter path (C:/Users/abc/def.ghi or ./def.ghi): ")
    repo = input("Enter repository (Abc/def): ")
    token = input("Enter token: ")
    branch = input("Enter branch (main): ") or "main"
    alias = input("Enter alias name (./def/ghi.jkl): ")
    comment = input("Enter comment (Update ghi): ")
    upload_file_to_github(file_path, repo, token, branch, alias, comment)


if __name__ == "__main__":
    main()

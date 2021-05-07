# action-sharepoint-upload
This action will upload file to Sharepoint library


## Inputs

| Input name            | Required  | Description                                      | Example                                               |
| --------------------- | :-------: | ------------------------------------------------ | ----------------------------------------------------- |
| `site_url`            | **Yes**   | The Sharepoint site url                          | `https://you.sharepoint.com/sites/mySite`             |
| `sharepoint_user`     | **Yes**   | The username to use for authentication           | `bob.tester@funnypage.com`                            |
| `sharepoint_password` | **Yes**   | The user's password </br> ***Use GitHub Actions Secrets to store sensible informations*** | `MyPassword123!`   |
| `destination_folder`  | **Yes**   | The path relative to site where to upload a file | `/Shared documents/${{ github.repository }}/releases` |
| `local_file`          | **Yes**   | The path of the file you want to upload          | `${{ github.workspace }}/test.txt`                    |
| `remote_file`         |   No      | The name of the file on the sharepoint site      | `test_release.txt`                                    |


## Example usage 

You may use this action to store your artifacts on Sharepoint or to put application releases there.

```yml
name: 'Sharepoint release'

on:
  release:
    types: created

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
    
    - name: Cloning repo # This step is required
      uses: actions/checkout@v2

    - name: Sharepoint upload file
      uses: actions/action-sharepoint-upload@v1
      with:
        site_url: 'https://you.sharepoint.com/sites/mySite'
        sharepoint_user: ${{ secrets.USER }}
        sharepoint_password: ${{ secrets.PASS }}
        destination_folder: /Shared Documents/${{ github.repository }}
        local_file: "your file location"
        remote_file: "filename on the server"


```

Big credits to `https://github.com/obrassard/action-sharepoint-publish` work, which was a trigger to write this action.
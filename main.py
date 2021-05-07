import os
from office365.sharepoint.client_context import ClientContext

SITE_URL = os.getenv('SITE_URL')
USER = os.getenv('USER')
PASS = os.getenv('PASS')
DESTINATION = os.getenv('DESTINATION')
FILE = os.getenv('FILE')
FILE_ON_SERVER = os.getenv('FILE_ON_SERVER')


def main():
    ctx = ClientContext(SITE_URL).with_user_credentials(USER,PASS)

    path = FILE
    with open(path, 'rb') as content_file:
        file_content = content_file.read()

    target_url = DESTINATION
    target_folder = ctx.web.ensure_folder_path(target_url).execute_query()
    name = FILE_ON_SERVER
    if not name:
        name = os.path.basename(path)
    target_file = target_folder.upload_file(name, file_content)
    ctx.execute_query()

    print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))


if __name__ == "__main__":
    main()

import webdav.client as wc

# Create WebDAV server/login details object
details = {
 'webdav_hostname': "https://dav.box.com/dav/",
 'webdav_login':    "your_user",
 'webdav_password': "your_pass"
}
client = wc.Client(details)

# Create a resource
client.mkdir("folder1/folder2")

# Check for existence of a resource
client.check("folder1/file1")
client.check("folder1")

# Delete a resource (careful)
client.clean("folder1/folder2")

# Copy a resource to another location within Box
client.copy(remote_path_from="folder1/file1", remote_path_to="folder2/file1")
client.copy(remote_path_from="folder1", remote_path_to="folder2")

# Move a resource to another location within Box
client.move(remote_path_from="folder1/file1", remote_path_to="folder2/file1")
client.move(remote_path_from="folder1", remote_path_to="folder2")

# Download a resource to your local environment
client.download_sync(remote_path="folder1/file1", local_path="~/Downloads/file1")
client.download_sync(remote_path="folder1/folder2/", local_path="~/Downloads/folder/")

# Upload a resource from your local environment
client.upload_sync(remote_path="folder1/file1", local_path="~/Documents/file1")
client.upload_sync(remote_path="folder1/folder2/", local_path="~/Documents/folder1/")

# Check free space on Box
free_size = client.free()

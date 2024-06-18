import requests

def scan_target(openvas_url, username, password, target_ip):
  """
  Initiates a vulnerability scan on a target IP using OpenVAS Manager API.

  Args:
      openvas_url (str): The URL of the OpenVAS Manager API.
      username (str): Username for OpenVAS Manager access.
      password (str): Password for OpenVAS Manager access.
      target_ip (str): The IP address of the target to scan.

  Returns:
      str: A message indicating the scan creation status.
  """
  # Base URL for OpenVAS Manager API
  base_url = f"{openvas_url}/api/v1/"

  # Authentication
  auth = (username, password)

  # Scan configuration (replace with your desired scan configuration ID)
  scan_config_id = 1  # Replace with your OpenVAS scan configuration ID

  # Create a new scan task
  url = f"{base_url}tasks"
  data = {
    "name": f"Scan of {target_ip}",
    "config": scan_config_id,
    "targets": f"[{target_ip}]"
  }

  response = requests.post(url, auth=auth, json=data)

  if response.status_code == 201:
    # Scan creation successful
    scan_id = response.json()["id"]
    return f"Scan task created successfully for target {target_ip} (Scan ID: {scan_id})"
  else:
    # Error creating scan task
    return f"Failed to create scan task for target {target_ip}: {response.reason}"

# Replace with your OpenVAS Manager details and target IP
openvas_url = "http://localhost:4443"  # Replace with your OpenVAS Manager URL
username = "admin"
password = "password"  # Replace with your credentials
target_ip = "192.168.1.100"  # Replace with the target IP to scan

# Initiate the vulnerability scan
scan_message = scan_target(openvas_url, username, password, target_ip)
print(scan_message)

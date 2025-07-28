import os
from datetime import datetime

project_name = "automationexer"
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

folders = [
    f"{project_name}/tests",
    f"{project_name}/pages",
    f"{project_name}/utils",
    f"{project_name}/reports/{timestamp}",
    f"{project_name}/logs/{timestamp}",
    f"{project_name}/screenshots/{timestamp}"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

files = [
    f"{project_name}/conftest.py",
    f"{project_name}/requirements.txt",
    f"{project_name}/pages/base_page.py",
    f"{project_name}/pages/login_page.py",
    f"{project_name}/tests/test_login.py",
    f"{project_name}/utils/logger.py"
]

for file in files:
    with open(file, 'w') as f:
        f.write("# " + os.path.basename(file))

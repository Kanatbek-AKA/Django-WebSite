# Not yet full look at the documentation on gitguardian 

import os
# import dotenv


API_KEY = os.getenv("API_KEY")
client = GGClient(api_key=API_KEY)



# Scan multiple, files ggshield
file_path = (pathlib.Path(name) for name in glob.iglob("**/**", resource=True))
to_scan = [{"filename": path.name, "document": path.read_text(errors="replace")} for path in file_path]
scan = client.multi_content_scan(to_scan)

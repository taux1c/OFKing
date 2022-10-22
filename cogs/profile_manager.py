from pathlib import Path
import config
from os import listdir
import cogs.prompt


# This is the master variable that stores the the profile locations.
def get_profiles():
    Path(config.profiles_folder).mkdir(parents=True, exist_ok=True)
    profiles = {name: Path(config.profiles_folder, name) for name in listdir(config.profiles_folder) if Path(config.profiles_folder, name).is_dir()}
    return profiles

def create_profile():
    profile_name = cogs.prompt.text("Enter a name for the profile: ")
    profile_path = Path(config.profiles_folder, profile_name).mkdir(parents=True, exist_ok=True)
    config_path = Path(config.profiles_folder, profile_name, "config.json")
    auth_path = Path(config.profiles_folder, profile_name, "auth.json")









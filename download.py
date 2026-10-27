import shutil
import kagglehub

path = kagglehub.competition_download("playground-series-s6e10")
shutil.copytree(path, "data", dirs_exist_ok=True)

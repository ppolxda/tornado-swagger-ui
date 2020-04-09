import pkg_resources
from PyInstaller.utils.hooks import collect_system_data_files

path = pkg_resources.resource_filename('tornado_swagger_ui', '')
datas = (
    collect_system_data_files(path)
)

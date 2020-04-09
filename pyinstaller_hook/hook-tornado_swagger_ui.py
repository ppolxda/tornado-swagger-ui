# import pkg_resources
from PyInstaller.utils.hooks import collect_data_files


datas = (
    collect_data_files(
        'tornado_swagger_ui.assets'  # noqa
    )
)
print('sdfsdfsdaf:', datas)

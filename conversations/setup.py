# -*- coding: utf-8 -*-
"""
    conversations
    ~~~~~~~~~~~~~

    Private messaging for FlaskBB

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
import ast
import re
from setuptools import find_packages, setup
from setuptools.command.install import install


with open("conversations/__init__.py", "rb") as f:
    version_line = re.search(
        r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
    ).group(1)
    version = str(ast.literal_eval(version_line))


class InstallWithTranslations(install):
    def run(self):
        # https://stackoverflow.com/a/41120180
        from babel.messages.frontend import compile_catalog  # noqa
        compiler = compile_catalog(self.distribution)
        option_dict = self.distribution.get_option_dict("compile_catalog")
        compiler.domain = [option_dict["domain"][1]]
        compiler.directory = option_dict["directory"][1]
        compiler.run()
        super().run()


setup(
    name="flaskbb-plugin-conversations",
    version=version,
    url="https://flaskbb.org",
    license="BSD License",
    author="Peter Justin",
    author_email="peter.justin@outlook.com",
    description="Private messaging for FlaskBB",
    long_description=__doc__,
    keywords="flaskbb plugin",
    cmdclass={"install": InstallWithTranslations},
    packages=find_packages("."),
    include_package_data=True,
    package_data={
        "": ["conversations/translations/*/*/*.mo",
             "conversations/translations/*/*/*.po"]
    },
    zip_safe=False,
    platforms="any",
    entry_points={
        "flaskbb_plugins": [
            "conversations = conversations"
        ]
    },
    install_requires=[
        "FlaskBB>=2.0.dev0"
    ],
    setup_requires=[
        "Babel",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)

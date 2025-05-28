import json
import os

from Context.CtxModule import CtxModule


class FileSystem(CtxModule):
    @staticmethod
    def scanDir(path: str, extensions: list[str] = None):
        matched_files = []

        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)

                if extensions and not any(file.lower().endswith(ext.lower()) for ext in extensions):
                    continue

                matched_files.append(full_path)

        return matched_files

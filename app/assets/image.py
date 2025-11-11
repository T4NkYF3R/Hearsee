import random
from pathlib import Path

from app import IMAGE, NB_IMAGE_SESSION


class Image:
    def __init__(self) -> None:
        self._allowedExtensions = (".png", ".jpg", ".jpeg", ".gif", ".bpm")
        self._files = self._loadImages()

    def _loadImages(self) -> list[str]:
        files = []
        for file in IMAGE.iterdir():
            if file.is_file():
                if file.suffix.lower() in self._allowedExtensions:
                    files.append(IMAGE / file.name)
                else:
                    print(f"[assets/image] Unsupported extension for file '{file.name}'")
        if len(files) < 8:
            raise RuntimeError(f"[assets/image] Images loaded: {len(files)}/{NB_IMAGE_SESSION} required.")
        return files

    def makeGroupeSession(self):
        session1 = []
        session2 = []
        for image in self._files:
            name = Path(image).stem
            if name.endswith("_1") is False and name.endswith("_2") is False:
                print(f"[assets/image] Wrong file nomenclature for '{name}'")
                continue
            baseName = name[:-2]
            if any(baseName in Path(img).stem[:-2] for img in session1 + session2):
                continue
            pair = [img for img in self._files if Path(img).stem.startswith(baseName)]
            if len(pair) < 2:
                print(f"[assets/image] '{name}' has no pair.")
                continue
            session1.append(pair[0] if Path(pair[0]).stem.endswith("_1") else pair[1])
            session2.append(pair[1] if Path(pair[1]).stem.endswith("_2") else pair[0])
        random.shuffle(session1)
        random.shuffle(session2)
        globalList = session1 + session2
        return globalList

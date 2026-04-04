import random
import shutil
from pathlib import Path

SOURCE_DIR = Path("dataset")
DEST_DIR = Path("dataset_split")
TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15
SEED = 42
SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

assert abs(TRAIN_RATIO + VAL_RATIO + TEST_RATIO - 1.0) < 1e-9

random.seed(SEED)

classes = [d for d in SOURCE_DIR.iterdir() if d.is_dir() and d.name != "skipped"]

for split in ["train", "val", "test"]:
    for cls in classes:
        (DEST_DIR / split / cls.name).mkdir(parents=True, exist_ok=True)

for cls in classes:
    files = [p for p in cls.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS]
    random.shuffle(files)

    n = len(files)
    n_train = int(n * TRAIN_RATIO)
    n_val = int(n * VAL_RATIO)
    train_files = files[:n_train]
    val_files = files[n_train:n_train + n_val]
    test_files = files[n_train + n_val:]

    for split_name, split_files in {
        "train": train_files,
        "val": val_files,
        "test": test_files,
    }.items():
        for f in split_files:
            shutil.copy2(f, DEST_DIR / split_name / cls.name / f.name)

    print(f"{cls.name}: train={len(train_files)}, val={len(val_files)}, test={len(test_files)}")

print(f"\nFinished. Split dataset saved in: {DEST_DIR.resolve()}")
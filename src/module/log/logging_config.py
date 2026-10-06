from datetime import datetime
import logging
from pathlib import Path


def logger():
    base_dir = Path().cwd()

    log_path = base_dir / "logs"

    log_path.mkdir(exist_ok=True, parents=True)

    arquivo_log = f"logs_{datetime.now():%Y-%m-%d}.log"

    logging.basicConfig(
        filename=f"logs/{arquivo_log}",
        level=logging.INFO,
        format="%(asctime)s | %(message)s",
        datefmt="%H:%M:%S",
        encoding="utf-8",
    )

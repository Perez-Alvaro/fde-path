"""Script mínimo para verificar Python, Pydantic y el debugger."""

import logging
import sys
from pydantic import BaseModel, Field

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


class EnvStatus(BaseModel):
    python_version: str = Field(..., description="Versión de Python en ejecución")
    ready: bool = True


def main() -> None:
    status = EnvStatus(
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    logger.info("Entorno verificado correctamente: %s", status.model_dump())


if __name__ == "__main__":
    main()

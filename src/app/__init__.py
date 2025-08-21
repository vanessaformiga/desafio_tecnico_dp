"""
Pacote principal do projeto.

Este módulo define configurações básicas, versão do pacote para a criação da APP
"""

__version__ = "0.1.0"


__all__ = [
    
]


import logging

logger = logging.getLogger(__name__)
if not logger.handlers:
   
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

logger.info("Pacote para a criação da APP carregado com sucesso!")
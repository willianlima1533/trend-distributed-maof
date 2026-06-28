import argparse
from packages.core import Engine, Orchestrator
from packages.utils.logging import setup_logging
from services.orchestrator import OrchestratorService

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logging-level', type=str, default='INFO')
    args = parser.parse_args()
    setup_logging(level=getattr(logging, args.logging_level.upper()))
    engine = Engine(orchestrator=Orchestrator(id='default'))
    orchestrator_service = OrchestratorService(engine=engine)
    orchestrator_service.start()

if __name__ == '__main__':
    main()
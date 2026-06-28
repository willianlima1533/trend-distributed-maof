from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

@dataclass
class Agent:
    id: str
    is_busy: bool = False

    def assign_task(self, task):
        # Implement task assignment logic here
        pass

    def get_task_status(self, task):
        # Implement task status retrieval logic here
        pass

@dataclass
class Task:
    id: str
    agent_id: str

class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4

@dataclass
class Orchestrator:
    id: str

    def register_agent(self, agent):
        # Implement agent registration logic here
        pass
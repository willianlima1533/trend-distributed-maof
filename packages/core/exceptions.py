class InvalidTaskException(Exception):
    pass

class AgentAlreadyRegisteredException(InvalidTaskException):
    pass

class NoAgentsAvailableException(InvalidTaskException):
    pass

class TaskNotFoundException(InvalidTaskException):
    pass

class AgentNotFoundException(Exception):
    """Exceção levantada quando um agente não é encontrado no registro."""
    pass


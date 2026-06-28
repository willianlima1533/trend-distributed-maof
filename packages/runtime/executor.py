import heapq
import time

class TaskExecutor:
    def __init__(self):
        # Fila de prioridade: (prioridade, timestamp, tarefa)
        self.queue = []

    def schedule_task(self, task_name, priority):
        """
        Agenda uma nova tarefa. Menor valor de prioridade = executada primeiro.
        """
        heapq.heappush(self.queue, (priority, time.time(), task_name))
        print(f"[LOG] Tarefa '{task_name}' agendada com prioridade {priority}")

    def execute_next(self):
        """
        Executa a próxima tarefa da fila baseada na prioridade.
        """
        if not self.queue:
            return None
        priority, _, task = heapq.heappop(self.queue)
        print(f"[LOG] Executando: {task} (Prioridade: {priority})")
        return task

# Exemplo de uso para teste rápido
if __name__ == "__main__":
    executor = TaskExecutor()
    executor.schedule_task("Limpeza de Memoria", 2)
    executor.schedule_task("Processamento de Dados", 1)
    
    executor.execute_next() # Deve rodar o Processamento de Dados (pri 1)


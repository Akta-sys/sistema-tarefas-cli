from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao="", prioridade="media", status="pendente", data_entrega=None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.data_entrega = data_entrega or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "data_entrega": self.data_entrega
        }
    
    @staticmethod
    def from_dict(data):
        return Tarefa(
            titulo=data["titulo"],
            descricao=data.get("descricao", ""),
            prioridade=data.get("prioridade", "media"),
            status=data.get("status", "pendente"),
            data_entrega=data.get("data_entrega")
        )
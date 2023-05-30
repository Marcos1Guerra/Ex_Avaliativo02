class TeacherDatabase:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Professor {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (p:Professor{name: $name}) RETURN p"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["p"] for result in results]

    def update(self, name, new_cpf):
        query = "MATCH (p:Professor {name: $name}) SET p.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)

    def delete_jogador(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)



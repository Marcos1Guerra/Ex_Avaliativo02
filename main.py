from database import Database
from teacher_database import TeacherDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.200.250.208:7687", "neo4j", "sting-technicians-manufacturers")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
professor = TeacherDatabase(db)

professor.create("Chris Lima", 1956,"189.052.396-66")

print("Professor: ")
print(professor.read("Chris Lima"))

professor.update("Chris Lima", "162.052.777-77")

db.close()
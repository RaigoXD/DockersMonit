import docker

class Dockers:

    def __init__(self):
        self.__client = docker.from_env()

    def list_containers(self, num: int = -1):
        if num == -1:
            containers = self.__client.containers.list(True)
        else:
            containers = self.__client.containers.list(True)[:num]
        info_containers = [
            [container.short_id, container.name, container.status.upper()]
            for container in containers
        ]
        return info_containers

    def container_logs(self,short_id:int):
        container = self.__client.containers.get(short_id)
        container.reload()
        return container.logs()
    
# dockersito = Dockers()
# gen_logs = dockersito.container_logs("d4a64d953e3e")
        
# for i in gen_logs:
#     print(i)
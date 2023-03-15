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
            [container.short_id[:5], container.name, container.status.upper()]
            for container in containers
        ]
        return info_containers


dockersito = Dockers()

print(dockersito.list_containers())

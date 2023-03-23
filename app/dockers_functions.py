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

    def container_logs(self,short_id):
        container = self.__client.containers.get(short_id)
        container.reload()
        return container.logs(tail = 30)
    
    def change_status_container(self,short_id, option: int):
        container = self.__client.containers.get(short_id)
        container.reload()
        if option == 1 and container.status == 'running':
            container.stop()
        elif option == 2 and container.status == 'exited':
            container.start()
        elif option == 3 and container.status == 'running':
            container.restart()
            
    def get_info_container(self, short_id):
        container = self.__client.containers.get(short_id)
        container.reload()
        command = " ".join(container.attrs['Args'])

        return (container.short_id, container.attrs['Config']['Image'],
                container.status, container.attrs['Created'],
                container.attrs['NetworkSettings']['Ports'], command
                )
        


# dockersito = Dockers()
# info = dockersito.get_info_container("d4a64d953e3e")
       
# print(info)
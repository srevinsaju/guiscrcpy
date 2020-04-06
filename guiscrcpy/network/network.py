
import socket
import multiprocessing
import subprocess
import os


class NetworkManager:

    def __init__(self):
        pass

    def pinger(self, job_q, results_q):
        """
        Do Ping
        :param job_q:
        :param results_q:
        :return:
        """
        DEVNULL = open(os.devnull, 'w')
        while True:

            ip = job_q.get()

            if ip is None:
                break

            try:
                subprocess.check_call(['ping', '-c1', ip], stdout=DEVNULL)
                results_q.put(ip)
            except:
                pass

    def get_my_ip(self):
        """
        Find my IP address
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def map_network(self, pool_size=255):
        """
        Maps the network
        :param pool_size: amount of parallel ping processes
        :return: list of valid ip addresses
        """

        ip_list = list()

        # get my IP and compose a base like 192.168.1.xxx
        ip_parts = self.get_my_ip().split('.')
        base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

        # prepare the jobs queue
        jobs = multiprocessing.Queue()
        results = multiprocessing.Queue()

        pool = [multiprocessing.Process(target=self.pinger, args=(
            jobs, results)) for i in range(pool_size)]

        for p in pool:
            p.start()

        # cue hte ping processes
        for i in range(1, 255):
            jobs.put(base_ip + '{0}'.format(i))

        for p in pool:
            jobs.put(None)

        for p in pool:
            p.join()

        # collect he results
        while not results.empty():
            ip = results.get()
            ip_list.append(ip)

        return ip_list


if __name__ == '__main__':
    print('Mapping...')
    nm = NetworkManager()
    lst = nm.map_network()
    print(lst)

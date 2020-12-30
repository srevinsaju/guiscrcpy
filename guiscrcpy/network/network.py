import logging
import socket
import threading
import time


class NetworkManager:
    @staticmethod
    def get_my_ip():
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
        ip_parts = self.get_my_ip().split(".")
        base_ip = ip_parts[0] + "." + ip_parts[1] + "." + ip_parts[2] + "."

        max_threads = 50

        def check_adb_port(ip):
            """
            Check if port is open
            :param ip:
            :param port:
            :return:
            """
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(2.0)
                result = sock.connect_ex((ip, 5555))
                if result == 0:
                    ip_list.append(ip)
                sock.close()
            except Exception as e:
                logging.warning("Unable to check %s: %s", ip, e)

        for i in range(1, 255):
            threading.Thread(
                target=check_adb_port,
                args=[f"{base_ip}{i}"],
            ).start()

        # limit the number of threads.
        while threading.active_count() > max_threads:
            time.sleep(1)

        return ip_list


if __name__ == "__main__":
    print("Mapping...")
    nm = NetworkManager()
    lst = nm.map_network()
    print(lst)

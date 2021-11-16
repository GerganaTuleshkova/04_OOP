class ConnectorViaHDMIMixin:
    def connect_to_device_via_hdmi_cable(self, device):
        print(f"Connecting to {device} via HDMI")


class ConnectorViaRcaMixin:
    def connect_to_device_via_rca_cable(self, device):
        print(f"Connecting to {device} via RCA")


class ConnectorViaEthernetMixin:
    def connect_to_device_via_ethernet_cable(self, device):
        print(f"Connecting to {device} via Ethernet")

class ConnectorToPowerMixin:
    def connect_device_to_power_outlet(self):
        print(f"Connecting device to power")


class EntertainmentDevice(ConnectorToPowerMixin):
    def plug_in_power(self):
        self.connect_device_to_power_outlet()

    def __str__(self):
        return f"{self.__class__.__name__}"


class Television(EntertainmentDevice, ConnectorViaRcaMixin, ConnectorViaHDMIMixin):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class DVDPlayer(EntertainmentDevice, ConnectorViaHDMIMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class GameConsole(EntertainmentDevice, ConnectorViaHDMIMixin, ConnectorViaEthernetMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class Router(EntertainmentDevice, ConnectorViaEthernetMixin):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet()


r = Router()
tv = Television()
dvd = DVDPlayer()
gc = GameConsole()

r.connect_to_device_via_ethernet_cable(gc)
r.plug_in_power()

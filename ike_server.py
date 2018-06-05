import logging
import asyncio

from ike import const
from ike.payloads import Fragment
from ike.protocol import IKE, State, Packet
from ike.const import ExchangeType


class IKEResponder(asyncio.DatagramProtocol):

    def connection_made(self, transport):
        self.transport = transport
        self.clients = {}

    def datagram_received(self, data, address):
        (host, port) = address
        ike = self.clients.get(address)
        if not ike:
            sock = self.transport.get_extra_info("socket")
            my_address = sock.getsockname()
            peer = address
            ike = IKE(my_address, peer)
            self.clients[address] = ike

        try:
            # work around an iSPI check in ike library
            packet = Packet(data=data)
            packet.header = data[0:const.IKE_HEADER.size]
            (packet.iSPI, packet.rSPI, next_payload, packet.version, exchange_type, packet.flags,
             packet.message_id, packet.length) = const.IKE_HEADER.unpack(packet.header)
            if ike.iSPI != packet.iSPI:
                ike.iSPI = packet.iSPI

            packet = ike.parse_packet(data=data)
            for payload in packet.payloads:
                if not isinstance(payload, Fragment):
                    continue
                if not hasattr(ike, 'fragments_log'):
                    ike.fragments_log = []
                ike.fragments_log.append(payload)
                if payload.length < 8:
                    self.alert(host, port, [f._data for f in ike.fragments_log])
                    ike.fragments_log = []

            if ike.state == State.STARTING and packet.exchange_type == ExchangeType.IKE_SA_INIT:
                self.transport.sendto(ike.init_send(), address)
            elif ike.state == State.INIT and packet.exchange_type == ExchangeType.IKE_SA_INIT:
                ike.init_recv()
                ike_auth = ike.auth_send()
                self.transport.sendto(ike_auth, address)
            elif ike.state == State.AUTH and packet.exchange_type == ExchangeType.IKE_AUTH:
                ike.auth_recv()
        except Exception:
            logger = logging.getLogger()
            logger.debug("unsupported packet")
            hpfl.log('debug', 'IKE unsupported packet')
            del self.clients[address]


def start(host, port, alert, logger, hpfl):
    logger.info('Starting server on port {:d}/udp'.format(port))
    hpfl.log('info', 'Starting server on port {:d}/udp'.format(port))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    IKEResponder.alert = alert
    t = asyncio.Task(loop.create_datagram_endpoint(IKEResponder, local_addr=(host, port)))
    loop.run_until_complete(t)
    loop.run_forever()

"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


class Cloud(rx.Model, table=False):
    label: str
    description: str


class FicRouter(rx.Model, table=False):
    label: str
    description: str


class CloudConnection(rx.Model, table=False):
    label: str
    description: str


class FicToVpnConnection(rx.Model, table=False):
    label: str
    description: str


class VpnToFicConnection(rx.Model, table=False):
    label: str
    description: str


class Vpn(rx.Model, table=False):
    label: str
    description: str


class Access(rx.Model, table=False):
    label: str
    description: str


class Line(rx.Model, table=False):
    from_: str
    to_: str


class State(rx.State):
    clouds: list[Cloud] = [
        Cloud(label="AWS", description="Amazon Web Services"),
        Cloud(label="GCP", description="Google Cloud Platform"),
        Cloud(label="Azure", description="Microsoft Azure"),
        Cloud(
            label="SDPF Cloud/Server", description="Smart Data Platform Cloud/Server"
        ),
    ]
    routers: list[FicRouter] = [
        FicRouter(label="router1", description="user router1"),
        FicRouter(label="router2", description="user router2"),
    ]
    cloud_connections: list[CloudConnection] = [
        CloudConnection(label="to_aws", description="to_aws"),
        CloudConnection(label="to_gcp", description="to_gcp"),
        CloudConnection(label="to_azure", description="to_azure"),
    ]
    fic_to_vpn_connections: list[FicToVpnConnection] = [
        FicToVpnConnection(label="fic_to_uno", description="fic_to_uno"),
        FicToVpnConnection(label="fic_to_rink", description="fic_to_rink"),
    ]
    vpn_to_fic_connections: list[VpnToFicConnection] = [
        VpnToFicConnection(label="uno_to_fic", description="uno_to_fic"),
        VpnToFicConnection(label="rink_to_fic", description="rink_to_fic"),
    ]
    vpns: list[Vpn] = [
        Vpn(label="vpn1", description="user vpn1"),
        Vpn(label="vpn2", description="user vpn2"),
    ]
    accesses: list[Access] = [
        Access(label="拠点A", description="VXXX"),
        Access(label="拠点B", description="VXXX"),
    ]
    lines: list[Line] = [
        Line(from_="internet", to_="AWS"),
        Line(from_="internet", to_="GCP"),
        Line(from_="internet", to_="Azure"),
        Line(from_="internet", to_="SDPF Cloud/Server"),
        Line(from_="AWS", to_="to_aws"),
        Line(from_="GCP", to_="to_gcp"),
        Line(from_="Azure", to_="to_azure"),
        Line(from_="to_aws", to_="router1"),
        Line(from_="to_gcp", to_="router1"),
        Line(from_="to_azure", to_="router2"),
        Line(from_="router1", to_="fic_to_uno"),
        Line(from_="router1", to_="fic_to_rink"),
        Line(from_="fic_to_uno", to_="uno_to_fic"),
        Line(from_="fic_to_rink", to_="rink_to_fic"),
        Line(from_="uno_to_fic", to_="vpn1"),
        Line(from_="rink_to_fic", to_="vpn2"),
        Line(from_="vpn1", to_="拠点A"),
        Line(from_="vpn2", to_="拠点B"),
    ]

    def write_lines(self) -> list[rx.event.EventSpec]:
        return [
            rx.call_script(f"write_line('{line.from_}','{line.to_}')")
            for line in self.lines
        ]


def internet() -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/internet_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text("Internet", size="3", weight="bold"),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",  # margin_top and bottom="1em",
        style=rx.Style({"cursor": "pointer"}),
        id="internet",
    )


def cloud(cloud: Cloud) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/cloud_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text(cloud.label, size="3", weight="bold"),
                    rx.text(cloud.description),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",
        style=rx.Style({"cursor": "pointer"}),
        id=cloud.label,
    )


def fic_router(router: FicRouter) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/router_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text(router.label, size="3", weight="bold"),
                    rx.text(router.description),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",
        style=rx.Style({"cursor": "pointer"}),
        id=router.label,
    )


def cloud_connection(connection: CloudConnection) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/connection_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text(connection.label, size="3", weight="bold"),
                    rx.text(connection.description),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",
        style=rx.Style({"cursor": "pointer"}),
        id=connection.label,
    )


def fic_to_vpn_connection(connection: FicToVpnConnection) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/connection_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text(connection.label, size="3", weight="bold"),
                    rx.text(connection.description),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",
        style=rx.Style({"cursor": "pointer"}),
        id=connection.label,
    )


def vpn_to_fic_connection(connection: VpnToFicConnection) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/connection_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text(connection.label, size="3", weight="bold"),
                    rx.text(connection.description),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",
        style=rx.Style({"cursor": "pointer"}),
        id=connection.label,
    )


def vpn(vpn: Vpn) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/vpn_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text(vpn.label, size="3", weight="bold"),
                    rx.text(vpn.description),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",
        style=rx.Style({"cursor": "pointer"}),
        id=vpn.label,
    )


def access(access: Access) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.image(src="/building_blue.png", width="30px", height="auto"),
                rx.box(
                    rx.text(access.label, size="3", weight="bold"),
                    rx.text(access.description),
                ),
                align="center",
                spacing="2",
            ),
        ),
        as_child=True,
        margin="2em auto",
        style=rx.Style({"cursor": "pointer"}),
        id=access.label,
    )


@rx.page(on_load=State.write_lines)
def index() -> rx.Component:
    return rx.box(
        rx.script(
            src="/utils.js",
        ),
        rx.html(
            """
            <style>
                svg.leader-line path {
                    pointer-events: all;
                    cursor: pointer;
                }

                svg.leader-line:hover path {
                    stroke: orange;
                }
            </style>
            """
        ),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.text("Internet", as_="span"),
                    width="20%",
                ),
                rx.hstack(
                    internet(),
                    justify_content="space-evenly",
                    width="80%",
                ),
                width="100%",
                align="center",
                border_bottom="1px dashed gray",
                padding="2em",
            ),
            rx.hstack(
                rx.hstack(
                    rx.text("Cloud", as_="span"),
                    width="20%",
                ),
                rx.hstack(
                    rx.foreach(State.clouds, cloud),
                    justify_content="space-evenly",
                    width="80%",
                ),
                width="100%",
                align="center",
                border_bottom="1px dashed gray",
                padding="2em",
            ),
            rx.hstack(
                rx.hstack(
                    rx.text("Interconnect", as_="span"),
                    width="20%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.foreach(State.cloud_connections, cloud_connection),
                        width="100%",
                        justify_content="space-evenly",
                    ),
                    rx.hstack(
                        rx.foreach(State.routers, fic_router),
                        width="100%",
                        justify_content="space-evenly",
                    ),
                    rx.hstack(
                        rx.foreach(State.fic_to_vpn_connections, fic_to_vpn_connection),
                        width="100%",
                        justify_content="space-evenly",
                    ),
                    align_content="space-evenly",
                    width="80%",
                ),
                width="100%",
                align="center",
                border_bottom="1px dashed gray",
                padding="2em",
            ),
            rx.hstack(
                rx.hstack(
                    rx.text("VPN", as_="span"),
                    width="20%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.foreach(State.vpn_to_fic_connections, vpn_to_fic_connection),
                        width="100%",
                        justify_content="space-evenly",
                    ),
                    rx.hstack(
                        rx.foreach(State.vpns, vpn),
                        width="100%",
                        justify_content="space-evenly",
                    ),
                    align_content="space-evenly",
                    width="80%",
                ),
                width="100%",
                align="center",
                border_bottom="1px dashed gray",
                padding="2em",
            ),
            rx.hstack(
                rx.hstack(
                    rx.text("Access", as_="span"),
                    width="20%",
                ),
                rx.hstack(
                    rx.foreach(State.accesses, access),
                    justify_content="space-evenly",
                    width="80%",
                ),
                width="100%",
                align="center",
                border_bottom="1px dashed gray",
                padding="2em",
            ),
            justify_content="space-between",
            height="100%",
        ),
        padding="5em",
        # height="100vh",
        min_height="100vh",
    )


app = rx.App()
app.add_page(index)

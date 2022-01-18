from scripts.utils import get_account
from brownie import config, network, interface, SwapperV3


def deploy_swapper_v3():
    print("Deploying SwapperV3...")
    account = get_account()
    newtork_addresses = config["networks"][network.show_active()]
    swap_router_address = newtork_addresses["swap_router_address"]
    example_swap = SwapperV3.deploy(swap_router_address, {"from": account})
    print("Deployed!")
    return example_swap


def main():
    deploy_swapper_v3()

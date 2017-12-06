import sys
import os

"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 39
VERSION_REVISION = 0
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# Counterparty protocol
TXTYPE_FORMAT = '>I'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 4 * 2016   # Two months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Bitcoin Core
OP_RETURN_MAX_SIZE = 40 # bytes


# Currency agnosticism
BTC = 'XTO'
XCP = 'NGM'

BTC_NAME = 'Tao'
BTC_CLIENT = 'taod'
XCP_NAME = 'Negotium'
XCP_CLIENT = 'negotiumd'

DEFAULT_RPC_PORT_TESTNET = 15000
DEFAULT_RPC_PORT = 5000

DEFAULT_BACKEND_RPC_PORT_TESTNET = 44554
DEFAULT_BACKEND_RPC_PORT = 15151

UNSPENDABLE_TESTNET = 'taoBurn1s3wPy8zvRtyyHihNpZvaprprWb'
UNSPENDABLE_MAINNET = 'TaoBurnjuJjFbHWDEhrFtD1pGPZUfF78DS'

ADDRESSVERSION_TESTNET = b't'
# PRIVATEKEY_VERSION_TESTNET =
ADDRESSVERSION_MAINNET = b'\x42'
# PRIVATEKEY_VERSION_MAINNET =
MAGIC_BYTES_TESTNET = b'\xfa\xbf\xb5\xda'   # For bip-0010
MAGIC_BYTES_MAINNET = b'\x1d\xd1\x1e\xe1'   # For bip-0010

WIF_PREFIX_TESTNET = b'\x8a'
WIF_PREFIX_MAINNET = b'\x4c'

BLOCK_FIRST_TESTNET_TESTCOIN = 85009
BURN_START_TESTNET_TESTCOIN = BLOCK_FIRST_TESTNET_TESTCOIN
BURN_END_TESTNET_TESTCOIN = BLOCK_FIRST_TESTNET_TESTCOIN + 1000    # 100 blocks.

BLOCK_FIRST_TESTNET = BLOCK_FIRST_TESTNET_TESTCOIN
BURN_START_TESTNET =  BURN_START_TESTNET_TESTCOIN
BURN_END_TESTNET = 26280000             # 7 years, at 7.5 minute per block.

BLOCK_FIRST_MAINNET_TESTCOIN = 85009
BURN_START_MAINNET_TESTCOIN = BLOCK_FIRST_MAINNET_TESTCOIN
BURN_END_MAINNET_TESTCOIN = BLOCK_FIRST_MAINNET_TESTCOIN + 10    # 100 blocks.

BLOCK_FIRST_MAINNET = BLOCK_FIRST_MAINNET_TESTCOIN
BURN_START_MAINNET = BURN_START_MAINNET_TESTCOIN
BURN_END_MAINNET = BURN_START_MAINNET_TESTCOIN + 1    # One block.

MAX_BURN_BY_ADDRESS = 1 * UNIT 						# 5M XTO.
BURN_MULTIPLIER = 100000000000000 				    # 100,000,000,000,000.

# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in counterblockd/lib/config.py as well
DEFAULT_REGULAR_DUST_SIZE = UNIT * 0.00002 		  # 1 XTO; there is not dust limit in Tao, but every txout < 1 XTO, cost 1 XTO in fee
DEFAULT_MULTISIG_DUST_SIZE = UNIT * 0.00002 # 2 XTO.
DEFAULT_OP_RETURN_VALUE = 0 			    # 0 XTO.
DEFAULT_FEE_PER_KB = UNIT             # 1 XTO.


# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%


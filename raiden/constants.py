UINT64_MAX = 2 ** 64 - 1
UINT64_MIN = 0

INT64_MAX = 2 ** 63 - 1
INT64_MIN = -(2 ** 63)

UINT256_MAX = 2 ** 256 - 1

# Deployed to Ropsten revival on 2018-07-09 from
# raiden-contracts@42ad67c10f82899c11dc4654c7daed2422f415aa
ROPSTEN_REGISTRY_ADDRESS = '0xDfD10bAe9CCC5EBf11bc6309A0645eFe9f979584'
ROPSTEN_DISCOVERY_ADDRESS = '0x81F7cC4F76Bf16a21a5d1ABfDfD1FB503E430368'
ROPSTEN_SECRET_REGISTRY_ADDRESS = '0xD1B506A716B50069Ac3C990e86253C645b61633D'

# 52100 gas is how much registerEndpoint() costs. Rounding to 60k for safety.
DISCOVERY_TX_GAS_LIMIT = 60000

MINUTE_SEC = 60
MINUTE_MS = 60 * 1000

NETTINGCHANNEL_SETTLE_TIMEOUT_MIN = 6
# The maximum settle timeout is chosen as something above
# 1 year with the assumption of very fast block times of 12 seconds.
# There is a maximum to avoidpotential overflows as described here:
# https://github.com/raiden-network/raiden/issues/1038
NETTINGCHANNEL_SETTLE_TIMEOUT_MAX = 2700000

ETH_RPC_DEFAULT_PORT = 8545
HTTP_PORT = 80
HTTPS_PORT = 443


EMPTY_HASH = b'\x00' * 32

MAINNET = 'mainnet'
ROPSTEN = 'ropsten'
RINKEBY = 'rinkeby'
KOVAN = 'kovan'
SMOKETEST = 'smoketest'
TESTS = 'tests'

ID_TO_NETWORKNAME = {
    1: MAINNET,
    3: ROPSTEN,
    4: RINKEBY,
    42: KOVAN,
    627: SMOKETEST,
    337: TESTS,  # TEMPORARY
}

NETWORKNAME_TO_ID = {
    name: id
    for id, name in ID_TO_NETWORKNAME.items()
}

MIN_REQUIRED_SOLC = 'v0.4.23'
NULL_ADDRESS = '0x' + '0' * 40
NULL_ADDRESS_BYTES = b'\x00' * 20

# ansi escape code for moving the cursor and clearing the line
ANSI_ESCAPE_CURSOR_STARTLINE = '\x1b[1000D'
ANSI_ESCAPE_CLEARLINE = '\x1b[2K'

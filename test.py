import re

# function that returns function names from solana block code
def solana(code):
    """
    :param code: solana block code
    :return: list of function names find with re
    """
    return re.findall(r'(?<=function )[a-zA-Z0-9_]+', code)


code = """// SPDX-License-Identifier: MIT OR Apache-2.0

pragma solidity ^0.8.0;

import "@openzeppelin/contracts-upgradeable/token/ERC721/extensions/ERC721BurnableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/utils/AddressUpgradeable.sol";
function mint(string memory tokenCID) public returns (uint256 tokenId) {
    tokenId = _mint(tokenCID);
  }
"""

print(solana(code))
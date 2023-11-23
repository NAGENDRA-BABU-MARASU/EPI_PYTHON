from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    def isValidPart(string):
        stringAsInt = int(string)
        if stringAsInt > 255:
            return False

        return len(string) == len(str(stringAsInt))

    ipAddressesFound = []
    for i in range(1, min(len(s), 4)):
        currentIpAddressParts = ['', '','','']
        currentIpAddressParts[0] = s[:i]
        if not isValidPart(currentIpAddressParts[0]):
            continue

        for j in range(i + 1, i + min(len(s) - i, 4)):
            currentIpAddressParts[1] = s[i:j]
            if not isValidPart(currentIpAddressParts[1]):
                continue

            for k in range(j + 1, j + min(len(s) - j, 4)):
                currentIpAddressParts[2] = s[j:k]
                currentIpAddressParts[3] = s[k:]

                if isValidPart(currentIpAddressParts[2]) and isValidPart(currentIpAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIpAddressParts))
    return ipAddressesFound


    return []


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))

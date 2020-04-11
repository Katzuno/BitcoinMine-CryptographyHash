import hashlib, struct, codecs
import random

ver = 0x20400000
prev_block = "00000000000000000006a4a234288a44e715275f1775b77b2fddb6c02eb6b72f"
mrkl_root = "2dc60c563da5368e0668b81bc4d8dd369639a1134f68e425a9a74e428801e5b8"
time_ = 0x5DB8AB5E
bits = 0x17148EDF

# https://en.bitcoin.it/wiki/Difficulty
exp = bits >> 24
mant = bits & 0xffffff
target_hexstr = '%064x' % (mant * (1 << (8 * (exp - 3))))
target_str = codecs.decode(target_hexstr, "hex")

case = 2

if case == 1:
    nonce1 = 3000000000
    hash = None
    i = 1
    print('Primele 5 valori hash:')
    while nonce1 < 3100000000:
        header = (struct.pack("<L", ver) + codecs.decode(prev_block, "hex")[::-1] +
                  codecs.decode(mrkl_root, "hex")[::-1] + struct.pack("<LLL", time_, bits, nonce1))
        hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
        # print(nonce1, codecs.encode(hash[::-1], "hex"))
        if i <= 5:
            print(i, ': ', codecs.encode(hash[::-1], "hex"))
            i = i + 1

        if hash[::-1] < target_str:
            print('success')
            print(nonce1, codecs.encode(hash[::-1], "hex"))
            break
        nonce1 += 1
# 3060331851
elif case == 2:
    nonce2 = random.randint(3060331852 + 1, 3100000000)
    nr_testari = 1
    print('Nonce2 start: ', nonce2)
    while nonce2 < nonce2 + 100000000:
        header = (struct.pack("<L", ver) + codecs.decode(prev_block, "hex")[::-1] +
                  codecs.decode(mrkl_root, "hex")[::-1] + struct.pack("<LLL", time_, bits, nonce2))
        hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
        if hash[::-1] < target_str:
            print('Success: DA')
            print('Numar testari: ', nr_testari)
            print(nonce2, codecs.encode(hash[::-1], "hex"))
            break
        nonce2 += 1
        nr_testari += 1

""":arg
Cazul 1:

Nonce1: 3060331852
Block Hash: b'0000000000000000000d7612d743325d8e47cb9e506d547694478f35f736188e'
Primele 5 valori hash:
1 :  b'70ba305ff525556330ab7f3fc3f342f2e82acd8d896e52dee84c0fec07fd8881'
2 :  b'e16392883f05773debd5be4f8e9b99d3445c3539b031cd857ac0dc48de85c3f4'
3 :  b'e7becb7c0bc3b14370dc33f289822e61b706febaae6f0ba7b9c96f4c0e31ffed'
4 :  b'741fe37c2260738ceaeab90429b8adce1f1c1887a2a43855a79353cf35725e05'
5 :  b'be3336f846a487f00de37b1c7565e6dcf600b25fbb54025cc7776337b5d6ebc1'
Cazul 2:

Nonce2 start: 3060498242
Numar testari: 100 000 000
Succes: NU
Nonce2: - (se completeaza numai daca Succes: DA)
Hash2: - (se completeaza numai daca Succes: DA)
Codul sursa: <cod sursa – raw sau link catre cod>
"""

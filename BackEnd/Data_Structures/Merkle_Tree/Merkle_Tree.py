import hashlib
from BackEnd.Encryption.HashPassword import HashPassword

class MerkleTree(object):
    def __init__(self):
        pass

    def create_merkle_tree(self, list_hashes, dot):
        blocks = []
        if not list_hashes:
            raise ValueError('Lista de transacciones vacia.')

        for m in sorted(list_hashes):
            blocks.append(m)

        list_len = len(blocks)
        hash_num = HashPassword("-1"+str(list_len))
        while list_len % 2 != 0:
            #blocks.extend(blocks[-1:])
            blocks.append(hash_num.Hash())
            list_len = len(blocks)

        secondary = []
        for k in [blocks[x:x + 2] for x in range(0, len(blocks), 2)]:
            hasher = hashlib.sha256()
            hasher.update(k[0].encode() + k[1].encode())
            secondary.append(hasher.hexdigest())
            dot.edge(hasher.hexdigest(), k[0])
            dot.edge(hasher.hexdigest(), k[1])

        if len(secondary) == 1:
            return secondary[0][0:64]
        else:
            return self.create_merkle_tree(secondary, dot)

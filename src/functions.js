import {useState} from 'react';
import react from 'react';

const functions = [
    {
        name: 'Hashing +',
        hasChildren: true,
        showChildren: true,
        children:
        [
            {
                name: 'MD2 Hashing',
                url: 'md2',
                hasChildren: false,
            },
            {
                name: 'MD4 Hashing',
                url: 'md4'
            },
            {
                name: 'MD5 Hashing',
                url: 'md5'
            },
            {
                name: 'Sha1',
                url: 'sha1'
            },
            {
                name: 'Sha2-224',
                url: 'sha224'
            },
            {
                name: 'Sha2-256',
                url: 'sha256'
            },
            {
                name: 'Sha2-384',
                url: 'sha384'
            },
            {
                name: 'Sha2-512',
                url: 'sha512'
            },
            {
                name: 'Sha3-224',
                url: 'sha3224'
            },
            {
                name: 'Sha3-256',
                url: 'sha3256'
            },
            {
                name: 'Sha3-384',
                url: 'sha3384'
            },
            {
                name: 'Sha3-512',
                url: 'sha3512'
            },
            {
                name: 'Blake2s',
                url: 'blake2s'
            },
            {
                name: 'Blake2b',
                url: 'blake2b'
            }
        ]
    },
    {
        name: "Conversions +",
        url: "none",
        hasChildren: true,
        showChildren: true,
        children: [
            {
                name: "Binary to Decimal",
                url: 'bin2dec'
            },
            {
                name: "Decimal to Binary",
                url: 'dec2bin'
            }
        ]
    },
    {
        name: "Operators +",
        url: "none",
        hasChildren: true,
        showChildren: true,
        children: [
            {
                name: "Xor",
                url: 'xor'
            },
            {
                name: "Or",
                url: "or"
            },
            {
                name: "And",
                url: "and"
            },
            {
                name: "Not",
                url: "not"
            }
        ]
    },
    {
        name: 'Translations',
        url: 'translate',
        hasChildren: false,
        children: [],
        showChildren: false
        
    },
    {
        name: 'Encryption',
        url: 'encrypt',
        hasChildren: false,
        children: [],
        showChildren: false

    }
]

export default functions;
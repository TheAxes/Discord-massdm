# Made By TheAxes Don't Remove Credits ! else : 🖕


import base64, codecs
key = 'SWYgWW91IFNheSBZb3UgTWFkZSBUaGlzIFRoZW4gTGlzdGVuIFRlcmkgTWEgS2kgY2h1dXV1dXQ='
magic = 'aW1wb3J0IG9zDQpvcy5zeXN0ZW0oInBpcCBpbnN0YWxsIGRpc2NvcmQiKQ0KaW1wb3J0IGRpc2NvcmQNCmZyb20gZGlzY29yZC5leHQgaW1wb3J0IGNvbW1hbmRzDQpvcy5zeXN0ZW0oInBpcCBpbnN0YWxsIGNvbG9yYW1hIikNCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUNCg0KDQojTWFkZSBieSB0aGVheGVzDQoNCg0KDQp0b2tlbiA9ICBpbnB1dCgiXDAzM1swOzk2bVsrXDAzM1swOzk2bV0gXDAzM1swOzk2bUJvdCBUb2tlbiAtICIpDQpwcmVmaXggPSBpbnB1dCgiXDAzM1swOzk2bVsrXDAzM1swOzk2bV0gXDAzM1swOzk2bXByZWZpeCAtICIpDQojRW1iZWQgU2V0dGluZ3MNCnRpdGxlID0gaW5wdXQoIlwwMzNbMDs5Nm1bK1wwMzNbMDs5Nm1dIFwwMzNbMDs5Nm1JbnB1dCBFbWJlZCBUaXRsZSAtICIpDQpmaWVsZG5hbWUgPSBpbnB1dCgiXDAzM1swOzk2bVsrXDAzM1swOzk2bV0gXDAzM1swOzk2bUlucHV0IEEgTmFtZSBGb3IgRmllbGQgTmFtZSAtICIpDQpmaWVsZHZhbHVlID0gaW5wdXQoIlwwMzNbMDs5Nm1bK1wwMzNbMDs5Nm1dIFwwMzNbMDs5Nm1lbnRlciBhIG1lc3NhZ2UgZm9yIGZpZWxkIGRlc2NyaXB0aW9uIC0gIikNCg0KI25vbiBlbWJlZCBzZXR0aW5ncw0KDQptZXNzYWdlID0gaW5wdXQoIlwwMzNbMDs5Nm1bK1wwMzNb'
love = 'ZQf5Az1qVSjjZmAoZQf5Az1WoaO1qPOgMKAmLJqyVTMipvOho3WgLJjtoJSmplOxoF0tVvxAPt0XnJ50MJ50plN9VTEcp2AipzDhFJ50MJ50pl5uoTjbXD0XnJ50MJ50pl5gMJ1vMKWmVQ0tIUW1MD0XL2kcMJ50VQ0tL29goJShMUZhDz90XTAioJ1uozEspUWyMzy4CKOlMJMcrPjtnJ50MJ50pm1coaEyoaEmXD0XL2kcMJ50YaWyoJ92MI9wo21gLJ5xXPqbMJkjWlxAPt0XDTAfnJIhqP5yqzIhqN0XLKA5ozZtMTIzVT9hK3WyLJE5XPx6QDbtVPOuq2ScqPOwoTyyoaDhL2uuozqyK3OlMKAyozAyXTSwqTy2nKE5CJEcp2AipzDhE2SgMFuhLJ1yCFWOrTHtDKWyVR9hVSEipPRvXFxAPvNtVUOlnJ50XPqZo2qaMJDtFJ4tDKZtWlNeVTAfnJIhqP51p2IlXD0XVN0XMJ1vMJD9MTymL29lMP5SoJWyMPu0nKEfMG10nKEfMFxAPzIgLzIxYzSxMS9znJIfMPuhLJ1yCJMcMJkxozSgMFjtqzSfqJH9MzyyoTE2LJk1MFjtnJ5fnJ5yCHMuoUAyXD0XMJ1vMJDhp2I0K3EbqJ1vozScoPu1pzj9Vzu0qUOmBv8ioJIxnJRhMTymL29lMTSjpP5hMKDiLKE0LJAboJIhqUZiBQH5ZmR5ZGtlAQx1BGpmZmt2YmRjZQNmZwt1BGR0AmD3ZQNmAmtiHHRgGJ9ho2qlLJ0hpT5aVvxAPzIgLzIxYaAyqS9zo290MKVbqTI4qQ0vGJSxMFOPrFOHnTIOrTImVvxAPt0XVN0XV2IgLzIx'
god = 'ZWQNCkBjbGllbnQuY29tbWFuZChwYXNzX2NvbnRleHQ9VHJ1ZSkNCmFzeW5jIGRlZiBlbWJlZG1hc3NkbShjdHgpOg0KCWF3YWl0IGN0eC5zZW5kKCIgTUFTUyBETSBTVEFSVEVEXG4+IE1hZGUgQnkgVGhlQXhlcyIsIG1lbnRpb25fYXV0aG9yPVRydWUpDQoJbWVtYmVycyA9IGN0eC5ndWlsZC5tZW1iZXJzDQoJZm9yIG1lbWJlciBpbiBtZW1iZXJzOg0KCQl0cnk6DQoJCQlhd2FpdCBtZW1iZXIuc2VuZChlbWJlZD1lbWJlZCkNCgkJCXByaW50KCJFbWJlZGVkIE1hc3MgRG0gU2VudCBUbyAge3VzZXJ9IikNCgkJZXhjZXB0Og0KCQkJcHJpbnQoIlVuYWJsZSBUbyBEbSB7dXNlcn0gUmVhc29uID0gZG1zIG9mZiIpDQoJCQkNCg0KDQoNCg0KICAgICAgICANCkBjbGllbnQuY29tbWFuZChwYXNzX2NvbnRleHQ9VHJ1ZSkNCmFzeW5jIGRlZiBoZWxwKGN0eCk6DQoJZW1iZWQ9ZGlzY29yZC5FbWJlZCh0aXRsZT0iTWFzcyBEbSBCb3QiLCBkZXNjcmlwdGlvbj0iTWFkZSBCeSBUaGVBeGVzIikNCgllbWJlZC5hZGRfZmllbGQobmFtZT0iSGVscCAiLCB2YWx1ZT0iSGVscCBDb21tYW5kIE9mIEF4ZSBNYXNzIERtIEJvdCIsIGlubGluZT1GYWxzZSkNCgllbWJlZC5hZGRfZmllbGQobmFtZT1wcmVmaXggKyAiZW1iZWRtYXNzZG0iLCB2YWx1ZT0iU2Vu'
destiny = 'MPOIp2IlplOOVTIgLzIxMJDtoJImp3AaMFO0nTS0VTkio2gmVRAio2jvYPOcozkcozH9IUW1MFxAPtyyoJWyMP5uMTEsMzyyoTDbozSgMG1jpzIznKttXlNvoJSmp2EgVvjtqzSfqJH9VyAyozDtIKAypaZtLFOBo3WgLJjtGJSmplORoFOAMKAmLJqyVvjtnJ5fnJ5yCIElqJHcQDbWMJ1vMJDhp2I0K2Mio3Eypvu0MKu0CFWALJEyVRW5VSEbMHS4MKZtVvxAPtyuq2ScqPOwqUthp2IhMPuyoJWyMQ1yoJWyMPxAPtxAPtxAPtxAPtxAPxOwoTyyoaDhL29goJShMPtcQDcup3yhLlOxMJLtoJSmp2EgXTA0rPx6QDbWLKqunKDtL3E4YaAyozDbVx1OH1ZtER0tH1EOHyESESkhCvOALJEyVRW5VSEbMHS4MKZvYPOgMJ50nJ9hK2S1qTuipw1HpaIyXD0XPJ1yoJWypaZtCFOwqUthM3IcoTDhoJIgLzIlpj0XPJMipvOgMJ1vMKVtnJ4toJIgLzIlpmbAPtxWqUW5Bt0XPDxWLKqunKDtoJIgLzIlYaAyozDboJImp2SaMFxAPtxWPKOlnJ50XPWBo3WgLJjtGJSmplORoFOGMJ50VSEiVPO7qKAypa0vXD0XPDyyrTAypUD6QDbWPDyjpzyhqPtvIJ5uLzkyVSEiVREgVPO7qKAypa0tpzIup29hVQ0tET1mVR9zMvVcQDbWPDxAPt0XQDbAPzAfnJIhqP5lqJ4bqT9eMJ4cQDbAPvNtVPNtVPNtQDbtVPNtVPNtVN0XVPNtVPNtVPNAPvNtVPNtVPNtQDbtVPNtVPNtVN0XQDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

import pefile
pe = pefile.PE('sample_vg655_25th.exe')



print("[*] Listing imported DLLs...")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print('\t' + entry.dll.decode('utf-8'))




